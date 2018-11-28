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



#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b) ((a)<(b)?(a):(b))
#define pi acos(-1.0)
#define inf ((i64)1<<30)
#define CLR(a) memset(a,0,sizeof(a))
#define SET(a) memset(a,-1,sizeof(a))
#define pb push_back
#define all(a) a.begin(),a.end()
#define eps 1e-11
#define i64 long long


int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int cs,t=1,n,k,x,i;
	cin>>cs;
	while(cs--)
	{
		cin>>n>>k;
		x=1;
		for(i=1;i<=n;i++)
		{
			x*=2;
		}
		if(k%(x)==(x-1))
		{
			printf("Case #%d: ON\n",t++);
		}
		else
		{
			printf("Case #%d: OFF\n",t++);
		}
	}
	return 0;
}


