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


const int MAXN=11;
int x[MAXN], y[MAXN], z[MAXN], p[MAXN];
int N;

bool intersects(int pnt1, int pnt2, double cpower)
{
	double dist1=(cpower*p[pnt1]);
	double dist2=(cpower*p[pnt2]);
	if(abs(x[pnt1]-x[pnt2])+abs(y[pnt1]-y[pnt2])+abs(z[pnt1]-z[pnt2]) <= dist1+dist2)
		return true;
	else
		return false;
}

int main()
{
	int a,b,c,d,tests;

	const string strFile = "c-small";
	string fin = strFile+".in";
	string fout = strFile+".out";

	freopen(fin.c_str(), "rt", stdin);
	freopen(fout.c_str(), "wt", stdout);

	scanf("%d\n", &tests);

for(int test=1;test<=tests;test++)
{

	scanf("%d", &N);
	fo(a,N)
		scanf("%d%d%d%d",&x[a],&y[a],&z[a],&p[a]);

	double res;
	double l,r,m;

	l=0;
	r=1e+7;

	bool good;

	while(l+(1e-8)<r)
	{
		m=(l+r)/2;

		good=true;
		for(a=0;a<N && good;a++)
		for(b=a+1;b<N;b++)
			if(!intersects(a,b,m))
			{
				good=false;
				break;
			}

		if(good)
			r=m;
		else
			l=m;
	}

	printf("Case #%d: %.9lf\n",test,l);

}

	fclose(stdout);
	fclose(stdin);
	return 0;
}
