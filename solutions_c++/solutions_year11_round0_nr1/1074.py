#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

#define REP(a,b) for (int a=0; a<b; ++a)


int main() 
{
	ifstream fin("a.in");
	ofstream fout("a.out");

	int tc, n;
	int posA, posB, t, lastA, lastB;
	string s;
	int pos, dst;

	fin >> tc;

	REP(tst,tc) {
		fin >> n;

		posA = posB = 0;
		lastA = lastB = 0; t = 0;
		REP(i,n) {
			fin >> s >> pos;
			--pos;
			if (s[0] == 'O') {
				dst = abs(posA-pos);
				if (dst > t-lastA) t = lastA+dst;
				lastA = ++t;		// push
				posA = pos;
			} else {
				dst = abs(posB-pos);
				if (dst > t-lastB) t = lastB+dst;
				lastB = ++t;		// push
				posB = pos;
			}
		}

		fout << "Case #" << tst+1 << ": " << t << endl;
	}

	fout.close();

	return 0;
}