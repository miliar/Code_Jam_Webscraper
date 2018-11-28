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
int l[nmax], p[nmax];

int main(int argc,char* argv[])
{
	int num_test_cases;
	scanf("%d",&num_test_cases);
	for(int test_case=1; test_case<=num_test_cases; test_case++)
	{
		int n;
		scanf("%d", &n);
		for(int i=0;i<n;i++)
			scanf("%d", l+i);
		for(int i=0;i<n;i++)
			scanf("%d", p+i);
		
		pii s[nmax];
		for(int i=0;i<n;i++)
			s[i] = pii(-p[i], i);
		sort(s, s+n);
		
		printf("Case #%d:",test_case);
		for(int i=0;i<n;i++)
			printf(" %d", s[i].second);
		printf("\n");
	}
	return 0;
}
