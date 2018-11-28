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

int n, pd, pg;

int gcd(int a, int b)
{
	if(b==0)
		return a;
	return gcd(b, a%b);
}

bool pos()
{
	if(pg == 0 && pd > 0 || pg == 100 && pd < 100)
		return false;
	int p=pd, q=100;
	int g = gcd(p, q);
	p /= g;
	q /= g;
	if(q > n)
		return false;
	return true;
}

int main(int argc,char* argv[])
{
    int num_test_cases;
    scanf("%d",&num_test_cases);
    for(int test_case=1; test_case<=num_test_cases; test_case++)
    {
		scanf("%d%d%d", &n, &pd, &pg);
		printf("Case #%d: %s\n", test_case, pos() ? "Possible" : "Broken");
    }
    return 0;
}
