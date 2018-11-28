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
int a[nmax];

int main(int argc,char* argv[])
{
    int num_test_cases;
    scanf("%d",&num_test_cases);
    for(int test_case=1; test_case<=num_test_cases; test_case++)
    {
		int n;
		scanf("%d", &n);
		int s=0;
		for(int i=1;i<=n;i++)
		{
			scanf("%d", a+i);
			if(a[i]!=i)
				s++;
		}
		printf("Case #%d: %d\n", test_case, s);
    }
    return 0;
}
