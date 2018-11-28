#include <cstdio>
#include <cstring>

using namespace std;

typedef long long LL;

#define ALL(x) (x).begin(), (x).end()
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); ++i)
#define FORI(it, v) for(__typeof((v).begin()) it = (v).begin(); it != (v).end(); ++it)
#define pb push_back
#define mp make_pair

#define MAXK 8
#define MAXN 10005

int K;
int MIN;
char s[MAXN], news[MAXN];

char used[MAXK];
int st[MAXK];

inline void applyPerm(int poz)
{
	char tmp[MAXK];
	for (int k = 0; k < K; k++)
		tmp[k] = news[poz + st[k]];
	for (int k = 0; k < K; k++)
		news[poz + k] = tmp[k];
}

void back(int k)
{
	if (k == K)
	{
		memcpy(news, s, sizeof(s));
		for (int i = 0; news[i]; i += K)
			applyPerm(i);
		int Nr = 1;
		for (int i = 1; news[i]; i++)
			Nr += news[i] != news[i - 1];
		if (Nr < MIN)
			MIN = Nr;
		return;
	}

	for (int i = 0; i < K; i++)
		if (!used[i])
		{
			st[k] = i;
			used[i] = 1;
			back(k + 1);
			used[i] = 0;
		}
}

int main()
{
//	freopen("D.in", "rt", stdin);
//	freopen("D.out", "wt", stdout);

	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		scanf("%d %s", &K, s);
		MIN = 0x3f3f3f3f;
		back(0);
		printf("Case #%d: %d\n", t, MIN);
	}
	return 0;
}


