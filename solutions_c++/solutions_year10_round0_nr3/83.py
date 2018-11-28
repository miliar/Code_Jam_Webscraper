#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <limits>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <string>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
const int INF = numeric_limits<int>::max();

const int nmax = 1005;
int p[nmax];
ll ps[nmax];
int g[nmax];

int main(int argc,char* argv[])
{
    int num_test_cases;
    scanf("%d",&num_test_cases);
    for(int test_case=1; test_case<=num_test_cases; test_case++)
    {
	fill(p, p + nmax, -1);
	int r, c, n;
	scanf("%d%d%d", &r, &c, &n);
	for(int i=0;i<n;i++)
	    scanf("%d",g+i);
	int f = 0;
	ll y = 0;
	for(int i=0; i<r; i++)
	{
	    if(p[f] >= 0)
	    {
		int j = p[f];
		int d = i - j, a = r - i;
		y += (a / d) * (y - ps[j]) + (ps[j + a % d] - ps[j]);
		break;
	    }
	    p[f] = i;
	    ps[i] = y;
	    //printf("%d %d %lld\n",i,f,y);
	    
	    int t = 0, fp = f;
	    while(t+g[f]<=c)
	    {
		t+=g[f];
		if(++f >= n)
		    f -= n;
		if(f == fp)
		    break;
	    }
	    y += t;
	}
	printf("Case #%d: %lld\n",test_case,y);
	
    }
    return 0;
}
