#include<iostream>
#include<cstring>
using namespace std;

bool v[10010];
bool vv[110];
int a[110];
int p,q;
int ans;

int com(int t)
{
	int s=0;
	int l=t-1,r=t+1;
	while(l>=1&&!v[l]) 
	{
		s++;
		l--;
	}
	while(r<=p&&!v[r])
	{
		s++;
		r++;
	}
	return s;
}

void dfs(int t,int s)
{
	int i;
	if(t==q)
	{
		if(s<ans) ans=s;
	}
	else
	{
		for(i=0;i<q;i++) 
		{
			if(!vv[i])
			{
				vv[i]=true;
				v[a[i]]=true;
             dfs(t+1,s+com(a[i]));
			 vv[i]=false;
			 v[a[i]]=false;
			}
		}
	}
}

int main()
{
    int t,i,k;
	freopen("C-small-attempt0.in","r",stdin);
	freopen("c.out","w",stdout);
	scanf("%d",&t);
	for(k=1;k<=t;k++)
	{
		scanf("%d%d",&p,&q);
		for(i=0;i<q;i++) scanf("%d",&a[i]);
		 ans=100000000;
		int s=com(a[0]);
//		printf("%d\n",s);
		memset(v,false,sizeof(v));
		memset(vv,false,sizeof(vv));
		dfs(0,0);
		printf("Case #%d: %d\n",k,ans);
	}
	return 0;
}
