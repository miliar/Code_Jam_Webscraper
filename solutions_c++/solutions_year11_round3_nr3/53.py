/* by Ashar Fuadi [fushar] */

#include <cstdio>
#include <cstring>

#include <vector>
#include <string>
#include <set>
#include <list>
#include <map>
#include <utility>
#include <iostream>
#include <algorithm>

using namespace std;

#define REP(i,n) for (int i = 0; i < (int)n; i++)
#define FOR(i, a, b) for (int i = (int)a; i <= (int)b; i++)
#define REPE(i,c) for (typeof((c).end()) i = (c).begin(); i != (c).end(); ++i)
#define RESET(c,v) memset(c, v, sizeof(c))

#define pb push_back
#define mp make_pair

int T;
int N, L, H, freq[2000];
int main()
{
	freopen("C-small-attempt0.in", "r", stdin); freopen("C-small-attempt0.out", "w", stdout);
	//freopen("C-large.in", "r", stdin); freopen("C-large.out", "w", stdout);
	
	scanf("%d", &T);
	REP(tc, T)
	{
		scanf("%d%d%d", &N, &L, &H);
		REP(i, N)
			scanf("%d", &freq[i]);
	
		printf("Case #%d: ", tc+1);
		bool kemal = false;
		
		for (int i = L; i <= H; i++)
		{
			bool maulana = true;
			REP(j, N)
			{
				if (i % freq[j] && freq[j] % i)
				{
					maulana = false;
					break;
				}
			}
			if (maulana)
			{
				kemal = true;
				printf("%d\n", i);
				break;
			}
		}
		if (!kemal)
			puts("NO");
	}
}
