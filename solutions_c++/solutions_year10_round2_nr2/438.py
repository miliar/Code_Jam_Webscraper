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

int vi[100],x[100],v[100];

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int cs,n,k,i,j,t,b,tt=1,res,cnt;
	cin>>cs;
	while(cs--)
	{
		cin>>n>>k>>b>>t;
		for(i=0;i<n;i++)
		{
			cin>>x[i];
		}
		for(i=0;i<n;i++)
		{
			cin>>v[i];
		}
		CLR(vi);
		res=0;
		cnt=0;
		for(i=n-1;i>=0;i--)
		{
			if((b-x[i])<=v[i]*t)
			{
				vi[i]=1;
				cnt++;
				for(j=n-1;j>i;j--)
				{
					res+=!vi[j];
				}
			}
			if(cnt>=k)
				break;
		}
		printf("Case #%d: ",tt++);
		if(cnt<k)
		{
			printf("IMPOSSIBLE\n");
		}
		else
		{
			printf("%d\n",res);
		}
	}
	return 0;
}


