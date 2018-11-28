#include <iostream>
using namespace std ;
int main(){
	int T ; cin >> T ;
	for(int t = 1 ; t <= T ; t++){
		int n ; cin >> n ;
		int wg[100] = {0}, tg[100] = {0}, match[100][100];
		long double wp[100], owp[100], oowp[100] ;
		for(int i = 0 ; i < n ; i++){
			char buf[105] ; cin >> buf ;
			for(int j = 0 ; j < n ; j++){
				if(buf[j] == '.') match[i][j] = 0 ;
				else if(buf[j] == '1') match[i][j] = 1, wg[i]++, tg[i]++ ;
				else match[i][j] = -1, tg[i]++ ;
			}
			wp[i] = (long double)wg[i] / tg[i] ;
		}
		
		for(int i = 0 ; i < n ; i++){
			long double ans = 0 ;
			for(int j = 0 ; j < n ; j++){
				if(match[i][j] != 0){
					ans += (long double)(wg[j] - ((match[i][j] == 1)?0:1)) / (tg[j] - 1) ;
//					cout << ans << ' ' ;
				}
			}
//			cout << endl ;
			owp[i] = ans / tg[i] ;
		}

		for(int i = 0 ; i < n ; i++){
			long double ans = 0 ;
			for(int j = 0 ; j < n ; j++){
				if(match[i][j] != 0){
					ans += owp[j] ;
				}
			}
			oowp[i] = ans / tg[i] ;
			//cout << wg[i] << ' ' << tg[i] << ' ' <<  wp[i] << ' ' << owp[i] << ' ' << oowp[i] << endl ;
		}
		cout << "Case #" << t << ":" << endl ;
		for(int i = 0 ; i < n ; i++)
			cout << 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i] << endl ;
	}
}
