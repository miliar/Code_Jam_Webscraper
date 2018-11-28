#pragma warning(disable:4786)
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<functional>
#include<string>
#include<cstring>
#include<cstdlib>
#include<queue>
#include<utility>
#include<fstream>
#include<sstream>
#include<cmath>
#include<stack>
#include<cstdio>
#include <iomanip>


using namespace std;

#define MEM(a,b) memset(a,(b),sizeof(a))
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b)  ((a) < (b) ? (a) : (b))
#define istr(S) istringstream sin(S)
#define MP make_pair
#define pb push_back
#define inf 1000000000

typedef pair<int,int> pi;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef vector<pi> vpi;

#define inf 1000000000
#define M 100003

//typedef long long LL;
typedef __int64 LL;


int x[60],v[60];

int main()
{
	int i,j,k,l,tests,cs=0,n,b,t;
	

	//freopen("D:\\gcj\\B-large.in","r",stdin);
	freopen("Blarge.out","w",stdout);

	scanf("%d",&tests);
	while(tests--)
	{
		scanf("%d%d%d%d",&n,&k,&b,&t);
		for(i=0;i<n;i++)
			scanf("%d",&x[i]);
		for(i=0;i<n;i++)
			scanf("%d",&v[i]);

		int cnt=0;

		for(i=0;i<n;i++)
		{
			LL pos=(LL)x[i]+(LL)v[i]*t;
			if(pos>=b) cnt++;
		}
		

		if(cnt<k)
		{
			printf("Case #%d: IMPOSSIBLE\n",++cs);
			continue;
		}
	
		int ans=0;

		for(i=n-1;i>=0;i--)
		{
			LL pos=(LL)x[i]+(LL)v[i]*t;

			if(pos>=b)
				k--;
			else
				ans+=k;

			if(k==0) break;
		}

		printf("Case #%d: %d\n",++cs,ans);
	}

	return 0;
} 


