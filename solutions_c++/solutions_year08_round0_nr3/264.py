// 
//	Alexandr Chupilko, 2008
//	
//	Fly Swatter
//

#include <iostream>	
#include <string>
#include <fstream>
#include <math.h>
#include <time.h>


using namespace std;

typedef long double tValue;

inline bool pointInDisk(tValue Rad, tValue x, tValue y)
{
	if (x * x + y * y  <= Rad * Rad)
	{
		return true;
	}
	return false;
}

int freeSquare(tValue Rad, tValue x1, tValue y1, tValue x2, tValue y2)
{

	if (Rad - sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) >= (sqrt((x1 + x2) * (x1 + x2) + (y1 + y2) * (y1 + y2))) / 2)
	{
		return 0;
	}
	if (Rad + sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) <= (sqrt((x1 + x2) * (x1 + x2) + (y1 + y2) * (y1 + y2))) / 2)
	{
		return 2;
	}

	bool
		x1y1 = pointInDisk(Rad, x1, y1),
		x1y2 = pointInDisk(Rad, x1, y2),
		x2y1 = pointInDisk(Rad, x2, y1),
		x2y2 = pointInDisk(Rad, x2, y2);

	if (x1y1 && x1y2 && x2y1 && x2y2)
	{
		return 0;
	}

	if (!(x1y1 || x1y2 || x2y1 || x2y2))
	{
		return 2;
	}

	return 1;
}

inline tValue segmentArea(tValue Rad, tValue x1, tValue y1, tValue x2, tValue y2)
{
	tValue alph_sin = abs(x1 * y2 - x2 * y1) / (Rad * Rad);
	tValue alph = asinl(alph_sin);
	return abs((Rad * Rad * (alph - alph_sin)) / 2);
}

double badSquareArea(tValue Rad, tValue x1, tValue y1, tValue x2, tValue y2)
{
	bool
		x1y1 = pointInDisk(Rad, x1, y1),
		x1y2 = pointInDisk(Rad, x1, y2),
		x2y1 = pointInDisk(Rad, x2, y1),
		x2y2 = pointInDisk(Rad, x2, y2);
	
	// assume it's first quadrant (simmetria)
	if (!x1y1)	return 0;
	if (x2y2)	return abs((x1 - x2) * (y1 - y2));

	tValue y1_ir, x1_ir, y2_ir, x2_ir, result;


	// now x1y1 and !x2y2
	if ((!x1y2) && (!x2y1))
	{
		y1_ir = sqrt(Rad * Rad - x1 * x1);
		x1_ir = sqrt(Rad * Rad - y1 * y1);
		result = (abs((y1_ir - y1) * (x1_ir - x1)) / 2) + segmentArea(Rad, x1, y1_ir, x1_ir, y1);
		return result;
	}
	if (x1y2 && (!x2y1))
	{
		x1_ir = sqrt(Rad * Rad - y2 * y2);
		x2_ir = sqrt(Rad * Rad - y1 * y1);
		result = abs((y1 - y2) * (min(x1_ir, x2_ir) - x1));
		result += abs((y1 - y2) * (max(x1_ir, x2_ir) - min(x1_ir, x2_ir))) / 2;
		result += segmentArea(Rad, x2_ir, y1, x1_ir, y2);
		return result;
	}
	if ((!x1y2) && x2y1)
	{
		y1_ir = sqrt(Rad * Rad - x2 * x2);
		y2_ir = sqrt(Rad * Rad - x1 * x1);
		result = abs((x1 - x2) * (min(y1_ir, y2_ir) - y1));
		result += abs((x1 - x2) * (max(y1_ir, y2_ir) - min(y1_ir, y2_ir))) / 2;
		result += segmentArea(Rad, x1, y2_ir, x2, y1_ir);
		return result;
	}
	if (x1y2 && x2y1)
	{
		y2_ir = sqrt(Rad * Rad - x2 * x2);
		x2_ir = sqrt(Rad * Rad - y2 * y2);
		result = abs((y1 - y2) * (x2_ir - x1));
		result += abs((y1 - y2_ir) * (x2_ir - x2));
		result += abs((y2 - y2_ir) * (x2_ir - x2)) / 2;
		result += segmentArea(Rad, x2_ir, y2, x2, y2_ir);
		return result;
	}
}

double calcProbability(tValue f, tValue R, tValue t, tValue r, tValue g)
{
	tValue innerRad = R - t - f;
	tValue period = 2 * r + g;
	tValue start1 = r + f, start2 = r + g - f;
	int freeSquares = 0;
	tValue badSquareAreas = 0;
	if (g <= 2 * f) return 1;
	if (innerRad <= 0) return 1;
	// now, g > 2 * f and R - t > f
	tValue x1, x2, y1, y2;
	x1 = start1;
	y1 = start1;
	x2 = start2;
	y2 = start2;

	int lines = 0, cols = 0;
	while (true)
	{
		switch (freeSquare(innerRad, x1, y1, x2, y2)) 
		{
			case 0:
				freeSquares++;
				cols++;
				x1 = start1 + period * cols;
				x2 = start2 + period * cols;
			break;
			case 1:
				badSquareAreas += badSquareArea(innerRad, x1, y1, x2, y2);
				cols++;
				x1 = start1 + period * cols;
				x2 = start2 + period * cols;
			break;
			case 2:
				if (cols == 0)
				{
					return 1 - 
						((((start2 - start1) * (start2 - start1) * ((double)freeSquares) + badSquareAreas) * 4) 
						/ (3.14159265358979323846 * R * R));
				}
				cols = 0;
				lines++;
				x1 = start1;
				x2 = start2;
				y1 = start1 + period * lines;
				y2 = start2 + period * lines;
			break;
		}
	}
}

string double2String(tValue d, int digits)
{
	char tmp[10];
	sprintf(tmp, "%f", d);
	//gcvt(d, digits, tmp);
	return tmp;
}

void answerQuestions(istream& in, ostream& out)
{
	size_t n;
	tValue f, R, t, r, g;
	int digits = 6;
	tValue result;
	in >> n;
	for(size_t i = 1; i <= n; i++)
	{
		in >> f >> R >> t >> r >> g;
		result = calcProbability(f, R, t, r, g);
		out << "Case #" << i << ": " << double2String(result, digits) << endl;
	}
}


int main(int argc, char* argv[])
{
	if(argc>3) {
		cerr << "Usage: <Input file> <Output file>" << endl;
		return EXIT_FAILURE;
	}
	char f_in[256], f_out[256];

	if (argc<3){strcpy_s(f_out,"C-large.out");}else{strcpy_s(f_out,argv[2]);};
	if (argc<2){strcpy_s(f_in,"C-large.in");}else{strcpy_s(f_in,argv[1]);};

	ifstream in(f_in);
	ofstream out(f_out);

	if (!in){
		cerr << "Bad Input file: " << f_in << endl;
		return EXIT_FAILURE;
	}
	if (!out){
		cerr << "Bad Output file: " << f_out << endl;
		return EXIT_FAILURE;
	}

	answerQuestions(in, out);

	return EXIT_SUCCESS;
}

