#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int i,j,k,n,m;
int I,T;
int ga[200][200];
int a[200][200];
int nu[200];
int opt[200];

bool cmp(int x,int y)
{
	return a[x][y];
}
int ma[250][250];
bool vi[500];
int y[500];
bool find(int a)
{
      for(int i=0;i<n;++i)
            if(ma[a][i]&&!vi[i])
            {
                  vi[i]=1;
                  if(y[i]==-1||find(y[i]))
                  {
                        y[i]=a;
                        return true;
                  }
            }
      return false;
}
main()
{
	scanf("%d",&T);
	for (I=1;I<=T;++I)
	{
		int ans=0;
		scanf("%d%d",&n,&m);
		for (i=0;i<n;++i)
			for (j=0;j<m;++j)
				scanf("%d",&ga[i][j]);
		memset(ma,0,sizeof ma);
		for (i=0;i<n;++i)
			for (j=0;j<n;++j)
			{
				bool f=1;
				for (k=0;k<m;++k)
					if (ga[i][k]>=ga[j][k]) 
					{
						f=0;
						break;
					}
				if (f) ma[i][j]=1;
			}

		memset(y,-1,sizeof y);
		for (i=0;i<n;++i)
		{
			memset(vi,0,sizeof vi);
			if (find(i))++ans;
		}
/*		for (i=0;i<n;++i)
			nu[i]=i;
		

		//sort(nu,nu+n,cmp);
		for (i=0;i<n;++i)
		{
			int tmp=i;
			for (j=i+1;j<n;++j)
			{
				if (a[nu[j]][nu[tmp]]==1)
					tmp=j;
			}
			swap(nu[i],nu[tmp]);
		}
		for (i=0;i<n;++i)
			printf("%d\n",nu[i]);		
		opt[0]=1;
		for (i=1;i<n;++i)
		{
			int tmp=1;
			for (j=0;j<i;++j)
				if (a[nu[i]][nu[j]]==0 && opt[j]+1>tmp)
				{
					printf("%d gx %d %d\n",nu[j],nu[i],a[nu[j]][nu[i]]);
					tmp=opt[j]+1;
				}
			opt[i]=tmp;
			printf("%d\n",opt[i]);
			if (opt[i]>ans) ans=opt[i];
		}*/
		printf("Case #%d: %d\n",I,n-ans);
	}
	return 0;
}
