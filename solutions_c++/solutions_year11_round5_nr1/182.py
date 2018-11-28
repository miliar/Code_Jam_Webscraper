#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <ctime>
#include <cassert>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <utility>
using namespace std;

#define MAX(A,B) ((A)>(B)?(A):(B))
#define MIN(A,B) ((A)<(B)?(A):(B))
#define S(X) ((X)*(X))
#define ABS(X) ((X)>0?(X):(-(X)))
#define SZ(X) (int)(X.size())
typedef pair<int,int> PII;
typedef __int64 LL;
typedef pair<double,double> PDD;

vector<PDD> Low, Up;
int L, U;
double total;

double AREA(PDD A, PDD B)
{
	return A.first*B.second - A.second*B.first;
}

void find_area()
{
	int i;
	total = 0;
	for(i=0;i<L-1;i++)
		total+=AREA( Low[i], Low[i+1] );
	for(i=0;i<U-1;i++)
		total-=AREA( Up[i], Up[i+1] );
	total+=AREA(Low[L-1],Up[U-1]);
	total+=AREA(Up[0],Low[0]);

 	total = ABS(total);
}

double f(double cut)
{
	int i;

	double now = 0;
	PDD dummy1, dummy2;

	for(i=0;i<L-1;i++)
		if(Low[i+1].first<=cut)
			now+=AREA( Low[i], Low[i+1] );
		else
		{
			dummy1 = PDD(cut, (Low[i+1].second - Low[i].second)/(Low[i+1].first - Low[i].first)*(cut - Low[i].first) + Low[i].second );
			now+=AREA( Low[i], dummy1 );
			break;
		}

	for(i=0;i<U-1;i++)
		if(Up[i+1].first<=cut)
			now-=AREA( Up[i], Up[i+1] );
		else
		{
			dummy2 = PDD(cut, (Up[i+1].second - Up[i].second)/(Up[i+1].first - Up[i].first)*(cut - Up[i].first) + Up[i].second);
			now-=AREA( Up[i], dummy2 );
			break;
		}

	now += AREA(Up[0],Low[0]);
	now+=AREA(dummy1,dummy2);
	now = ABS(now);

	return now;
}

int main()
{
//	freopen("A-small-attempt0.in","r",stdin); freopen("A-small-output0.out","w",stdout);
//	freopen("A-small-attempt1.in","r",stdin); freopen("A-small-output1.out","w",stdout);
//	freopen("A-small-attempt2.in","r",stdin); freopen("A-small-output2.out","w",stdout);
	freopen("A-large.in","r",stdin); freopen("A-large.out","w",stdout);

	int T, ks;
	int W, G;
	int i, j;
	double x,y;
	double lo, hi, mid, now;

	scanf("%d",&T);
	for(ks=1;ks<=T;ks++)
	{
		printf("Case #%d:\n",ks);

		scanf("%d%d%d%d",&W,&L,&U,&G);

		Low.clear();
		Up.clear();

		for(i=0;i<L;i++)
		{
			scanf("%lf%lf",&x,&y);
			Low.push_back( PDD(x,y) );
		}

		for(i=0;i<U;i++)
		{
			scanf("%lf%lf",&x,&y);
			Up.push_back( PDD(x,y) );
		}

		find_area();

		for(i=1;i<G;i++)
		{
			now = total/G*i;

			lo = 0;
			hi = W;

			for(j=0;j<100;j++)
			{
				mid = (lo+hi)/2;

				if( f(mid)< now )lo = mid;
				else hi = mid;
			}
			printf("%.10lf\n",lo);
		}


	}

	return 0;
}