#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <queue> 
#include <deque> 
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
#include <ctime> 
using namespace std; 

const int inf = 1000*1000*1000; 
#define CL(x,a) memset(x,a,sizeof(x)); 
#define ALL(v) (v).begin(),(v).end() 
#define PII pair<int,int> 
#define PDI pair<double,int> 
#define MP(a,b) make_pair(a,b) 
#define FOR(i,n) for(int i=0;i<n;i++) 
typedef long long LL; 
typedef vector<int> vi; 
typedef vector< vi > vvi; 
typedef vector< vector<PII > > vvpii; 

int T,n,m,D;

char ar[512][512];
LL dp[512][512][512];

int main() 
{ 
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&T);
	for (int test=1;test <= T; test++)
	{
		int res = 0;
		scanf("%d%d%lf",&n,&m,&D);
		scanf("\n");
		FOR(i,n)
			gets(ar[i]);
		FOR(i,n)
		{
			FOR(j,m)
				ar[i][j]-='0';
		}
		for (int i=0;i+3<=n;i++)
		{
			for (int j=0;j+3<=m;j++)
			{
				for (int k = 3; i+k <= n && j+k <=m;k++)
				{
					double Cx = (i+i+k-1)/2.0;
					double Cy = (j+j+k-1)/2.0;
					double Sx = 0;
					double Sy = 0;
					for (int x=i;x<i+k;x++)
					{
						for (int y=j;y<j+k;y++)
						{
							Sx+=(x-Cx)*(D+ar[x][y]);
							Sy+=(y-Cy)*(D+ar[x][y]);
						}
					}
					Sx-=(i-Cx)*(D+ar[i][j]);
					Sx-=(i+k-1-Cx)*(D+ar[i+k-1][j+k-1]);
					Sx-=(i-Cx)*(D+ar[i][j+k-1]);
					Sx-=(i+k-1-Cx)*(D+ar[i+k-1][j]);
					
					Sy-=(j-Cy)*(D+ar[i][j]);
					Sy-=(j+k-1-Cy)*(D+ar[i+k-1][j+k-1]);
					Sy-=(j-Cy)*(D+ar[i+k-1][j]);
					Sy-=(j+k-1-Cy)*(D+ar[i][j+k-1]);
					if (fabs(Sx) < 1e-9 && fabs(Sy) < 1e-9)
					{
						res = max(res,k);
					}
				}
			}
		}
		if (res == 0)
			printf("Case #%d: IMPOSSIBLE\n",test);
		else
			printf("Case #%d: %d\n",test,res);
	}
	return 0; 
}