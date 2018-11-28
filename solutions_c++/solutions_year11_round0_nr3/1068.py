#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

#define REP(a,b) for (int a=0; a<b; ++a)

int main() 
{
	ifstream fin("c.in");
	ofstream fout("c.out");

	int tc, n, mn, x, s, m;

	fin >> tc;

	REP(t,tc) {
		fin >> n;

		x = 0; s = 0; mn = 1<<30;
		REP(i,n) {
			fin >> m;
			if (m < mn) mn = m;
			s += m;
			x = x^m;
		}


		fout << "Case #" << t+1 << ": ";
		if (x != 0) fout << "NO" << endl;
		else fout << s - mn << endl;
	}

	fout.close();

	return 0;
}