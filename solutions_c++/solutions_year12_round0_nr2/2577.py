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

int main(int argc,char* argv[])
{
	int num_test_cases;
	scanf("%d",&num_test_cases);
	for(int test_case=1; test_case<=num_test_cases; test_case++)
	{
		int n, s, p;
		scanf("%d%d%d", &n, &s, &p);
		int r = 0;
		for(int i=0;i<n;i++)
		{
			int t;
			scanf("%d", &t);
			if(t>=p+max(p-1, 0)*2)
				r++;
			else if(t>=p+max(p-2, 0)*2 && s>0)
			{
				r++;
				s--;
			}
		}
		printf("Case #%d: %d\n",test_case, r);
	}
	return 0;
}
