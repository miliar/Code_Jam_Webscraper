#include <stdio.h>
#include <string.h>
using namespace std;

bool vis[17][256];
int n,m,len;
char x[5001][17];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	
	scanf("%d %d %d",&len,&n,&m);
	
	int i,j,k,t,ret;
	char c;
	
	for(i=0;i<n;i++)
		scanf("%s",x[i]);
		
	for(i=0;i<m;i++) {
		memset(vis,0,sizeof(vis));
		k=0; j=0;
		
		while(1) {
			if(k==len) break;
			scanf("%c",&c);
			
			if(c==' ' || c=='\n') continue;
			else if(c=='(') j=1;
			else if(c==')') {
				j=0; k++;
			}
			else {
				vis[k][c]=1;
				if(!j) k++;
			}
		}
		
		for(ret=0,j=0;j<n;j++) {
			for(k=0,t=0;t<len;t++)
				if(vis[t][x[j][t]]) k++;
			
			if(k==len) ret++;
		}
		
		printf("Case #%d: %d\n",i+1,ret);
	}
}
