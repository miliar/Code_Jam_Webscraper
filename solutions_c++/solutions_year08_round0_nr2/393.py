#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <memory>
#include <cctype>
#include <string>
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
typedef pair<int,int> PII;
typedef vector<int> VInt;

#define FOR(i, a, b) for(i = (a); i < (b); ++i)
#define RFOR(i, a, b) for(i = (a) - 1; i >= (b); --i)
#define CLEAR(a, b) memset(a, b, sizeof(a))
#define SIZE(a) int((a).size())
#define ALL(a) (a).begin(),(a).end()
#define PB push_back
#define MP make_pair

int main()
{
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	
	int T, t;
	scanf("%d", &T);
	FOR(t, 0, T)
	{
		int time;
		int N[2];
		scanf("%d%d%d", &time, &N[0], &N[1]);

		int i, j;
		vector< pair<int, PII> > v;
		FOR(i, 0, 2)
			FOR(j, 0, N[i])
			{
				int hh, mm, tt;
				scanf("%d:%d", &hh, &mm);
				tt = hh*60 + mm;
				v.PB(MP(tt, PII(1, i)));

				scanf("%d:%d", &hh, &mm);
				tt = hh*60 + mm + time;
				v.PB(MP(tt, PII(0, i ^ 1)));
			}

		sort(ALL(v));

		int res[] = {0, 0};
		int trains[] = {0, 0};
		FOR(i, 0, SIZE(v))
		{
			int pos = v[i].second.second;
			if(v[i].second.first == 0)
				++trains[pos];
			else
			{
				if(trains[pos] == 0)
					++res[pos];
				else
					--trains[pos];
			}
		}

		printf("Case #%d: %d %d\n", t + 1, res[0], res[1]);
	}
	
	return 0;
};
