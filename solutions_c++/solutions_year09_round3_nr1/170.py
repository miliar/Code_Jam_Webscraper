#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

int vis[256],tak[256],num[256];
char str[70];

int main()
{
	int T,t,n,k,i,j;
	
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	
	scanf("%d",&T);
	
	for(t=1;t<=T;t++) {
		scanf("%s",str);
		
		memset(tak,0,sizeof(tak));
		memset(vis,-1,sizeof(vis));
		
		n=strlen(str);
		
		tak[1]=1; vis[str[0]]=1; num[0]=1;
		
		for(i=1;i<n;i++) {
			if(vis[str[i]]!=-1)
				num[i]=vis[str[i]];
			else {
				for(j=0;;j++) {
					if(!tak[j]) {
						vis[str[i]]=j;
						num[i]=j;
						tak[j]=1;
						break;
					}
				}
			}
		}
		
		for(k=0,i=0;i<n;i++)
			k = max(k, num[i]);
		
		k++;
		
		long long ret=0;
		
		for(long long jj=1,i=n-1;i>=0;i--) {
			ret += jj*num[i];
			jj*=k;
		}
		
		printf("Case #%d: %lld\n",t,ret);
	}
	
}
