#include <cstdio>
#include <cstdlib>

const int MaxN = 120;

int N,T;

int Max(int a , int b){
	if( a > b ) return a;
	return b;
}
void solve(){
	scanf("%d",&N);
	int TO = 0 , TB = 0;
	int PO = 1 , PB = 1;
	for( int i = 0 ; i < N ; ++i ){
		char color[3];
		int p;
		scanf("%s%d",color,&p);
		if( color[0] == 'O' ){
			int T = abs(p-PO);
			PO = p;
			TO = Max( TO + T , TB ) + 1;
		}else if( color[0] == 'B' ){
			int T = abs(p-PB);
			PB = p;
			TB = Max( TB + T , TO ) + 1;
		}
	}
	printf("%d\n",Max(TB,TO));
}
int main(){
	freopen("bot.in","r",stdin);
	freopen("bot.out","w",stdout);
	scanf("%d",&T);
	for( int i = 1 ; i <= T ; ++i ){
		printf("Case #%d: ",i);
		solve();
	}
}