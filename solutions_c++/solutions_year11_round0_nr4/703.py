#include <stdio.h>
#include <cstring>

const int MaxN = 1002;

int Ai[MaxN];
bool f[MaxN];
int Step,N;

void DFS( int i ){
	Step ++;
	f[i] = true;
	if( !f[Ai[i]] ) DFS( Ai[i] ); 
}
void solve(){
	double Ans = 0;
	scanf("%d",&N);
	memset(f,false,sizeof(f));
	for( int i = 1 ; i <= N ; ++i ){
		scanf("%d",&Ai[i]);
	}
	for( int i = 1 ; i <= N ; ++i )
		if( !f[i] ){
			Step = 0;
			DFS( i );
			if( Step > 1 ) Ans +=  Step;
		}
	printf("%.6f\n",Ans);
}
int main(int argc, char *argv[])
{
	freopen("Goro.in","r",stdin);
	freopen("Goro.out","w",stdout);
	int T;
	scanf("%d",&T);
	for( int i = 1 ; i <= T ; ++i ){
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}
