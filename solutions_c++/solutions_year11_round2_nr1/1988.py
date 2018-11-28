#include <iostream>
#include <cstdio>
using namespace std;

#define FOR(i, M) for( int i = 0; i < (M); ++i )

int main(){
    int T;
    cin >> T;
    for( int t = 1; t <= T; ++t ){
    	int N;
    	cin >> N;
    	
    	int wg[N];
		double wp[N];
    	int played[N][N];
    	int nplayed[N];
    	
    	char c;
    	FOR(i, N){
			wg[i] = 0;
			nplayed[i] = 0;
			FOR(j, N){
				cin >> c;
				if(c!='.'){
					++nplayed[i];
					if(c=='1'){
						++wg[i];
						played[i][j] = 1;
					}
					else{
						played[i][j] = -1;
					}
				}
				else {
					played[i][j] = 0;
				}
			}
			wp[i] = (double)wg[i]/nplayed[i];
		}
    
    	double owp[N];
    	FOR(i, N){
			owp[i] = 0;
			FOR(j, N){
				if(played[i][j]){
					owp[i] += (double)(wg[j]-(played[j][i] == 1))/(nplayed[j]-1);
				}
			}
			owp[i] /= nplayed[i];
		}
		
		double oowp[N];
    	FOR(i, N){
			oowp[i] = 0;
			FOR(j, N){
				if(played[i][j]){
					oowp[i] += owp[j];
				}
			}
			oowp[i] /= nplayed[i];
		}
    
        printf("Case #%d:\n", t);
		FOR(i, N){
			printf("%.12f\n", 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]);
			//printf("wp: %f, owp: %f, oowp: %f\n", wp[i], owp[i], oowp[i]);
		}
    }
}
