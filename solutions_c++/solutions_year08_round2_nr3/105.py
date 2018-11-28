#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>

using namespace std;

typedef vector<string> vs;
typedef vector<int> vi;
typedef pair<int, int> pii;

#define FOR(i,n) for (i = 0; i < (n); i++)
#define FORI(i,a,b) for (i = (a); i <= (b); i++)
#define FORD(i,a,b) for (i = (a); i >= (b); i--)
#define ZERO(a) memset(a, 0, sizeof(a))
#define MINUS(a) memset(a, -1, sizeof(a))

#define MAXN 5001

int num[MAXN];
int tc, K, n;
deque<int> abc;

int main()
{
	int t, i, j,k, l;
	scanf("%d", &tc);
	FOR(t, tc)
	{
 		fprintf(stderr, "%d\n", t);
		scanf("%d", &K);	
		MINUS(num);
		l = 0;
		FOR(i, K) { abc.push_back(i); }
		FOR(i, K)
		{
			FORI(j, 0, i - 1) { k = abc.front(); abc.pop_front(); abc.push_back(k); }
			num[abc.front()] = i;
			abc.pop_front();
		}
//		printf("ok\n");
		
		printf("Case #%d:", t + 1);
		scanf("%d", &n);
		FOR(i, n)
		{
			scanf("%d", &k);
			printf(" %d", num[k-1] + 1);
		}
		printf("\n");
	}
	return 0;
}

