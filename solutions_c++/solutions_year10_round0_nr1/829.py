#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <cctype>
#include <memory>
#include <vector>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

typedef long long Int;
typedef long double Double;
typedef vector<int> VInt;
typedef vector< vector<int> > VVInt;
typedef pair<int,int> PII;

#define FOR(i,n,m) for(i=(n); i<(m); ++i)
#define RFOR(i,n,m) for(i=(n)-1; i>=(m); --i)
#define CLEAR(x,y) memset((x), (y), sizeof(x))
#define COPY(x,y) memcpy((x),(y),sizeof(x))
#define PB push_back
#define MP make_pair
#define SIZE(v) ((int)((v).size()))
#define ALL(v) (v).begin(), (v).end()

int main()
{
//	freopen("A-small.in", "r", stdin);
//	freopen("A-small.out", "w", stdout);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int T, t;
	scanf("%d", &T);
	for (t = 0; t < T; ++t)
	{
		int N, K;
		scanf("%d%d", &N, &K);
		int i;
		for (i = 0; i < N; ++i)
		{
			if (K & 1)
				K >>= 1;
			else
				break;
		}
		printf("Case #%d: %s\n", t+1, i < N ? "OFF" : "ON");
	}
	return 0;
}