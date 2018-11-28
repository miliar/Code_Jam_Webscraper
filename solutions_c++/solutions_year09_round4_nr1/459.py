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
//typedef __int64 LL;

int val[50];
char grid[50][50];

int main()
{
	int i,j,k,n,tests,cs=0;
	
//	freopen("C:\\Asmall.in","r",stdin);
	freopen("Alarge.out","w",stdout);
	scanf("%d",&tests);

	while(tests--)
	{
		scanf("%d",&n);

		for(i=0;i<n;i++)
			scanf("%s",grid[i]);

		vi all;

		for(i=0;i<n;i++)
		{
			int r=0;

			for(j=0;j<n;j++)
			{
				if(grid[i][j]=='1')
					r=MAX(r,j);
			}
			all.pb(r);
		}

		int ans=0;

		for(i=0;i<n;i++)
		{
			for(j=i;j<n;j++)
			{
				if(all[j]<=i) break;
			}

			ans+=j-i;

			for(k=j-1;k>=i;k--)
				swap(all[k],all[k+1]);
		}

		printf("Case #%d: %d\n",++cs,ans);

	}


	return 0;
} 


