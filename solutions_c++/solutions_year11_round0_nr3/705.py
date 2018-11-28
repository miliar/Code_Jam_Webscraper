#include <cstdio>
#include <cstdlib>

void solve(){
	int N;
	scanf("%d",&N);
	int min = -1;
	int Ans = 0;
	int xsum = 0;
	for( int i = 0 ; i < N ; ++i ){
		int New ;
		scanf("%d",&New);
		Ans += New;
		if( min > New || min == -1 )
			min = New;
		xsum ^= New;
	}
	if( xsum == 0 ){
		Ans -= min;
		printf("%d\n",Ans);
	}else printf("NO\n");
}
int main(){
	freopen("Candy.in","r",stdin);
	freopen("Candy.out","w",stdout);
	int T;
	scanf("%d",&T);
	for( int i = 1 ; i <= T ; ++i ){
		printf("Case #%d: ",i);
		solve();
	}
}