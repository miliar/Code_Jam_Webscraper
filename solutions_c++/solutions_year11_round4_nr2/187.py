#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

typedef vector <string> vs;
typedef vector <int> vi;
#define REP(a,b) for(int a=0;a<(b);++a)
#define FOR(a,c,b) for(int a=c;a<(b);++a) 

char bb[500][501];
int b[500][501];
int r, c;

bool check(int k) {
	double wr, wc;
	double cr, cc;

	FOR(i,0,r-k+1) FOR(j,0,c-k+1) {
		wr = wc = 0;
		cr = (i+i+k-1)*0.5;
		cc = (j+j+k-1)*0.5;
		REP(ii,k) REP(jj,k) {
			wr += (i+ii-cr)*b[i+ii][j+jj];
			wc += (j+jj-cc)*b[i+ii][j+jj];
		}
		wr -= (i-cr)*b[i][j];
		wc -= (j-cc)*b[i][j];

		wr -= (i+k-1-cr)*b[i+k-1][j];
		wc -= (j-cc)*b[i+k-1][j];

		wr -= (i-cr)*b[i][j+k-1];
		wc -= (j+k-1-cc)*b[i][j+k-1];

		wr -= (i+k-1-cr)*b[i+k-1][j+k-1];
		wc -= (j+k-1-cc)*b[i+k-1][j+k-1];

		if (fabs(wr) < 1e-6 && fabs(wc) < 1e-6) return true;
	}	

	return false;
}

int main() 
{
	ifstream fin("b.in");
	ofstream fout("b.out");

	int tc;
	int d;
	int res;

	fin >> tc;

	REP(tcase,tc) {
		fin >> r >> c >> d;
		
		REP(i,r) fin >> bb[i];

		REP(i,r) REP(j,c) b[i][j] = bb[i][j] - '0';

		//check(5);
		for (res = min(r,c); res >= 3; --res) {
			if (check(res)) break;
		}

		fout << "Case #" << tcase+1 << ": ";
		if (res < 3) fout << "IMPOSSIBLE" << endl;
		else fout << res << endl;
		cout << tcase+1 << " / " << tc << endl;
	}

	fout.close();

	return 0;
}