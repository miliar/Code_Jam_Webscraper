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

char s[65];
vector<int> q;
int n;

void pb(ll v)
{
	for(int i=n-1;i>=0;i--)
		printf("%d", (v>>i)&1);
	printf("\n");
}

bool rec(int i, ll v)
{
	if(i==q.size())
	{
		ll s = sqrt(v);
		if(s*s == v)
		{
			pb(v);
			return true;
		}
		return false;
	}
	return rec(i+1, v) || rec(i+1, v | (1LL<<(q[i])));
}

int main(int argc,char* argv[])
{
    int num_test_cases;
    scanf("%d",&num_test_cases);
    for(int test_case=1; test_case<=num_test_cases; test_case++)
    {
		ll v = 0;
		q.clear();
		scanf(" %s", s);
		n = strlen(s);
		for(int i=0;s[i];i++)
		{
			v = (v<<1)+(s[i] == '1');
			if(s[i] == '?')
				q.push_back(n-i-1);
		}
		//printf("%lld\n", v);
		//for(int i=0;i<q.size();i++) printf("%lld ", q[i]); printf("\n");
		
		printf("Case #%d: ",test_case);
		if(!rec(0, v))
			printf("FAIL\n");
    }
    return 0;
}
