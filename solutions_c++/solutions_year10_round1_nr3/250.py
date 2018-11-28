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

const int nmax = 1000005;
int dp[nmax];				// dp[a] = smallest b that is losing position

int main(int argc,char* argv[])
{
    dp[1] = 1;
    for(int a=2;a<nmax;a++)
    {
	int b;
	for(b=dp[a-1];b>=dp[a-b] && b<dp[a-b]+a-b;b++);
	dp[a] = b;
    }
    
    int num_test_cases;
    scanf("%d",&num_test_cases);
    for(int test_case=1; test_case<=num_test_cases; test_case++)
    {
	int a1,a2,b1,b2;
	scanf("%d%d%d%d", &a1, &a2, &b1, &b2);

	/*int c=0;
	for(int a=a1;a<=a2;a++)
	    for(int b=b1;b<=b2;b++)
	    c += (b < dp[a] || b >= dp[a]+a);*/

	ll c=0;
	for(int a=a1;a<=a2;a++)
	{
	    int z = min(dp[a]+a, b2+1) - max(dp[a], b1);
	    c += b2 - b1 + 1 - max(z, 0);
	}
	printf("Case #%d: %lld\n",test_case,c);
    }
    return 0;
}
