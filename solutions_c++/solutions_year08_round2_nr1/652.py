#include <iostream>
#include <fstream>
#include <map>
#include <math.h>


using namespace std;


#define epsi	0.000000001
#define D_EQL(x, y)		(((x-y) < epsi) && ((x-y) > -epsi))
#define sqr(x)		(x)*(x)

int n, A, B, C, D, _x00, _y00, M;

double *X;
double *Y;



bool ispequal(int p1, int p2)	// is point equal
{
	if ((((X[p1] - X[p2]) < epsi) && ((X[p1] - X[p2]) > -epsi)) &&
		(((Y[p1] - Y[p2]) < epsi) && ((Y[p1] - Y[p2]) > -epsi)))
	{
		return true;
	}

	return false;
}

bool iscntrdtrngl(int p1, int p2, int p3)
{
	double dCx = (X[p1] + X[p2] + X[p3])/3.0;
	double dCy = (Y[p1] + Y[p2] + Y[p3])/3.0;

	cout << "p1=" << X[p1] << ", " << Y[p1] << " p2=" << X[p2] << ", " << Y[p2] << " p3=" << X[p3] << ", " << Y[p3];
	cout << "Center = " << dCx << ", " << dCy << endl;

	int iCx = dCx;
	int iCy = dCy;

	if (D_EQL(iCx, dCx) && D_EQL(iCy, dCy))
	{
		return true;		
	}

	return false;
}


int main (int argc, char **argv)
{
	ifstream input;
	input.open(argv[1]);
	ofstream output;
	output.open(argv[2]);

//	char zLine[100];
//	char *zTemp = NULL;		// used for tokenizing
//	input.getline(zLine, 100);
//	
//	int iCases = atoi(zLine);

	int iCases;
	input >> iCases;
	// variables

	

	for (int iCase = 1; iCase <= iCases; iCase++)
	{
		//	input.getline(zLine, 100);
		//	zTemp = strtok(zLine, " ");
	
		// n, A, B, C, D, x0, y0 and M
		input >> n;
		input >> A;
		input >> B;
		input >> C;
		input >> D;
		input >> _x00;
		input >> _y00;
		input >> M;

		X = new double[n];
		Y = new double[n];

		double dX = _x00;
		double dY = _y00;
		X[0] = dX;
		Y[0] = dY;
		for (int i = 1; i < n; i++)
		{
			dX = fmod((A * 1.0 * dX + B), M * 1.0);
			dY = fmod((C * 1.0 * dY + D), M * 1.0);
			X[i] = dX;
			Y[i] = dY;
		}

		int iTriangles = 0;
		for (int p1 = 0; p1 < n; p1++)
		{
			for (int p2 = p1 + 1; p2 < n; p2++)
			{
				for (int p3 = p2 + 1; p3 < n; p3++)
				{
					//if ((! ispequal(p1, p2)) && (!ispequal(p2, p3)) && (!ispequal(p3, p1)))
					//{
						if (iscntrdtrngl(p1, p2, p3))
						{
							iTriangles++;
						}
					//}
				}

			}
		}

		cout << "Case #" << iCase << ": " << iTriangles << endl;
		
		output << "Case #" << iCase << ": " << iTriangles << endl;

		delete [] X;
		delete [] Y;

	}
	
	exit(0);
}