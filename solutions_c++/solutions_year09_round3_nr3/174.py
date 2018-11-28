#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

int n,q,best[105][105],x[105];

int calc(short s, short e)
{
	if(s>e) return 0;
	if(best[s][e]!=-1) return best[s][e];
	
	int i,k,ret=1<<30;
	
	for(i=s;i<=e;i++) {
		k = calc(s,i-1) + calc(i+1,e);
		k += x[e+1]-x[s-1]-2;

		ret = min(k, ret);
	}
	
	return best[s][e]=ret;
}

int main()
{
	int T,t,i;
	
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	
	scanf("%d",&T);
	
	for(t=1;t<=T;t++) 
	{
		memset(best,-1,sizeof(best));
		
		scanf("%d %d",&n,&q);
		
		x[0]=-1; x[q+1]=n;
		
		for(i=1;i<=q;i++) {
			scanf("%d",&x[i]);
			x[i]--;
		}
		
		printf("Case #%d: %d\n",t,calc(1,q));
	}
}

