#include<iostream>
using namespace std;

#define maxn 100
typedef long long ll;
int sw[255];
char str[maxn];

int hash[maxn];

int Find() {
	for( int i = 0; ; i ++ ) {
		if( hash[i] == -1 ) {
			hash[i] = 1;
			return i;
		}
	}
	return -1;
}

int main() {
	freopen("C:\\in.in","r", stdin);
	freopen("C:\\out.out","w", stdout);
	int T;
	int ca = 0;
	scanf("%d", &T);
	while( T -- ) {
		memset( sw, -1, sizeof(sw) );
		memset( hash, -1, sizeof(hash) );

		scanf("%s", str);
		int len = strlen( str );
		sw[ str[0] ] = 1;
		hash[1] = 1;
		for( int i = 1; i < len; i ++ ) {
			int x = str[i];
			if( sw[x] != -1 ) continue;
			int k = Find();
			sw[x] = k; 
		}
		int end = 0;
		for( int i = 99; i >= 0; i -- ) {
			if( hash[i] != -1 ) {
				end = i;
				break;
			}
		}
		end ++;
		ll res = 1;
		ll ans = 0;
		for( int i = 0; i < len; i ++ ) {
			ans = ans * end + sw[ str[i] ];
		}
		printf("Case #%d: %lld\n", ++ ca, ans);
	}
	return 0;
}