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
		int n;
		scanf("%d", &n);
		int xs=0, cmin=INF, sum=0;
		for(int i=0;i<n;i++)
		{
			int c;
			scanf("%d", &c);
			xs ^= c;
			cmin = min(cmin, c);
			sum += c;
		}

		printf("Case #%d: ", test_case);
		if(xs == 0)
			printf("%d\n", sum - cmin);
		else
			printf("NO\n");
    }
    return 0;
}
