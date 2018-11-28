#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <bitset>
#include <list>
#include <algorithm>
#include <cmath>

#include <cstdlib>
#include <ctime>

using namespace std;

typedef long long LL;

#define ALL(x) (x).begin(), (x).end()
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); ++i)
#define FORI(it, v) for(__typeof((v).begin()) it = (v).begin(); it != (v).end(); ++it)
#define pb push_back
#define mp make_pair

#define MAXN 128

int N, Q;
map<string, int> S;
set< pair<int, int>, greater< pair<int, int> > > H;

vector<int> Qs;
queue<int> nxt[MAXN];

char tmp[1024];

int main()
{
//	freopen("A.in", "rt", stdin);
//	freopen("A.out", "wt", stdout);

	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		scanf("%d ", &N);
		S.clear(); Qs.clear(); H.clear();
		for (int i = 0; i < N; i++)
		{
			fgets(tmp, 1024, stdin);
			S[string(tmp)] = i;

			for (; !nxt[i].empty(); nxt[i].pop());
		}

		scanf("%d ", &Q);
		for (int i = 0; i < Q; i++)
		{
			fgets(tmp, 1024, stdin);
			if (S.find( string(tmp) ) == S.end())
			{
				i--; Q--;
				continue;
			}
			int ID = S[ string(tmp) ];
			Qs.push_back(ID);
			nxt[ID].push(i);
		}

		for (int i = 0; i < N; i++)
		{
			nxt[i].push(Q);
			H.insert( make_pair( nxt[i].front(), i ) );
		}

		int cur = (*H.begin()).second;
		int NR = 0;
		for (int i = 0; i < Q; i++)
		{
			H.erase( make_pair( nxt[ Qs[i] ].front(), Qs[i] ) );
			nxt[ Qs[i] ].pop();
			H.insert( make_pair( nxt[ Qs[i] ].front(), Qs[i] ) );

			if (cur == Qs[i])
			{
				set< pair<int, int> > :: iterator it;
				it = H.begin();
				if (cur == it -> second)
					it++;

				cur = it -> second;
				NR++;
			}
		}
		printf("Case #%d: %d\n", t, NR);
	}

	return 0;
}


