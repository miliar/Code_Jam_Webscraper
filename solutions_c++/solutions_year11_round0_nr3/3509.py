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
#include <ctime>


using namespace std;

#define MEM(a,b) memset(a,(b),sizeof(a))
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b)  ((a) < (b) ? (a) : (b))
#define istr(S) istringstream sin(S)
#define MP make_pair
#define pb push_back
#define inf 1000000000
#define maxn 1000000

//typedef long long  LL;
//typedef __int64 LL;

typedef pair<int,int> pi;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef vector<pi> vpi;

int main()
{
	int i,j,k,tests,cs=0,n;


	freopen("E:\\GCJ\\Cl.in","r",stdin);
	freopen("E:\\GCJ\\Clarge2.out","w",stdout);

	scanf("%d",&tests);

	while(tests--)
	{
		int xor=0,ans=inf,sum=0;
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%d",&k);
			ans=MIN(ans,k);
			sum+=k;
			xor^=k;
		}

		if(xor)
			printf("Case #%d: NO\n",++cs);
		else
			printf("Case #%d: %d\n",++cs,sum-ans);

	}

	return 0;
} 


