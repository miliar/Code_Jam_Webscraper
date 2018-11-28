// Goog-R1C-A
// Chupilko

#include <iostream>	
#include <string>
#include <fstream>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

#define FILE_IN		 "A-small-attempt0.in"
#define FILE_OUT	 "A-small.out"

#define REP(i,n) for(i=0;i<(n);i++)
#define FOR(i,a,b) for(i=(a);i<=(b);i++)
#define SZ size()
#define SIZE(a) ((int)a.SZ)
#define MAX(a,b) ((a)>(b)?(a):(b))

typedef vector<int> VI;


void answerQuestion(istream& in, ostream& out)
{
	int P, K, L, i, sm = 0;
	VI f;
	in >> P >> K >> L;
	if(P*K<L) out << "Impossible";
	f.resize(L);
	for(int i=0;i<L;i++) in >> f[i];
	sort(f.begin(), f.end());
	int j = 0;
	for(int i=L-1;i>=0;j++,i--) 
	{
		sm += f[i]*(1+(j/K));
	};
	out << " " << sm;
//	out << " " << i;
};

void answerQuestions(istream& in, ostream& out)
{
	int n, i;
	in >> n;
	FOR(i,1,n) {
		out << "Case #" << i << ":";
		answerQuestion(in, out);
		out << endl;
	}
};

int main(int argc, char* argv[])
{
	if(argc>3) {
		cerr << "Usage: <Input file> <Output file>" << endl;
		return EXIT_FAILURE;
	}
	char f_in[256], f_out[256];

	if (argc<3){strcpy_s(f_out,FILE_OUT);}else{strcpy_s(f_out,argv[2]);};
	if (argc<2){strcpy_s(f_in,FILE_IN);}else{strcpy_s(f_in,argv[1]);};

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
};
