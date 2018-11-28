#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

#define REP(a,b) for (int a=0; a<b; ++a)

char m[128][128], m2[128][128];

int main() 
{
	ifstream fin("c.in");
	ofstream fout("c.out");

	int tc, r;
	int c[1024][4];

	fin >> tc;

	REP(t,tc) {
		fin >> r;
		REP(i,r) {
			fin >> c[i][0] >> c[i][1] >> c[i][2] >> c[i][3];
			--c[i][0];--c[i][1];--c[i][2];--c[i][3];
		}

		int res = 0;
		memset(m, 0, sizeof(m));
		REP(i,r) {
			for (int y = c[i][1]; y <= c[i][3]; ++y)
				for (int x = c[i][0]; x <= c[i][2]; ++x)
					m[y][x] = 1;
		}

		while (true) {
			memset(m2, 0,  sizeof(m2));
			char found = 0;
			REP(y,100) REP(x,100) {
				if (m[y][x] == 1) {
					found = 1;
					if ((x > 0 && m[y][x-1]) || (y > 0 && m[y-1][x]))
						m2[y][x] = 1;
				} else {
					if (x > 0 && y > 0 && (m[y-1][x] && m[y][x-1]))
						m2[y][x] = 1;
				}
			}
			if (found == 0) break;
			++res;
			memcpy(m,m2,sizeof(m));
		}

		fout << "Case #" << t+1 << ": " << res << endl;
	}

	fout.close();

	return 0;
}