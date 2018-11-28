#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
const int mx=310;

int n;

struct table
{
	int ta[mx];
}ta[mx];

int g[mx][mx];

int visit[mx];
int m;
int link[mx],ans;

bool cmp(table a,table b)
{
	return a.ta[0]<b.ta[0];
}

bool yes(int x,int y)
{
	int i;
	for(i=0;i<m;i++) 
		if(ta[x].ta[i]>=ta[y].ta[i]) return false;
	return true;
}


int find(int a)
{
	int i,k;
	for(i=0;i<n;i++)
	{
		if(!visit[i]&&g[a][i])
		{
			k=link[i];
			link[i]=a;
			visit[i]=1;
			if(k==-1||find(k)) return 1;
			link[i]=k;
		}
	}
	return 0;
}


int main()
{freopen("C-large.in","r",stdin);
freopen("outC.txt","w",stdout);
    int t,ca,i,j;
    scanf("%d",&t);
    for(ca=1;ca<=t;ca++)
    {
        scanf("%d%d",&n,&m);
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
			{
				scanf("%d",&ta[i].ta[j]);
			}
		}
		sort(ta,ta+n,cmp);
		memset(g,0,sizeof(g));
		for(i=0;i<n;i++)
		{
			for(j=i+1;j<n;j++)
			{
				if(yes(i,j))g[i][j]=1;
			}
		}
		memset(link,-1,sizeof(link));
		int ans=0;
		for(i=0;i<n;i++){
			memset(visit,0,sizeof(visit));
			if(find(i)) ans++;
		}
		printf("Case #%d: %d\n",ca,n-ans);
    }

    return 0;
}

