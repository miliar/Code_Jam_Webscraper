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

int T, C, D, N;
typedef map<string, char> MS;
MS combs;
typedef set<string> SS;
SS oppos;

int main(int argc, char* argv[])
{
#define TASK_NAME(file) "B"file
#define FOLDER(file) "c:\\Projects\\coding\\cj\\2011\\QualificationRound\\"TASK_NAME("")"\\"file
//	ifstream in(FOLDER(TASK_NAME("-test.in")));
//	ofstream out(FOLDER(TASK_NAME("-test.out")));
//	ifstream in(FOLDER(TASK_NAME("-small-attempt0.in")));
//	ofstream out(FOLDER(TASK_NAME("-small-attempt0.out")));
	ifstream in(FOLDER(TASK_NAME("-large.in")));
	ofstream out(FOLDER(TASK_NAME("-large.out")));

	in >> T;
	FORI(ncase, T) {
		in >> C;
		combs.clear();
		FORI(i, C) {
			string c;
			in >> c;
			if(SZ(c) != 3) throw 1;
			combs[string(1, c[0])+c[1]] = c[2];
			combs[string(1, c[1])+c[0]] = c[2];
		}
		in >> D;
		oppos.clear();
		FORI(i, D) {
			string c;
			in >> c;
			if(SZ(c) != 2) throw 1;
			oppos.insert(string(1, c[0])+c[1]);
			oppos.insert(string(1, c[1])+c[0]);
		}
		in >> N;
		string txt;
		in >> txt;
		if(SZ(txt) != N) throw 1;

		string res;
		FORI(i, N) {
			if(SZ(res) > 0) {
				string c = string(1, res[SZ(res)-1]) + txt[i];
				if(combs.count(c) > 0) {
					res[SZ(res)-1] = combs[c];
					continue;
				}
			}
			res += txt[i];
			FORI(j, SZ(res)-1) {
				string c = string(1, res[j]) + txt[i];
				if(oppos.count(c) > 0) {
					res = "";
					break;
				}
			}
		}

		out << "Case #" << (ncase+1) << ": [";
		if(SZ(res) > 0)
			out << res[0];
		FORIS(i, 1, SZ(res))
			out << ", " << res[i];
		out << "]" << endl;
	}
	return 0;
}
