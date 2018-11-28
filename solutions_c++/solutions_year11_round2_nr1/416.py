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

	char b[101][101];
	double wp[100], owp[100], oowp[100];
	int np[100], nw[100];

	int tc, n, cnt, cntw, m;

	fin >> tc;

	REP(t,tc) {
		fin >> n;

		REP (i,n) {
			cnt = cntw = 0;
			fin >> b[i];
			REP(j,n) if (b[i][j] != '.') {
				++cnt;
				if (b[i][j] == '1') ++cntw;
			}
			np[i] = cnt; nw[i] = cntw;
			wp[i] = cntw/(double)cnt;
		}

		REP(i,n) {
			double sum = 0;
			cnt = 0;
			REP(j,n) if (j!=i && b[i][j] != '.') {
				sum += (b[j][i] == '1' ? nw[j]-1 : nw[j])/(double)(np[j]-1);
				++cnt;
			}
			owp[i] = sum/cnt;
		}

		REP(i,n) {
			double sum = 0;
			cnt = 0;
			REP(j,n) if (j!=i && b[i][j] != '.') {
				sum += owp[j];
				++cnt;
			}
			oowp[i] = sum/cnt;
		}

		double res;

		fout << "Case #" << t+1 << ":" << endl;

		REP(i,n) {
			res = 0.25*wp[i]+0.5*owp[i]+0.25*oowp[i];
			fout.precision(14);
			fout << res << endl;
		}
	}

	fout.close();

	return 0;
}