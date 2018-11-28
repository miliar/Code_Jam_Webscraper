// 
//	Alexandr Chupilko, 2008
//	
//	Train Shedule
//

#include <iostream>	
#include <string>
#include <sstream>
#include <fstream>
#include <map>

using namespace std;

typedef map<int, int> tTrainShedule;

inline int convertCcToInt(const int x1, const int x2)
{
   return (x1 - 48) * 10 + x2 - 48;
} 

inline int understandTime(string& t)
{
	return (convertCcToInt(t[0], t[1])) * 60 + convertCcToInt(t[3], t[4]);
}

void readShedule(istream& in, tTrainShedule& ts_out, tTrainShedule& ts_in, int turnAround, int q)
{
	string tmp1, tmp2;
	for (int i = 1; i <= q; i++)
	{
		in >> tmp1;
		ts_out[understandTime(tmp1)]--;
		in >> tmp2;
		ts_in[understandTime(tmp2) + turnAround]++;
	}
}

int calcInitialTrains(tTrainShedule& ts)
{
	int acc = 0, result = 0;
	for(tTrainShedule::iterator p = ts.begin(); p != ts.end(); ++p)
	{
		acc += (*p).second;
		result = min(result, acc);
	}
	return -result;
}

void answerQuestions(istream& in, ostream& out)
{
	size_t n;
	int turnAround, qA, qB;
	tTrainShedule tsA, tsB;
	in >> n;
	for(size_t i = 1; i <= n; i++)
	{
		tsA.clear();
		tsB.clear();
		in >> turnAround >> qA >> qB;
		readShedule(in, tsA, tsB, turnAround, qA);
		readShedule(in, tsB, tsA, turnAround, qB);
		out << "Case #" << i << ": " << calcInitialTrains(tsA) << " " << calcInitialTrains(tsB) << endl;
	}
}

int main(int argc, char* argv[])
{
	if(argc>3) {
		cerr << "Usage: <Input file> <Output file>" << endl;
		return EXIT_FAILURE;
	}
	char f_in[256], f_out[256];

	if (argc<3){strcpy_s(f_out,"B-large.out");}else{strcpy_s(f_out,argv[2]);};
	if (argc<2){strcpy_s(f_in,"B-large.in");}else{strcpy_s(f_in,argv[1]);};

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

