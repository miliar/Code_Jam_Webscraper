#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>

#include<cmath>
#include<iostream>
#include<fstream>

#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>
#include<iterator>
using namespace std;

#define i64 __int64
#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b) ((a)<(b)?(a):(b))
#define pi acos(-1.0)
#define inf ((i64)1<<30)
#define CLR(a) memset(a,0,sizeof(a))
#define SET(a) memset(a,-1,sizeof(a))
#define pb push_back
#define eps 1e-11
#define NCOUNT 1050

int m[NCOUNT],pr[NCOUNT],p,n;


int main()
{
	freopen("B-small-attempt1.in","r",stdin);
	//freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int cs,i,j,k,bt,t=1,sz,flag,cnt;
	cin>>cs;
	while(cs--)
	{
		cin>>p;
		n=1<<p;
		for(i=0;i<n;i++)
		{
			cin>>m[i];
			m[i]=p-m[i];
		}
		k=0;
		cnt=0;
		for(i=0;i<p;i++)
		{
			for(j=0;j<(1<<(p-i-1));j++)
			{
				cin>>pr[k++];
			}
		}
		for(i=1;i<n;i*=2)
		{
			sz=n/i;
			for(j=0;j<i;j++)
			{
				flag=0;
				for(k=j*sz;k<(j+1)*sz;k++)
				{
					if(m[k])
					{
						flag=1;
						break;
					}
				}
				if(flag)
				{
					for(k=j*sz;k<(j+1)*sz;k++)
					{
						if(m[k])
							m[k]--;
					}
					cnt++;
				}
			}
		}
		printf("Case #%d: %d\n",t++,cnt);
	}
	
	return 0;
}
