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

int n;
ll left;

int digits(int x)
{
	int r = 0;
	while(x>0)
	{
		x /= 10;
		r++;
	}
	return r;
}

ll pow(int b, int e)
{
	ll r = 1;
	for(int i=0;i<e;i++)
		r *= b;
	return r;
}

ll rot(ll x)
{
	return x/10 + (x%10) * left;
}

int main(int argc,char* argv[])
{
	int num_test_cases;
	scanf("%d",&num_test_cases);
	for(int test_case=1; test_case<=num_test_cases; test_case++)
	{
		int a,b;
		scanf("%d%d", &a, &b);
		n = digits(a);
		left = pow(10, n-1);
		ll count = 0;
		for(ll x=a;x<=b;x++)
		{
			for(ll y=rot(x);y!=x;y=rot(y))
			{
				if(y >= a && y <= b)
					count++;
			}
		}
		count /= 2;
		printf("Case #%d: %lld\n",test_case,count);
	
	}
	return 0;
}
