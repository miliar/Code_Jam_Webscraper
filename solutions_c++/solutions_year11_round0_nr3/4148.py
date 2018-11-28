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
#define inf (1<<29)
#define CLR(a) memset(a,0,sizeof(a))
#define SET(a) memset(a,-1,sizeof(a))
#define pb push_back
#define all(a) a.begin(),a.end()
#define eps 1e-9
#define i64 long long
#define MX 1000002

typedef pair<int,int> pii;

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int n,a,cs,t=1,ret,sum,mn;
	cin>>cs;
	while(cs--)
	{
		cin>>n;
		ret=sum=0;
		mn=10000000;
		while(n--)
		{
			cin>>a;
			ret^=a;
			mn=min(mn,a);
			sum+=a;
		}
		printf("Case #%d: ",t++);
		if(ret)printf("NO");
		else printf("%d",sum-mn);
		puts("");
	}
	return 0;
}


