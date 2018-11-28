#include <cstdio>
#include <cstring>
#include <vector>
const int maxn = 133;
const int maxm = 133;
char form[maxn][maxn];
int start[maxn], to[maxm], next[maxm], edge;
void add(const int a, const int b)
{
	to[++edge] = b;
	next[edge] = start[a];
	start[a] = edge;
}
int n;
char s[maxn];
char l[maxn], lc;
int in[maxn];
char last = 0, nextc;
void work(int now)
{
	memset(form, 0, sizeof form);
	memset(start, 0, sizeof start);
	edge = 0;
	lc = 0;
	for (scanf("%d", &n); n--; )
	{
		scanf("%s", s);
		form[s[0]][s[1]] = s[2];
		form[s[1]][s[0]] = s[2];
	}
	for (scanf("%d", &n); n--; )
	{
		scanf("%s", s);
		add(s[0], s[1]);
		add(s[1], s[0]);
	}

	memset(in, 0, sizeof in);
	scanf("%d%s", &n, s);
	last = 0;
	for (int i = 0; i < n; ++i)
	{
		if ((nextc = form[last][s[i]]))
			--in[last], l[lc - 1] = nextc, ++in[nextc], last = nextc;
		else
		{
			for (int e = start[s[i]]; e; e = next[e])
				if (in[to[e]])
				{
					lc = 0;
					memset(in, 0, sizeof in);
					last = 0;
					goto nextl;
				}
			++in[s[i]];
			l[lc++] = s[i];
			last = s[i];
nextl:;
		}
	}
	printf("Case #%d: [",now);
	for (int i = 0; i < lc - 1; ++i)
		printf("%c, ", l[i]);
	if (lc)
		printf("%c]\n", l[lc - 1]);
	else
		puts("]");
}
int main()
{
	int n;
	scanf("%d", &n);
	for (int i = 1; i <=n; ++i)
		work(i);
}
