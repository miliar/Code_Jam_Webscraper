#include<iostream>
#include<algorithm>
#include<map>
using namespace std;

typedef long long ll;


#define maxn 100
int f[maxn], n;

int str[maxn], len;

bool check( ll x, int base ) {
	map< ll, int > hd;
	hd[x] = 1;
	while( x != 1 ) {
		len = 0;
		while( x ) {
			str[ len ++ ] = x % base;
			x /= base;
		}

		x = 0;
		for( int i = 0; i < len; i ++ )
			x += (ll) str[i] * str[i];
		if( hd[x] == 1 ) break;
		hd[x] = 1;
	} 

	return x == 1;
}


int main() {
	int T;
	//freopen("D:\\in.in","r",stdin);
	//freopen("D:\\out.out","w",stdout);
	int ca = 0;
	scanf("%d\n", &T);
	while( T -- ) {
		int x;
		char c;
		n = 0;
		while( scanf("%d%c",&x,&c) != EOF ) {
			f[n ++ ] = x;
			if( c == '\n' ) break;
		}
		for( ll i = 2;  ; i++) {
			bool flag = 1;

			for( int j = 0; j < n && flag; j ++ ) {
				if( check(i, f[j]) == 0 )
					flag = 0;
			}
			if( flag ) {
				printf("Case #%d: %d\n",++ca, i);
				break;
			}

		}
	}
	return 0;
}