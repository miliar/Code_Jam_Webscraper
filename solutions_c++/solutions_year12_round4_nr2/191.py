/*{{{*/
/*includes e defines*/
#include <iostream>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <sstream>
using namespace std;
typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<int,int> PII;
#define sz(A) (int)(A).size()
#define FOR(A,B) for(int A=0; A < (int) (B);A++)
#define FOREACH(A,B) for((__typeof (B).begin) A = (B).begin(); A != (B).end(); A++)
#define pb push_back
#define all(x) x.begin() , x.end()
#define mp make_pair
/*}}}*/
/*{{{*/
/*main*/
void solveCase();
int main() {
	int TESTES; scanf("%d", &TESTES);
	for(int TESTE = 1; TESTE <= TESTES; TESTE++) {
		printf("Case #%d: ", TESTE);
		solveCase();
	}
    return 0;
}
/*}}}*/

void solveCase() {
	int n;
	int W, L;
	cin >> n >> W >> L;
	vector< pair<double,int> > r(n);
	FOR(i,n) { cin >> r[i].first; r[i].second = i; }
	
	vector< pair<double,double> > ans(n);

	int erro = 1, cnt = 0;

	while(erro) {
		erro = 0;
		if(cnt == 1) sort(all(r));
		else if(cnt == 2) { sort(all(r)); reverse(all(r)); }
		else if(cnt > 2) random_shuffle( all(r) );
		cnt++;

		if(cnt >= 50) {
			cerr << "Zuou" << endl;
			break;
		}

		FOR(i, sz(r)) {
			double atx;
			if(i == 0) {
				atx = 0;
			} else {
				atx = ans[ r[i-1].second ].first + r[i-1].first + r[i].first + 1e-9;
			}
			if(atx > W) {
				atx = 0;
			}
			double aty = 0;
			for(int j = 0; j < i; j++) {
				double dx = ans[ r[j].second ].first - atx;
				double dy = ans[ r[j].second ].second - aty;
				double rr = r[i].first + r[j].first;
				if(dx*dx + dy*dy <= rr*rr) { 
					aty = ans[ r[j].second ].second + r[j].first + r[i].first + 1e-9; 
				}
			}

			if(atx > W || aty > L) {
				cerr << "ERRO" << endl;
				erro = 1;
			}

			ans[ r[i].second ] = mp(atx, aty);
		}


		FOR(i, n) {
			FOR(j, n) {
				if(i == j) continue;
				double rr = r[i].first + r[j].first;
				double dx = ans[ r[i].second ].first - ans[ r[j].second ].first;
				double dy = ans[ r[i].second ].second - ans[ r[j].second ].second;
				if(dx * dx + dy*dy < rr * rr ) {
					if(!erro) {
						cerr << " >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Erro doidodao"  << endl;					
						cerr << dx * dx + dy* dy - rr*rr << endl;
						erro = 1;
					} else {
//						cerr << "JA ERA ERRO MESMO" << endl;
					}
				}
			}
		}

	}

	if(erro) cerr << "FERROU <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< " << endl;

//	cerr << W << " " << L << endl;
	FOR(i,n) {
		printf("%f %f ", ans[i].first, ans[i].second);
//		cout << ans[i].first << " " << ans[i].second << " ";
	}
	cout << endl;

}

