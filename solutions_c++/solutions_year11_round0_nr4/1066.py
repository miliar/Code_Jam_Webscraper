#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

#define REP(a,b) for (int a=0; a<b; ++a)


int main() 
{
	ifstream fin("d.in");
	ofstream fout("d.out");

	int tc, n, cnt, m;

	fin >> tc;

	REP(t,tc) {
		cnt = 0;

		fin >> n;

		REP (i,n) {
			fin >> m;
			if (m != i+1) ++cnt;
		}


		fout << "Case #" << t+1 << ": " << cnt << endl;
	}

	fout.close();

	return 0;
}