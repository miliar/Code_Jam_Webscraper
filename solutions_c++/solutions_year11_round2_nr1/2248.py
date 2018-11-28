#include<iostream>
using namespace std;
#include<algorithm>
#include<queue>
#include<stack>
#include<functional>
#include<string>
#include<sstream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<math.h>
#include<vector>
#include<deque>
#include<list>
#include<set>
#include<map>

char table[150][150];
double WP[150];
double OWP[150];
double OOWP[150];
double calc[150];

int main() {
	//freopen("input.txt","rt",stdin);
	//freopen("o.txt","wt",stdout);
	int T;
	cin >> T;
	++T;
	int N;
	int kase = 0;
	while( -- T ) {
		cin >> N;
		for(int i = 0 ; i < N; ++i)
			for(int j = 0 ; j < N ; ++j) {
				cin >> table[i][j];
			}

			for(int i = 0 ; i < N ; ++i) {
				int wins = 0, loses = 0;
				for(int j = 0 ; j < N ; ++j) {
					wins += (table[i][j] == '1');
					loses += (table[i][j] == '0'||table[i][j]=='1');
				}
				WP[i] = (wins*1.0)/loses;
			}
			for(int k = 0 ; k < N ; ++k) {
				double sum = 0.;
				int cnt = 0;
				for(int i = 0 ; i < N ; ++i) {
					if( k == i || table[i][k] == '.' )
						continue;
					++cnt;
					int wins = 0, loses = 0;
					for(int j = 0 ; j < N ; ++j) {
						if( k == j )
							continue;
						wins += (table[i][j] == '1');
						loses += (table[i][j] == '0'||table[i][j]=='1');
					}
					sum  += (wins*1.0)/loses;
				}
				OWP[k] = (sum/(cnt));

			}
			for(int k = 0 ; k < N ; ++k) {
				double sum = 0.;
				int cnt = 0;
				for(int i = 0 ; i < N ; ++i) {
					if( k == i || table[i][k] == '.' )
						continue;
					++cnt;
					sum += OWP[i];
				}
				OOWP[k] = sum / cnt;
			}
			// RPI = 0.25 * WP + 0.50 * OWP + 0.25 * OOWP

			printf("Case #%d:\n", ++kase);
			for(int i = 0 ; i < N ; ++i) {
				cout << fixed << 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i] << endl;
			}
	}
	return 0;
}