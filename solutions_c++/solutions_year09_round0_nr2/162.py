#include <stdio.h>
#include <string.h>
using namespace std;

int T,t,n,m,x[101][101],ans[101][101],last,mov[][2]={{-1,0},{0,-1},{0,1},{1,0}};

int explore(int a,int b)
{
	if(ans[a][b]) return ans[a][b];
	
	int i,j=-1,k=1<<30;
	
	for(i=0;i<4;i++) {
		if(a+mov[i][0] < 0 || a+mov[i][0] >= n) continue;
		if(b+mov[i][1] < 0 || b+mov[i][1] >= m) continue;
		if(x[a+mov[i][0]][b+mov[i][1]] >= k) continue;
		
		j=i; k=x[a+mov[i][0]][b+mov[i][1]];
	}
	
	if(k>=x[a][b]) j=-1;
	
	if(j==-1) {
		ans[a][b] = last;
		return last++;
	}
	else {
		k = explore(a+mov[j][0],b+mov[j][1]);
		ans[a][b] = k;
		return k;
	}
}

int main()
{
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	
	int i,j,k;
	
	scanf("%d",&T);
	
	for(t=0;t<T;t++) {
		scanf("%d %d",&n,&m);
		
		last=1;
		memset(ans,0,sizeof(ans));
		
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
				scanf("%d",&x[i][j]);
				
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
				if(!ans[i][j]) explore(i,j);
		
		printf("Case #%d:\n",t+1);
		for(i=0;i<n;i++) {
			printf("%c",ans[i][0]+'a'-1);
			
			for(j=1;j<m;j++)
				printf(" %c",ans[i][j]+'a'-1);
			printf("\n");
		}
	}
}
