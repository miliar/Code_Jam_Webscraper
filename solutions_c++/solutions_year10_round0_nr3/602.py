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
//typedef long long LL;
typedef __int64 LL;

int g[1005],seen[1005];
LL cost[1005];

int main()
{
	int i,j,k,tests,cs=0,n;
	
	freopen("C:\\C-large.in","r",stdin);
	freopen("C:\\Clarge.out","w",stdout);

	scanf("%d",&tests);

	while(tests--)
	{
		LL ans=0,R,K;
		scanf("%I64d%I64d%d",&R,&K,&n);
		for(i=0;i<n;i++)
			scanf("%d",&g[i]);

		MEM(seen,0);

		int cnt=0,at=0;

		while(R)
		{
			if(seen[at])
			{
				int x=seen[at];
				LL len=cnt-x+1;
				LL tc =cost[cnt]-cost[x-1];
				ans+=(R/len)*tc;
				R%=len;

				LL sc= cost[x+R-1]-cost[x-1];
				ans+=sc;
				break;
			}

			LL tot=0;
			int last=at;

			for(j=0;j<n;j++)
			{
				LL x=g[(at+j)%n];
				if(tot+x>K) break;
				last=(at+j)%n;
				tot+=x;
			}

		//	printf("%I64d %I64d\n",tot,R);

			ans+=tot;
			seen[at]=++cnt;
			cost[cnt] = cost[cnt-1]+tot ;
			at=(at+j)%n;
			R--;
		}
		
		printf("Case #%d: %I64d\n",++cs,ans);
	}

	return 0;
} 


