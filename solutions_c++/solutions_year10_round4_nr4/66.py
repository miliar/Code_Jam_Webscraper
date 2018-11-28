#include <stdio.h>
#include <math.h>
#include <string.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#pragma comment(linker, "/STACK:16777216")
using namespace std;

#define bit(n) (1<<(n))
#define inf 1000000000
#define eps 1e-9
#define PI 3.1415926535897932385
#define pb push_back
#define sz size()
#define mp make_pair
#define cl clear()
#define all(a) a.begin(),a.end()
#define fill(ar,val) memset(ar,val,sizeof ar)
#define MIN(a,b) if(a>(b)) a=(b)
#define MAX(a,b) if(a<(b)) a=(b)
#define sqr(x) ((x)*(x))
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))

typedef vector<int> VI;
typedef pair<int,int> PII;
typedef __int64 LL;

int main()
{
	freopen("D1.in","r",stdin);
	freopen("D1.out","w",stdout);
	int TST,tst=0;
	for(scanf("%d",&TST);TST--;)
	{
		printf("Case #%d:",++tst);
		int n,m;
		scanf("%d%d",&n,&m);
		int x1,y1,x2,y2;
		scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
		double d=hypot(x1-x2,y1-y2);
		for(int i=0;i<m;i++)
		{
			int x,y;
			scanf("%d%d",&x,&y);
			double ar=0;
			double d1=hypot(x-x1,y-y1);
			double d2=hypot(x-x2,y-y2);
			double a1=2*acos((d1*d1+d*d-d2*d2)/(2*d1*d));
			ar+=d1*d1*(a1-sin(a1))/2;
			double a2=2*acos((d2*d2+d*d-d1*d1)/(2*d2*d));
			ar+=d2*d2*(a2-sin(a2))/2;
			printf(" %.7lf",ar);
		}
		printf("\n");
	}
	return 0;
}
