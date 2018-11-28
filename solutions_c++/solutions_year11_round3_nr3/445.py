#include <cstdio>

const int MaxN = 102;

int N , L , H;
int f[MaxN];

void solve(){
	scanf("%d%d%d",&N,&L,&H);
	for( int i = 0 ; i < N ; ++i )
		scanf("%d",&f[i]);
	
	for( int i = L ; i <= H ; ++i ){
		bool ok = true;
		for( int j = 0 ; j < N ; ++j ){
			if( f[j] % i != 0 && i % f[j] != 0 ){
				ok = false;
				break;
			}
		}
		if( ok ){
			printf("%d\n",i);
			return;
		}
	}
	printf("NO\n");
}
int main(){
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	int T;
	scanf("%d",&T);
	for( int i = 1 ; i <= T ; ++i ){
		printf("Case #%d: ",i);
		solve();
	}
}