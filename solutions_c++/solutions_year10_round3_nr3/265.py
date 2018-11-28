#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <queue>
#include <cassert>

#define MAXN 515
#define MAXM (515 * 4 + 1)

using namespace std;

int f[MAXN + 1][MAXM + 1];
int a[MAXN + 1][MAXM + 1];
int s[MAXN + 1][MAXM + 1];
int n, m;
int num[257];
void Out(int a[MAXN + 1][MAXM + 1])
{
    for (int i = 1; i <= n; i ++)
    {
	for (int j = 1; j <= m; j ++)
	{
	    printf("%d ", a[i][j]);
	}
	printf("\n");
    }
    printf("\n");
}

void Init()
{
    for (int i = 0; i <= 9; i ++)
	num[i + '0'] = i;
    for (int i = 'A'; i <= 'F'; i ++)
	num[i] = i - 'A' + 10;
    scanf("%d%d", &n, &m);
    memset(a, -1, sizeof(a));
    char s[513] = {0};
    for (int i = 1; i <= n; i ++)
    {
	scanf("%s", s);
	for (int j = 0; j < (m >> 2); j ++)
	{
	    int t = num[s[j]];
	    for (int k = 3; k >= 0; k --)
		a[i][j * 4 + 3 - k + 1] = (!((t >> k) & 1));
	}
    }
}

class Node
{
    public:
	Node(){}
	Node(int _len, int _x, int _y):len(_len),x(_x),y(_y){}
	int len, x, y;
	inline friend bool operator < (const Node &a, const Node &b)
	{
	    if (a.len != b.len)
		return a.len < b.len;
	    if (a.x != b.x)
		return a.x > b.x;
	    return a.y > b.y;
	}
};

//#define TREE_STRUCTURED_ARRAY
#ifdef TREE_STRUCTURED_ARRAY
#define Lowbit(x) ((x) & (-(x)))

int Get(int x, int y)
{
    int tx = x, ty;
    int ret = 0;
    while (tx)
    {
	ty = y;
	while (ty)
	    ret += s[tx][ty], ty -= Lowbit(ty);
	tx -= Lowbit(tx);
    }
    return ret;
}

int S(int x1, int y1 ,int x2, int y2)
{
    return Get(x2 ,y2) - Get(x1 - 1, y2) - Get(x2, y1 - 1) + Get(x1 - 1, y1 - 1);
}


void Add(int x, int y1, int y2)
{
    int len = Lowbit(x);
    int y = y1;
    while (y <= m + 1)
	s[x][y] += len, y += Lowbit(y);
    y = y2 + 1;
    while (y <= m + 1)
	s[x][y] -= len, y += Lowbit(y);
}

void Add(int x1, int y1, int x2 , int y2)
{
    int x = x1;
    while (x <= x2)
    {
	Add(x, y1, y2);
	x += Lowbit(x);
    }
}

#else
int S(int x1, int y1, int x2, int y2)
{
    for (int i = x1;  i <= x2; i ++)
	for (int j = y1; j <= y2; j ++)
	    if (s[i][j])
		return true;
    return false;
}

void Add(int x1, int y1, int x2, int y2)
{
    for (int i = x1;  i <= x2; i ++)
	for (int j = y1; j <= y2; j ++)
	    s[i][j] = true;
}

#endif
int hash[MAXN + 1];
void DP()
{
    for (int i = 1; i <= n; i ++)
	for (int j = 1; j <= m; j ++)
	{
	    f[i][j] = 1;
	    if (a[i - 1][j] == a[i][j - 1]  && a[i][j - 1] == (!a[i - 1][j - 1]) && a[i - 1][j - 1] == a[i][j])
		f[i][j] = min(f[i - 1][j], min(f[i][j - 1], f[i - 1][j - 1])) + 1;
	}

}
void GetAns()
{
    for(int i = 1; i <= n; i ++)
	for (int j = 1; j <= m; j ++)
	    s[i][j] = 0;
    int sum = 0;
    memset(hash, 0, sizeof(hash));
    while (sum < n * m)
    {
	memset(f, 0, sizeof(f));
	int maxlen = 0, x, y;
	for (int i = 1; i <= n; i ++)
	    for (int j = 1; j <= m; j ++)
		if (!s[i][j])
		{
		    f[i][j] = 1;
		    if (a[i - 1][j] == a[i][j - 1]  && a[i][j - 1] == (!a[i - 1][j - 1]) && a[i - 1][j - 1] == a[i][j])
			f[i][j] = min(f[i - 1][j], min(f[i][j - 1], f[i - 1][j - 1])) + 1;
		    if (maxlen < f[i][j])
			maxlen = f[i][j], x = i, y = j;
		}
	if (maxlen == 1)
	{
	    hash[1] = n * m - sum;
	    break;
	}
	hash[maxlen] ++;
	sum += maxlen * maxlen;
	Add(x - maxlen + 1, y - maxlen + 1, x, y);
    }
    /*
       priority_queue<Node> H;
       for (int i = 1; i <= n; i ++)
	for (int j = 1; j <= m; j ++)
	{
	    f[i][j] = 1;
	    if (a[i - 1][j] == a[i][j - 1]  && a[i][j - 1] == (!a[i - 1][j - 1]) && a[i - 1][j - 1] == a[i][j])
		f[i][j] = min(f[i - 1][j], min(f[i][j - 1], f[i - 1][j - 1])) + 1;
	    if (i == 2 && j == 13)
	    {
		int asdf = 0;
	    }
	    H.push(Node(f[i][j], i, j));
	}
    Node t;
    memset(hash, 0, sizeof(hash));
    while (!H.empty())
    {
	t = H.top(); H.pop();
	int x1 = t.x - t.len + 1, y1 = t.y - t.len + 1, x2 = t.x, y2 = t.y, len = t.len;
	if (S(x1, y1, x2, y2))
	    continue;
	Add(x1, y1, x2, y2);
	hash[len] ++;
    }
    */
}

void Solve(int id)
{
    fprintf(stderr, "%d\n", id);
    Init();
    GetAns();
    int cnt = 0;
    for (int i = n; i >= 1; i --)
	if (hash[i])
	    cnt ++;
    printf("Case #%d: %d\n", id, cnt);
    for (int i = n; i >= 1; i --)
	if (hash[i])
	    printf("%d %d\n", i, hash[i]);
}

int main()
{
    freopen("3.in2", "r", stdin);
    freopen("3.out2", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; i ++)
	Solve(i);
    return 0;
}

