#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <cmath>
#include <cstring>

#include <iomanip>
#include <iostream>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <list>
#include <deque>
#include <utility>
#include <queue>

#define fo(a,b,c) for( a = ( b ); a < ( c ); ++ a )
#define fr(a,b) fo( a, 0, ( b ) )
#define fi(a) fr( i, ( a ) )
#define fj(a) fr( j, ( a ) )
#define fk(a) fr( k, ( a ) )
#define mp make_pair
#define pb push_back
#define all(v) (v).begin( ), (v).end( )
#define _(a,b) memset( a, b, sizeof( a ) )

#define MAXTAM 110
#define WIN 0
#define PLAY 1

using namespace std;

int main(){
	ios_base::sync_with_stdio(false);
	
	int test, t=1, n, i, j, aux;
	char line[MAXTAM][MAXTAM];
	double info[MAXTAM][2], wp[MAXTAM], owp[MAXTAM], oowp[MAXTAM];
	double sumWP, sumOWP;
	
	_(info, 0);
	_(wp, 0);
	_(owp, 0);
	
	cin >> test;
	while (test--){
		cin >> n;
		
		fi(n){
			fj(n){
				cin >> line[i][j];
				if (line[i][j] == '1'){
					info[i][WIN]++;
					info[i][PLAY]++;
				}
				else if (line[i][j] == '0'){
					info[i][PLAY]++;
				}
			}
			wp[i] = info[i][WIN] / info[i][PLAY];
			//cout << "DBG: " << i << " tem wp: " << wp[i] << endl;
		}
		
		fi(n){
			sumWP = 0.0;
			aux = 0;
			fj(n){
				// linha oponente, coluna eu
				// tirando jogo que ele teve contra mim
				if (line[j][i] == '1'){
					sumWP += (info[j][WIN] - 1) / (info[j][PLAY] -1);
					//cout << j << " venceu " << i << " entao sumWP: " << sumWP << endl;
					aux++;
				}
				else if (line[j][i] == '0'){
					sumWP += info[j][WIN] / (info[j][PLAY] - 1);
					//cout << j << " NAO venceu " << i << " entao sumWP: " << sumWP << endl;
					aux++;
				}
			}
			owp[i] = sumWP / aux;
			//cout << "DBG: " << i << " tem owp: " << owp[i] << endl;
		}
		fi(n){
			sumOWP = 0.0;
			aux = 0;
			fj(n){
				if (line[j][i] != '.'){
					sumOWP += owp[j];
					//cout << j << " jogou com " << i << " entao sumOWP: " << sumOWP << endl;
					aux++;
				}
			}
			oowp[i] = sumOWP / aux;
			//cout << "DBG: " << i << " tem oowp: " << oowp[i] << endl;
		}
		
		cout << "Case #" << t++ << ":\n";
		fi(n){
			//printf("DBG: team %d - wp: %llf owp: %llf oowp: %llf - total: %.11lf\n", i, 0.25*wp[i], 0.5*owp[i], 0.25*oowp[i], 0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
			//printf("%.11llf\n", 0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
			cout << fixed << setprecision(11) << (0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]) << "\n";
		}
		
		fi(n){
			info[i][PLAY] = info[i][WIN] = 0.0;
			wp[i] = owp[i] = oowp[i] = 0.0;
		}
	}
	
	return 0;
}