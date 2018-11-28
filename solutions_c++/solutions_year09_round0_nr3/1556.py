#include <cstdio>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cstring>
#include <cmath>
#include <queue>
#include <stack>
#include <algorithm>
using namespace std;

typedef long long int huge;
const int inf=0x3f2f1f0f;
const huge hinf=0x3fff2fff1fff0fffll;

#define foreach(i...) _foreach(i)
#define all(v) v.begin(), v.end()
#define _foreach(i, b, e) for(__typeof(b) i=b; i!=e; i++)
#define MAXN 510

int DP[MAXN][20];
char str1[MAXN];
char str2[20] = "welcome to code jam";

int main()
{
  int n;
  int l1, l2=strlen(str2);
  scanf(" %d", &n);
  for(int i=0; i<MAXN; ++i)
    DP[i][0]=1;
  for(int i=1; i<=l2; ++i)
    DP[0][i]=0;
  for(int z=1; z<=n; ++z)
    {
      scanf(" %[^\n]", str1);
      l1=strlen(str1);
      for(int i=1; i<=l1; ++i)
	for(int j=1; j<=l2; ++j)
	  {
	    DP[i][j]=DP[i-1][j];
	    if (str1[i-1]==str2[j-1])
	      DP[i][j]=(DP[i][j]+DP[i-1][j-1])%10000;
	  }
      printf("Case #%d: %04d\n", z, DP[l1][l2]);
    }
}
