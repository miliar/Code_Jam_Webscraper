#include <cstdio>
#include <cstring>
#include <cctype>

const int limit_word = 100 + 10;
const int limit_leng = 50 + 10;
const int mod = 10009;

int		n, k;
char	tar	[limit_leng];
int		word[limit_word][26];
int		ans[20];

void init()
{
	memset(word, 0, sizeof(word));
	scanf("%s%d", tar, &k);
	scanf("%d", &n);

	char	buf	[limit_leng];
	for (int i = 0; i < n; i ++)
	{
		scanf("%s", buf);
		for (char* p = buf; *p; p ++)
			word[i][*p - 'a'] ++;
	}
}

struct	State
{
	int	cnt[4];
};

const int M = 2171371;

struct	StateStore
{
	int head, tail;
	State queue[M];
	int count[M];
	int mark[M];
	int pos[M];
	int curt_mark;

	void init()
	{
		curt_mark = 0;
		memset(mark, 0, sizeof(mark));
	}

	void clear()
	{
		head = 0; tail = -1;
		curt_mark ++;
	}

	void add(const State& stat, int cnt, int i)
	{
		int delta = (long long)cnt * stat.cnt[0] * stat.cnt[1] * stat.cnt[2] * stat.cnt[3] % mod;
		ans[i] += delta; if (ans[i] >= mod) ans[i] -= mod;

		int h = 0;
		for (i = 0; i < 4; i ++)
			h = (h * 131 + stat.cnt[i]) % M;
		while (mark[h] == curt_mark)
		{
			if (stat.cnt[0] == queue[pos[h]].cnt[0] && 
				stat.cnt[1] == queue[pos[h]].cnt[1] &&
				stat.cnt[2] == queue[pos[h]].cnt[2] &&
				stat.cnt[3] == queue[pos[h]].cnt[3] )
			{
				count[pos[h]] += cnt; return;
			}
			h ++;
			if (h == M) h = 0;
		}
		mark[h] = curt_mark;
		pos[h] = ++ tail;
		queue[ tail ] = stat;
		count[ tail ] = cnt;
	}

} dp[2];

void process(char* str, int leng)
{
	int target[10];
	
	int i;
	State start;
	start.cnt[0] = start.cnt[1] = start.cnt[2] = start.cnt[3] = 1;
	for (i = 0; i < leng; i ++) 
	{		
		target[i] = str[i] - 'a';
		start.cnt[i] = 0;
	}

	int	prev, curt;
	dp[0].init();
	dp[1].init();

	dp[0].clear();
	dp[0].add(start, 1, 0);

	prev = 0;

	int p, x, j;
	int count;
	State stat, new_stat;
	
	for (i = 0; i < k; i ++)
	{
		curt = 1 - prev;
		dp[curt].clear();

		for (p = dp[prev].head; p <= dp[prev].tail; p ++)
		{
			stat = dp[prev].queue[ p ];
			count = dp[prev].count[ p ];

			for (x = 0; x < n; x ++)
			{
				new_stat = stat;
				for (j = 0; j < leng; j ++)
					new_stat.cnt[j] += word[x][ target[j] ];
				dp[curt].add(new_stat, count, i + 1);
			}
		}

		prev = curt;

//		if (dp[curt].tail > 1000)
//		fprintf(stderr, "%d " , dp[curt].tail);
	}
}

void solve()
{
	memset(ans, 0, sizeof(ans));

	int i, j;
	for (i = 0; ; )
	{
		for (j = i; isalpha(tar[j]); j ++) ;
		process(tar + i, j - i);

		if (!tar[j]) break;
		i = j + 1;
	}

	for (i = 1; i <= k; i ++)
		printf(" %d", ans[i]);
	printf("\n");
}

int main()
{
//	freopen("in.txt", "r", stdin);
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("B.out", "w", stdout);

	int caseNo, t;
	scanf("%d", &caseNo);

	for (t = 1; t <= caseNo; t ++)
	{
		printf("Case #%d:", t);

		init();
		solve();
	}

	return 0;
}