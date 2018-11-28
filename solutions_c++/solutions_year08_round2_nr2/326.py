#include <iostream>

using namespace std;


bool use[1100];
bool mat[1100][1100];
int a,b,p;


bool good(int x, int y)
{
	while(x>0 && y>0)
		if(x>y)
			x%=y;
		else
			y%=x;
	int nod = x+y;
	for(int i=2; i<p; i++)
	{
		while(nod%i==0)
			nod/=i;
	}
	return nod!=1;
}


void dfs(int v)
{
	use[v]=true;
	for(int i=a; i<=b; i++)
		if(!use[i] && mat[v][i])
		{
			bool tmp = good(v,i);
			if(!tmp)
			{
				mat[v][i]=false;
				mat[i][v]=false;
			}
			else
				dfs(i);
		}
}


int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int c;
	scanf("%d",&c);
	for(int i=0; i<c; i++)
	{
		int res = 0;
		scanf("%d%d%d",&a,&b,&p);
		memset(mat,true,sizeof(mat));
		memset(use,false,sizeof(use));
		for(int j=a; j<=b; j++)
		{
			if(!use[j])
			{
				res++;
				dfs(j);
			}
		}
		printf("Case #%d: %d\n",i+1,res);
	}
	return 0;
}