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
		int T = 0;
		int t[2], p[2];
		t[0] = t[1] = 0;
		p[0] = p[1] = 1;
		for(int i=0;i<n;i++)
		{
			char c;
			int b;
			scanf(" %c%d", &c, &b);
			int r = c == 'B';
			T = max(t[r] + abs(p[r] - b), T) + 1;
			t[r] = T;
			p[r] = b;
		}
		printf("Case #%d: %d\n", test_case, T);
	
    }
    return 0;
}
