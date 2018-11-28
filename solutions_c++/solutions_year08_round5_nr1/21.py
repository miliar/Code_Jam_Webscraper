#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cctype> 
#include <string> 
#include <cstring> 
#include <ctime> 

using namespace std;

int minh[7000],maxh[7000];
int minl[7000],maxl[7000];

vector<int> hh[7000];

int a[7000][7000];

int neigh[4][2]={{0,1},{1,0},{0,-1},{-1,0}};

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	int i,j,l,t,m,n,ans,x,y,dire,h;
	char s[1000];
	string pa;
	scanf("%d",&t);
	for (l=0;l<t;l++)
	{
		scanf("%d",&m);
		pa="";
		for (i=0;i<m;i++)
		{
			scanf("%s%d",s,&x);
			for (j=0;j<x;j++)
				pa=pa+s;
		}
		for (i=0;i<7000;i++)
		{
			minh[i]=7000;
			maxh[i]=0;
			minl[i]=7000;
			maxl[i]=0;
			hh[i].clear();
		}
		x=3500;y=3500;
		dire=0;
		for (i=0;i<pa.length();i++)
		{
			switch (pa[i])
			{
			case 'R':
				dire=(dire+1)%4;
				break;
			case 'L':
				dire=(dire+3)%4;
				break;
			case 'F':
				x+=neigh[dire][0];
				y+=neigh[dire][1];
				if (neigh[dire][0]==0)
				{
					h=y;
					if (neigh[dire][1]==1) h--;
					if (x<minh[h]) minh[h]=x;
					if (x>maxh[h]) maxh[h]=x;
					hh[h].push_back(x);
				}
				else
				{
					h=x;
					if (neigh[dire][0]==1) h--;
					if (y<minl[h]) minl[h]=y;
					if (y>maxl[h]) maxl[h]=y;
				}
				break;
			}
		}
		memset(a,0,sizeof(a));
		for (i=0;i<7000;i++)
		{
			if (maxh[i]>=minh[i])
			{
				for (j=minh[i];j<maxh[i];j++)
					a[j][i]=1;
			}
			if (maxl[i]>=minl[i])
			{
				for (j=minl[i];j<maxl[i];j++)
					a[i][j]=1;
			}
		}
		ans=0;
		for (i=0;i<7000;i++)
		{
			sort(hh[i].begin(),hh[i].end());
			for (j=0;j<hh[i].size();j+=2)
				ans-=(hh[i][j+1]-hh[i][j]);

		}
		for (i=0;i<7000;i++)
			for (j=0;j<7000;j++)
				if (a[i][j]==1) ans++;
		printf("Case #%d: %d\n",l+1,ans);
	}
	return 0;
}

