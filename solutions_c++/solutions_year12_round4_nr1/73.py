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

const int nmax = 10005;
int d[nmax], l[nmax];
int s[nmax];

int main(int argc,char* argv[])
{
	int num_test_cases;
	scanf("%d",&num_test_cases);
	for(int test_case=1; test_case<=num_test_cases; test_case++)
	{
		int n;
		scanf("%d", &n);
		for(int i=0; i<n;i++)
			scanf("%d%d", d+i, l+i);
		int D;
		scanf("%d", &D);
		for(int i=0; i<n;i++)
			s[i] = -1;
		s[0] = d[0];
		bool r = false;
		for(int i=0; i<n;i++)
			if(s[i] >= 0)
			{
				for(int j=i+1;j<n;j++)
					if(d[j] <= d[i] + s[i])
						s[j] = max(s[j], min(l[j], d[j] - d[i]));
				if(D <= d[i] + s[i])
					r = true;
			}
		printf("Case #%d: %s\n",test_case, r ? "YES" : "NO");
		
	}
	return 0;
}
