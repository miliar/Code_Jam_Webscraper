#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <memory.h>
#include <vector>
#include <map>
#include <queue>
#include <algorithm>
#include <string>

#define REP(i,n) for(int i=0; i<n; i++)
#define REPD(i,n) for(int i=(n-1); i>=0; i--)
#define FOR(i,a,b) for(int i=a; i<=b; i++)
#define FORD(i, a,b) for(int i=a; i>=b; i--)
#define FILL(a, v) memset(&a, v, sizeof(a))
#define DB(x) cout << #x << " : " << x << endl
#define pb push_back
#define mp make_pair
#define x first
#define y second

using namespace std;

const int MAXN = 1000;

int T, c, d, n;
char s[MAXN];
char combine[255][255];
vector<char> oppose[255];
char st[MAXN]; int sz;
int cnt[255];

int main()
{
	//freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	scanf("%d", &T);
	FOR(Tn, 1, T)
	{
		printf("Case #%d: [", Tn);
		sz = 0;
		FILL(cnt, 0); 
		FILL(combine, 0);
		FILL(oppose, 0);
		FILL(st, 0);
		FILL(s, 0);
		scanf("%d", &c);
		REP(i, c)
		{
			cin >> s;
			combine[s[0]][s[1]] = combine[s[1]][s[0]] = s[2];
		}
		scanf("%d", &d);
		REP(i, d)
		{ 
			cin >> s;
			oppose[s[0]].pb(s[1]);
			oppose[s[1]].pb(s[0]);
		}
		scanf("%d", &n);
		cin >> s;
		REP(i, n)
		{
			st[sz++] = s[i];
			cnt[s[i]]++;
			while (sz > 1 && combine[st[sz-2]][st[sz-1]] != 0)
			{
				cnt[st[sz-1]]--;
				cnt[st[sz-2]]--;
				st[sz-2] = combine[st[sz-2]][st[sz-1]];
				sz--;
				cnt[st[sz-1]]++;
			}
			REP(i, oppose[st[sz-1]].size())
			{
				if (cnt[oppose[st[sz-1]][i]] > 0)
				{
					FILL(cnt, 0); sz = 0;
					break;
				}
			}
		}
		REP(i, sz)
		{
			if (i) printf(", ");
			printf("%c", st[i]);
		}
		printf("]\n");
	}
	return 0;
}
