#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <set>
#include <vector>
#include <string>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector <int> vi;

int T;
int n, a[1010];

int main()
{
  scanf("%d", &T);
  for (int t = 0; t < T; ++t)
  {
    scanf("%d", &n);
    int r = 0, m = 1000100;
    int sum = 0;
    for (int i = 0; i < n; ++i)
    {
    	scanf("%d", &a[i]);
    	m = min(m, a[i]);
    	r ^= a[i];
    	sum += a[i];
    }
    if (r)
  		printf("Case #%d: NO\n", t + 1);
  	else
  		printf("Case #%d: %d\n", t + 1, sum - m);
  }
	return 0;
}          