#include<stdio.h>

int g[31],c[31],v[31];
int m,V;
int res;

int compute()
{
	int i;
	for(i=(m-1)/2; i>0;i--) 
	{
		if(g[i]==1) v[i] = v[2*i] && v[2*i+1];
		else v[i] = v[2*i] || v[2*i+1];
	//	printf("%d:%d\n",i+1,v[i]);
	}
	return v[1];
}

void dfs(int index,int change)
{
	int i;
	for(i=index;i<=(m-1)/2;i++) 
	{
		if(c[i]==1) {
			if(i<=(m-1)/2-1) dfs(i+1,change);
			g[i] = !g[i]; 
			if(V == compute()) {
				if(res > change+1) res = change+1;
				//return;
			}
			else dfs(i+1,change+1);
			g[i] = !g[i];
			
		}
	}
}


void solve(int tt)
{
	int i;
	scanf("%d%d",&m,&V);
	for(i=1;i<=(m-1)/2;i++) scanf("%d%d",&g[i],&c[i]);
	for(;i<=m;i++) scanf("%d",&v[i]);
//	for(i=0;i<m;i++) printf("%d:%d\n",i+1,v[i]);
	res = m;
	if(V==compute()) printf("Case #%d: 0\n", tt);
	else {
		dfs(1,0);
		if(res != m) printf("Case #%d: %d\n", tt, res);
		else printf("Case #%d: IMPOSSIBLE\n", tt);
	}	
}


int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	int N,i;
	scanf("%d",&N);
	for(i=1;i<=N;i++) solve(i);
	return 0;
}