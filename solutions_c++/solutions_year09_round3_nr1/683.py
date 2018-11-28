#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>
#include <set>
#include <map>
#include <cmath>
#include <cstdlib>
typedef long long LL;
using namespace std;

char str[100];
bool tg[256];
int val[256];
LL pw[100];

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int cas,i,j,ic,n;
	scanf("%d",&cas);
	for(ic=1;ic<=cas;ic++){
		scanf("%s",str);
		memset(tg,0,sizeof(tg));
		for(i=0;str[i];i++) tg[str[i]]=1;
		int base=0;
		n=strlen(str);
		for(i=0;i<256;i++) if(tg[i]) base++;
		if(base==1) base=2;
		pw[0]=1;
		for(i=1;i<=n;i++) pw[i]=pw[i-1]*base;
		for(i=0;i<256;i++) val[i]=-1;
		val[str[0]]=1;
		memset(tg,0,sizeof(tg));
		tg[1]=1;
		LL ans=pw[n-1];
		for(i=1;str[i];i++){
			if(val[str[i]]==-1){
				for(j=0;;j++){	
					if(tg[j]==0){
						tg[j]=1;
						val[str[i]]=j;
						break;
					}
				}
			}
			ans+=pw[n-i-1]*val[str[i]];
		}
		printf("Case #%d: %lld\n",ic,ans);
	}
    return 0;
}
