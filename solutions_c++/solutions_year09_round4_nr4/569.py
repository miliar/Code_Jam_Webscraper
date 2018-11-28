#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <limits>
#include <vector>
#include <queue>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;

const int nmax=3;
int x[nmax],y[nmax],r[nmax];

inline int sqr(int x) { return x*x; }

int main(int argc,char* argv[])
{
    int num_test_cases;
    scanf("%d",&num_test_cases);
    for(int test_case=1; test_case<=num_test_cases; test_case++)
    {
	int n;
	scanf("%d",&n);
	for(int i=0;i<n;i++)
	    scanf("%d%d%d",x+i,y+i,r+i);

	double R=numeric_limits<double>::infinity();
	if(n==1)
	    R=r[0];
	else if(n==2)
	    R=max(r[0],r[1]);
	else
	{
	    for(int i=0;i<n;i++)
	    {
		int a=(i+1)%n,b=(i+2)%n;
		double dist=sqrt(sqr(x[a]-x[b])+sqr(y[a]-y[b]));
		R=min(R,max((double)r[i], dist+r[a]+r[b])/2.0);
	    }
	}
	printf("Case #%d: %.7lf\n",test_case,R);
	
    }
    return 0;
}
