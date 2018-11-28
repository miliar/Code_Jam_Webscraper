#include <iostream>
#include <cstring>

using namespace std;

int T;
int R,K,N;
long long g[ 1005 ];
long long gain[ 1005 ];
int timeAp[ 1005 ];
bool seen[ 1005 ];

int main(){	
	cin >> T;
	
	for (int tt=1; tt<=T; tt++){
		cin >> R >> K >> N;
		
		long long suma = 0;
		
		for (int i=0; i<N; i++){
			cin >> g[i];
			suma += g[i];
		}
		
		long long ans = 0;
		
		if ( suma <= K ){
			ans = suma * R;
			cout << "Case #" << tt << ": " << ans << endl;
			continue;
		}
		
		memset( seen, 0, sizeof seen );
		
		int now = 0;
		int sz = 0;
		while ( !seen[ now ] ){
			seen[ now ] = true;
			timeAp[ now ] = sz;
			long long cont = 0;
			int j = now;
			while ( true ){
				cont += g[j];
				if ( cont > K ) break;
				j++;
				if ( j == N ) j = 0;
			}
			gain[ sz++ ] = cont - g[j];
			now = j;
		}
		
		int j=0;
		
		while (j<timeAp[now] && R>0){
			ans += gain[j];
			j++;
			R--;
		}
		
		long long W = sz - timeAp[now];
		long long c1 = R / W;
		long long c2 = R % W;
		
		for (int i=timeAp[now]; i<sz; i++) ans += gain[i] * c1;
		int i=timeAp[now];
		while ( c2-- ){
			ans += gain[i];
			i++;
		}
		
		cout << "Case #" << tt << ": " << ans << endl;
	}
	
	return 0;
}
