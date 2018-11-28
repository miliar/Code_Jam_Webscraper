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

#define MAXD 1000005

int A, B, P;
int p[MAXD];
#define p(N) p[ ((int)(N)) - (A) ]

inline int getSet( int x )
{
	if (x == p(x))
		return x;
	return p(x) = getSet( p(x) );
}

inline void unite( int a, int b )
{
	a = getSet(a);
	b = getSet(b);
	if (a == b)
		return;

	if (rand() % 2)
		p(a) = b;
	else
		p(b) = a;
}

inline int prim( int k )
{
	if (k == 2)
		return 1;
	if (k % 2 == 0)
		return 0;

	for (int i = 3; i * i <= k; i += 2)
		if (k % i == 0)
			return 0;
	return 1;
}

int main()
{
	srand(7);
//	freopen("B.in", "rt", stdin);
//	freopen("B.out", "wt", stdout);

	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		scanf("%d %d %d", &A, &B, &P);
		for (int i = 0; i <= B - A; i++)
			p[i] = i + A;

		for (int i = P; i <= B - A; i++)
		{
			if (!prim(i))
				continue;
			int poz = A;
			if (A % i != 0)
				poz += i - (A % i);
			for (poz += i; poz <= B; poz += i)
				unite( poz, poz - i );
		}

		set<int> tmp;
		tmp.clear();
		for (int i = A; i <= B; i++)
			tmp.insert( getSet(i) );
		
		printf("Case #%d: %d\n", t, (int)tmp.size());
	}

	return 0;
}


