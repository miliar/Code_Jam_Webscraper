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

inline double getdist(int x1, int y1, int x2, int y2)
{
	return sqrt((double)(x2-x1)*(x2-x1)+(double)(y2-y1)*(y2-y1));
}

inline double getarea(int x1, int y1, int x2, int y2, int x3, int y3)
{
	double a=getdist(x1,y1,x2,y2);
	double b=getdist(x2,y2,x3,y3);
	double c=getdist(x3,y3,x1,y1);
	double p=(a+b+c)/2;
	return sqrt((p-a)*(p-b)*(p-c)*p);
}

int main()
{
	int a,b,c,d,tests;

	const string strFile = "b-small";
	string fin = strFile+".in";
	string fout = strFile+".out";

	freopen(fin.c_str(), "rt", stdin);
	freopen(fout.c_str(), "wt", stdout);

	scanf("%d", &tests);

	int N,M,A;

for(int test=1;test<=tests;test++)
{

	scanf("%d%d%d", &N, &M, &A);
	int x1,x2,x3;
	int y1,y2,y3;
	int sx1,sx2,sx3;
	int sy1,sy2,sy3;

	y1=0;
	int found=0;
	double area;

	x1=0;y1=0;
	for(x2=0;x2<=N && !found;x2++)
	for(y2=0;y2<=M && !found;y2++)
	for(x3=0;x3<=N && !found;x3++)
	for(y3=0;y3<=M && !found;y3++)
	if(!(x1==x2 && y1==y2 || x1==x3 && y1==y3 || x2==x3 && y2==y3))
	{
		area=getarea(x1,y1,x2,y2,x3,y3);
		if(fabs(area*2-A)<1e-7)
		{
			found=1;
			sx1=x1;
			sx2=x2;
			sx3=x3;
			sy1=y1;
			sy2=y2;
			sy3=y3;
		}
	}

	y1=0;
	x2=0;
	for(x1=0;x1<=N && !found;x1++)
	for(y2=0;y2<=M && !found;y2++)
	for(x3=x1+1;x3<=N && !found;x3++)
	for(y3=0;y3<=M && !found;y3++)
	if(!(x1==x2 && y1==y2 || x1==x3 && y1==y3 || x2==x3 && y2==y3))
	{
		area=getarea(x1,y1,x2,y2,x3,y3);
		if(fabs(area*2-A)<1e-7)
		{
			found=1;
			sx1=x1;
			sx2=x2;
			sx3=x3;
			sy1=y1;
			sy2=y2;
			sy3=y3;
		}
	}

	if(found)
		printf("Case #%d: %d %d %d %d %d %d\n", test, sx1, sy1, sx2, sy2, sx3, sy3);
	else
		printf("Case #%d: IMPOSSIBLE\n", test);
}

	fclose(stdout);
	fclose(stdin);
	return 0;
}
