#include <cstdio>
#include <cstring>
#include <algorithm>
#include <string>
#include <set>
#include <map>
using namespace std;
int TT;
#define two(n) (1<<(n))
int perder[1024];
int precos[1024][1024];
int P;
//rodada,jogo,assistidos
long long PD[10+10][1024+10][10+10];
long long int calc(int rodada,int jogo, int assistidos) {
	long long int &ans=PD[rodada][jogo][assistidos];
	if(ans!=-1)
		return ans;

	if(rodada==0) {
		if(assistidos<perder[jogo])
			return 1000000000ll;
		return 0;
	}

	//entre asssistir e nao assistir
	ans=min( calc(rodada-1,jogo*2,assistidos+1) + calc(rodada-1,jogo*2+1,assistidos+1) + precos[rodada-1][jogo] , calc(rodada-1,jogo*2,assistidos) + calc(rodada-1,jogo*2+1,assistidos) );
	return ans;
}

int main(void) {
	scanf("%d",&TT);
	for(int T=1;T<=TT;T++) {
		printf("Case #%d: ",T);
		scanf("%d",&P);
		for(int i=0;i<two(P);i++) {
			scanf("%d",perder+i);
			perder[i]=P-perder[i];
		}
		for(int i=0;i<P;i++) {
			for(int j=0;j<two(P-i-1);j++)
				scanf("%d",&precos[i][j]);
		}
		memset(PD,-1,sizeof(PD));
		long long int ans=calc(P,0,0);
		printf("%lld\n",ans);
	}
	return 0;
}
