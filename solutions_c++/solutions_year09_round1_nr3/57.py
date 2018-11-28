#include <iostream>
#include <sstream>
#include <cstring>
#include <cstdio>
#include <cassert>
#include <vector>
#include <queue>
using namespace std;

vector<vector<int> > words;
#define fu(i,m,n) for(int i=m; i<n; i++)
typedef long long i64;

double binom[100][100];

int main(void) {
	int T;
	cin >> T;


	fu(n,0,50) binom[n][0]=1;
	fu(m,1,50) fu(n,1,50) binom[m][n]=binom[m-1][n]+binom[m-1][n-1];

	/*fu(i,0,10) {
		fu(j,0,10) cout << binom[i][j] << " ";
		cout << endl;
	}*/

	fu(t,0,T) {
		int N,C;
		cin >> C >> N;
		double prob[C+1];
		fu(c,1,C+1) prob[c]=0;
		prob[0]=1;
		double tprop=0;
		double expn=0;
		//if(t==0) continue;
		fu(tr,1,30000) {
			//fu(c,0,C+1) cout << prob[c] << " "; cout << endl;
			for(int c=C; c>=1; c--) {
				//if(binom[C][N]==0) cout << C << " " << N << endl;
				double p = prob[c] * binom[c][N]/binom[C][N];
				for(int c2=max(0,c-N); c2<c; c2++) {
					p += prob[c2] * binom[C-c2][c-c2] * binom[c2][N-(c-c2)] / binom[C][N];//binom[c2][N-(c-c2)]/binom[C][N] * binom[C-c2][N];
				}
				prob[c]=p;
			}
			prob[0]=0;
			tprop+=prob[C];
			expn += tr*prob[C];
			prob[C]=0;
		}
		//cout << tprop << " " << expn << endl;
		printf("Case #%d: %.7lf\n", t+1, expn, tprop);
	}
}
