#include <stdio.h>
#include <string.h>




#define min(a,b) (((a)<(b))?(a):(b))

int n,m;
int price[200][30];



#define M 500
int nNode[M];
int match[M][M];
int flag[M];
int check[M];

int DFS(int p)
{
	int t,tmp,i;
	for (i = 0; i < nNode[p]; i ++)
	{
		t = i;
		i = match[p][i];
		if (!check[i])
		{
			check[i] = 1;
			tmp = flag[i];
			flag[i] = p;
			if (tmp == -1 || DFS(tmp))
			{
				return 1;
			}
			flag[i] = tmp;
		}
		i = t;
	}
	return 0;
}
bool ok(int i,int j,int m)
{
	int k;
	for( k=0;k<m;k++) 
		if(price[i][k]<=price[j][k]) 
			return false;
		return true;
}
int main()
{
	int i,j,k;
	int t,v;
	int cas,CAS;
	int ans;
	
		freopen("in.txt","r",stdin);
		freopen("out.txt","w",stdout);
	
	
	scanf("%d",&CAS);
	for (cas = 1; cas <= CAS; cas ++)
	{
		scanf("%d%d",&n,&m);	
		for (i=0;i<n;i++)
			for (j=0;j<m;j++)
				scanf("%d",&price[i][j]);
			memset(nNode,0,sizeof(nNode));
			
			for (i = 0; i < n; i ++) {
				for (j = 0; j < n; j ++) {
					if (i != j && ok(j,i,m)) {
						//	match[j][nNode[j] ++] = i;
						match[i][nNode[i] ++] = j;
					}
				}
			}
			memset(flag,-1,sizeof(flag));
			ans = 0;
			for (i = 0; i < n; i ++)
			{
				memset(check,0,sizeof(check));
				if (DFS(i) == 1)
					ans ++;
			}
			
		/*	for (i = 0; i < n; i ++) {
				printf("%d : %d\n",i,check[i]);
			}*/
			
			
			
			
			
			printf("Case #%d: %d\n",cas,n-ans);
	}
	return 0;
}
