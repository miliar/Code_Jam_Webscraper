#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <utility>
#include <set>
#include <map>
#include <queue>
using namespace std;

#define mset(A,B) memset(A,B,sizeof(A));
#define mcpy(A,B) memcpy(A,B,sizeof(B));
typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<string> vs;
#define FI(I,L,U) for (int I=L;I<U;I++)
#define sqr(x) ((x)*(x))

using namespace std;

int k;
char s[10000];
char ss[10000];

int len;
int p[6];
bool v[6];

int best = 100000000;
void dfs(int depth)
{
  if (depth == k)
  {
		for (int i = 0;i<len;i=i+k)
		{
			for (int j = 0;j<k;j++)
				ss[i+j] = s[i+p[j]];
		}
		int rle = 1;
		for (int i = 1;i<len;i++)
			 if (ss[i] != ss[i-1]) rle++;
		if (rle < best) best = rle;
	   
  }
  else
	  for (int i = 0;i<k;i++)
		  if (!v[i])
		  {
			p[depth] = i;
			v[i] = true;

			dfs(depth+1);
			v[i] = false;
		  }
}

bool rock[200][200];

int dp[200][200];

int main()
{
   int T;
   cin>>T;
   
   int ans = 0;

   int h,w,r;
   for (int c = 1;c<=T;c++)
   {

	   cin>>h>>w>>r;

	   memset(rock,0,sizeof(rock));
	   memset(dp,0,sizeof(dp));

	   for (int i = 1;i<=r;i++)
	   {
		   int x,y;
		   cin>>x>>y;
		   rock[x][y] = true;
	   }
	   dp[1][1] = 1;
	   for (int i = 1;i<=h;i++)
		   for (int j = 1;j<=w;j++) if (!rock[i][j])
		   {
			   if (i-1>0 && j-2>0) dp[i][j]+=dp[i-1][j-2];
			   if (i-2>0 && j-1>0) dp[i][j]+=dp[i-2][j-1];
			   dp[i][j]%=10007;
		   }

	   printf("Case #%d: %d\n", c , dp[h][w]);
   }
   return 0;
}
