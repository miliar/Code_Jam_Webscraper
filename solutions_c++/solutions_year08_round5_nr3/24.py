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

char a[100][100];
int d[20][2000];
int cnt[2000];

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);

	vector<int> aa;
	int i,j,k,o,l,t,n,m,b1;
	int ans;
	memset(cnt,0,sizeof(cnt));
	for (i=0;i<(1<<10);i++)
	{
		for (j=0;j<10;j++)
			if (((1<<j)&i)!=0) cnt[i]++;
	}
	scanf("%d",&t);
	for (l=0;l<t;l++)
	{
		scanf("%d%d",&m,&n);
		for (i=0;i<m;i++)
			scanf("%s",a[i]);
		aa.clear();
		for (i=0;i<(1<<n);i++)
		{
			b1=1;
			for (j=0;j<n-1;j++)
				if ((((1<<j)&i)!=0)&&(((1<<(j+1))&i)!=0))
					b1=0;
			if (b1==1) aa.push_back(i);
		}
		memset(d,-1,sizeof(d));
		for (i=0;i<aa.size();i++)
		{
			b1=1;
			for (j=0;j<n;j++)
				if ((((1<<j)&aa[i])!=0)&&(a[0][j]=='x')) b1=0;
			if (b1==1)
			{
				d[0][aa[i]]=cnt[aa[i]];
			}
		}
		for (i=0;i<m-1;i++)
			for (j=0;j<(1<<n);j++)
				if (d[i][j]>-1)
				{
					for (k=0;k<aa.size();k++)
					{
						b1=1;
						for (o=0;o<n;o++)
							if ((((1<<o)&aa[k])!=0)&&(a[i+1][o]=='x')) b1=0;
						if (b1==0) continue;
						b1=1;
						for (o=0;o<n-1;o++)
							if (((((1<<o)&j)!=0)&&(((1<<(o+1))&aa[k])!=0))||
								((((1<<o)&aa[k])!=0)&&(((1<<(o+1))&j)!=0)))
							{
								b1=0;break;
							}
						if (b1==1)
						{
							if (d[i][j]+cnt[aa[k]]>d[i+1][aa[k]]) d[i+1][aa[k]]=d[i][j]+cnt[aa[k]];
						}
					}
				}
		ans=-1;
		for (i=0;i<aa.size();i++)
			if (d[m-1][aa[i]]>ans) ans=d[m-1][aa[i]];
		printf("Case #%d: %d\n",l+1,ans);
	}
	return 0;
}

