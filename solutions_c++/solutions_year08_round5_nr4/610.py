#include <iostream>
#include <vector>
using namespace std ;
long long dp(long long m[][100] ,long long r[][100], long long x , long long y){
	if(m[x][y] != -1) return m[x][y] ;
	if(r[x][y] == 1) return 0 ;
	long long ans = 0 ;
	if(x>=1 && y >=2 ) ans += dp(m,r,x-1,y-2) ;
	if(x>=2 && y >= 1) ans += dp(m,r,x-2,y-1) ;
//	cout << x << ' ' << y << ' ' << ans << endl  ;
	return m[x][y] = ans ;
}
int main(){
	long long t ;
	cin >> t ;
	for(long long tc = 1 ; tc <= t ; tc++){
		long long h , w , R ;
		long long m[100][100] = {0} ;
		cin >> h >> w >> R ;
		for(long long i = 0 ; i < h ; i++){
			for(long long j = 0 ; j < w ; j++){
				m[i][j] = -1 ;
			}
		}
		m[0][0] = 1 ;
		long long r[100][100] = {0} ;
		for(long long j = 0 ; j <R ; j++){
			long long x , y ;
			cin >> x >> y ;
			r[x-1][y-1] =1 ;
		}
		long long ans = dp(m,r,h-1,w-1) ;
		cout << "Case #" << tc << ": " ;
		cout << ans  % 10007<< endl ;
	}
}
