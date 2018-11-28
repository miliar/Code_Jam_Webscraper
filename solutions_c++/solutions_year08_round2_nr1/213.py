#include <algorithm>
#include <string>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <queue>
#include <map>
#include <set>
using namespace std;

#define fo(a,n) for(a=0;a<n;a++)
#define memset0(v) memset(v,0,sizeof(v))
typedef vector<string> vs;
typedef vector<int> vi;

#ifdef __GNUC__
typedef long long ll;
typedef unsigned long long ull;
#else
typedef __int64 ll;
typedef unsigned __int64 ull;
#endif

int pnts[100001][2];

int main()
{
	int a,b,c,d,tests;
	int n,A,B,C,D,x0,y0,M;
	int total;

	freopen("a-small.in", "rt", stdin);
	freopen("a-small.out", "wt", stdout);

	scanf("%d",&tests);

for(int test=1;test<=tests;test++)
{

	scanf("%d%d%d%d%d%d%d%d", &n,&A,&B,&C,&D,&x0,&y0,&M);
	pnts[0][0]=x0;
	pnts[0][1]=y0;
	for(a=1;a<n;a++)
	{
		x0=((ll)A*x0+B)%M;
		y0=((ll)C*y0+D)%M;
		pnts[a][0]=x0;
		pnts[a][1]=y0;
	}

	total=0;
	int x1,x2,x3,y1,y2,y3;
	for(a=0;a<n;a++)
	for(b=a+1;b<n;b++)
	for(c=b+1;c<n;c++)
	{
		x1=pnts[a][0];x2=pnts[b][0];x3=pnts[c][0];
		y1=pnts[a][1];y2=pnts[b][1];y3=pnts[c][1];
		if(((ll)x1+x2+x3)%3==0 && ((ll)y1+y2+y3)%3==0) total++;
	}

	printf("Case #%d: %d\n",test,total);

}

	fclose(stdout);
	fclose(stdin);
	return 0;
}
