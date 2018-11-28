// Hexagon.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef vector<LL> VL;
#define FORE(it, c, T) for(T::iterator it = c.begin(); it != c.end(); it++)
#define FORI(i, n) for(int i = 0; i < (n); i++)
#define FORIS(i, s, n) for(int i = (s); i < (n); i++)
#define CLEAR(a, n) memset(a, n, sizeof(a))
#define PB(n) push_back(n)
#define SZ(c) int((c).size())
#define ALL(c) (c).begin(), (c).end()

#define NUM 101

int T, N;

int main(int argc, char* argv[])
{
#define TASK_NAME(file) "C"file
#define FOLDER(file) "c:\\Projects\\coding\\cj\\2011\\QualificationRound\\"TASK_NAME("")"\\"file
//	ifstream in(FOLDER(TASK_NAME("-test.in")));
//	ofstream out(FOLDER(TASK_NAME("-test.out")));
//	ifstream in(FOLDER(TASK_NAME("-small-attempt0.in")));
//	ofstream out(FOLDER(TASK_NAME("-small-attempt0.out")));
	ifstream in(FOLDER(TASK_NAME("-large.in")));
	ofstream out(FOLDER(TASK_NAME("-large.out")));

	in >> T;
	FORI(ncase, T) {
		in >> N;
		int xr = 0;
		int mn = 1000000000;
		int sm = 0;
		FORI(i, N) {
			int a;
			in >> a;
			xr ^= a;
			mn = min(mn, a);
			sm += a;
		}
		if(xr)
			out << "Case #" << (ncase+1) << ": " << "NO" << endl;
		else 
			out << "Case #" << (ncase+1) << ": " << (sm-mn) << endl;
	}
	return 0;
}
