#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <utility>
#include <math.h>
#include <cstdlib>
#include <memory.h>
#include <queue>

#define pb push_back
#define i64 long long
#define mp make_pair
#define pii pair <int,int>
#define vi vector <int>
#define vii vector <pii>
#define f first
#define s second
#define foran(i,a,b) for (int i=a;i<(int)b;i++)
#define forn(i,n) for (int i=0;i<(int)n;i++)
#define ford(i,n) for (int i=(int)n-1;i>=0;i--)

const double eps = 1e-9;
const int int_inf = 2000000000;
const i64 i64_inf = 1000000000000000000LL;
const double pi = acos(-1.0);
 
using namespace std;
int tests;
int n,s,p;
int t[110];
int d[110][110];

int solve()
{
	memset(d,0,sizeof(d));
	d[0][0] = 0;
	
	for (int i=0; i<=n; i++)
	 for (int j=0; j<=i; j++)
		if (t[i+1] % 3 == 0)
		{
		    int nd = d[i][j];
		    if (t[i+1] / 3 >= p) nd++;
		    d[i+1][j] = max(d[i+1][j],nd);
		    if (t[i+1] == 0) continue;
		    nd = d[i][j];
		    if (t[i+1] / 3 + 1 >= p) nd++;
		    d[i+1][j+1] = max(d[i+1][j+1],nd);
		} else if (t[i+1] % 3 == 1)
		{
			int nd = d[i][j];
			if (t[i+1] / 3 + 1 >= p) nd++;
			d[i+1][j] = max(d[i+1][j],nd);
			if (t[i+1] == 1) continue;
			nd = d[i][j];
			if (t[i+1] / 3 + 1 >= p) nd++;
			d[i+1][j+1] = max(d[i+1][j+1],nd);
		} else
		{
			int nd = d[i][j];
			if (t[i+1] / 3 + 2 >= p) nd++;
			d[i+1][j+1] = max(d[i+1][j+1],nd);
			nd = d[i][j];
			if (t[i+1] / 3 + 1 >= p) nd++;
            d[i+1][j] = max(d[i+1][j],nd);			
		}
	return d[n][s];
}

int main() {
//  freopen("input.txt","r",stdin);
//  freopen("output.txt","w",stdout);
  cin >> tests;
  for (int test=1; test<=tests; test++)
  {
	scanf("%d%d%d",&n,&s,&p);
	for (int j=1; j<=n; j++) scanf("%d",&t[j]);
	printf("Case #%d: %d\n",test,solve());
  }
  
  return 0;
}