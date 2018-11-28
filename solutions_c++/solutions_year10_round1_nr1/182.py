#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

#define REP(a,b) for (int a=0; a<b; ++a)

const int dx[] = {1, 1, 1, 0};
const int dy[] = {1, 0, -1, 1};

int main() 
{
	ifstream fin("a.in");
	ofstream fout("a.out");

	int tc, n, k;
	char b[64][64], R[64][64];

	fin >> tc;

	REP(t,tc) {
		fin >> n >> k;
		REP(i,n) fin >> b[i];

		memset(R, '.', sizeof(R));
		REP(i,n) {
			int pos = 0;
			for (int j = n-1; j >=0; --j) {
				if (b[i][j] != '.') R[pos++][i] = b[i][j];
			}
		}

		REP(i,n) {
			R[i][n] = 0;
			cout << R[i] << endl;
		}
		cout << endl;

		bool hasr = false, hasb = false;
		char pl;
		int cnt, r, c;

		REP(i,n) REP(j,n) if (R[i][j] != '.') {
			pl = R[i][j]; 
			REP(d,4) {
				cnt = 0; r = i; c = j;
				while (r >= 0 && c >= 0 && r < n && j < n && R[r][c] == pl) {
					++cnt;
					r += dx[d];
					c += dy[d];
				}
				if (cnt >= k) {
					if (pl == 'B') hasb = true;
					else hasr = true;
				}
			}
		}

		fout << "Case #" << t+1 << ": ";

		if (hasr && hasb) fout << "Both" << endl;
		if (hasr && !hasb) fout << "Red" << endl;
		if (!hasr && hasb) fout << "Blue" << endl;
		if (!hasr && !hasb) fout << "Neither" << endl;


	}

	fout.close();

	return 0;
}