#include <stdio.h>
#include <string.h>
#include <vector>
using namespace std;
#define pb push_back

int n,T,best[2][20];
vector <int> prev[256];
char s[]="welcome to code jam",x[510];

int main()
{
	bool mod;
	int i,j,k,t;
	
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	
	for(i=0;i<strlen(s);i++)
		prev[int(s[i])].pb(i);
		
	scanf("%d\n",&T);
	
	for(t=0;t<T;t++) {
		for(i=0;;i++) {
			scanf("%c",&x[i]);
			if(x[i]=='\n') {
				x[i]='\0';
				break;
			}
		}
		
		n = strlen(x);
		
		mod=1;
		memset(best,0,sizeof(best));
		best[1][0]=1;
		
		for(i=0;i<n;i++) {
			mod = !mod;
			
			for(j=0;j<20;j++)
				best[mod][j] = best[!mod][j];
			
			for(j=0;j<prev[x[i]].size();j++) {
				best[mod][prev[x[i]][j]+1] += best[!mod][prev[x[i]][j]];
				best[mod][prev[x[i]][j]+1] %= 10000;
			}
		}
		
		printf("Case #%d: ",t+1);
		
		if(best[mod][19] < 10) printf("000%d\n",best[mod][19]);
		else if(best[mod][19] < 100) printf("00%d\n",best[mod][19]);
		else if(best[mod][19] < 1000) printf("0%d\n",best[mod][19]);
		else printf("%d\n",best[mod][19]);
	}
}
