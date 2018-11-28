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
#define NUM 55




#define FOLDER(file) "c:\\Projects\\coding\\cj\\2010\\QualificationRound\\A\\"file

int main(int argc, char* argv[])
{

//	ifstream in(FOLDER("A-test-practice.in"));
//	ofstream out(FOLDER("A-test-practice.out"));
//	ifstream in(FOLDER("A-small-practice.in"));
//	ofstream out(FOLDER("A-small-practice.out"));
	ifstream in(FOLDER("A-large-practice.in"));
	ofstream out(FOLDER("A-large-practice.out"));

	int N, K, T;
	in >> T;
	FORI(ncase, T) {
		in >> N >> K;
		int res = (((1<<N)-1) & K) == ((1<<N)-1);
		out << "Case #" << (ncase+1) << ": " << (res?"ON":"OFF") << endl;
	}
	return 0;
}
