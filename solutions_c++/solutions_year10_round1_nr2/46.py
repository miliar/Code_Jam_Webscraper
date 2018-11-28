#include <cstdio>
#include <algorithm>
#include <cstring>
#include <iostream>
using namespace std;
const int maxn=110;

int D, I, M, n, task, T=0;
int a[maxn], f[maxn][300];

int main(){
	freopen("B-large.in","r",stdin);
	freopen("a.out","w",stdout);
	for (scanf("%d", &task); task--;){
		scanf("%d%d%d%d", &D, &I, &M, &n);
		for (int i=1; i<=n; i++) scanf("%d", a+i);

		int ret = 1000000000;
		for (int j=0; j<=255; j++)
			f[0][j] = 0;

		for (int i=1; i<=n; i++){
			for (int j=0; j<=255; j++){
				f[i][j] = f[i-1][j]+D;
				for (int k=0; k<=255; k++)
				if ( abs( j-k )<=M ){
					f[i][j] = min( f[i][j], f[i-1][k]+abs( a[i]-j ) );
				}
			}

			bool fnsh;
			do{
				fnsh = true;
				for (int j=0; j<=255; j++)
				for (int k=max(0, j-M); k<=min( 255, j+M ); k++)
				if ( f[i][k] > f[i][j]+I ){
					f[i][k] = f[i][j]+I;
					fnsh = false;
				}
			}while ( !fnsh );
		}

		for (int j=0; j<=255; j++)
			ret = min( ret, f[n][j] );
		printf("Case #%d: %d\n", ++T, ret);
	}
	return 0;
}
