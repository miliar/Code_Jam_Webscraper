/*
#include <iostream>
#include <cmath>
using namespace std;

int Count(int R, int k, int pos)
{
	if (R == 0)
		return 0;
	if (k == 0)
		return 1;
	if (k < pos)
		return R;
	if (k == pos)
		return Count(R - (1 << pos), pos - 1, pos);

	int i, temp = 0;
	for (i = 0;  ;i++)
	{
		temp = (1 << i);
		
		if (temp >= R)
			break;
	}

	return ((i - 2 >= 0) ? int(pow(2.0, i - 2)) : 0) + Count(R - (1 << (i - 1)), k - 1, pos);
}

int main()
{
	int l;
	while (cin >> l)
	{
		for (int i = 0; i < 30; i++)
		{
			if ((1 << i) > l)
				cout << 0 << endl;
			else
			{
				if ((1 << i) == l)
					cout << endl;
				else
				{
					int j;
					for (j = i + 1; ;j++)
					{
						if ((1 << j) >= l)
							break;
					}
					cout << Count(l, j - 1 ,i) << endl;
				}
			}
		}
	}
	system("pause");
	return 0;
}
*/
/*
#include <iostream>
using namespace std;

const int MAXN = 100010;
int a[MAXN];
int b[MAXN];
int h[MAXN];

int main()
{
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
		scanf("%d", &h[i]);
	a[0] = 1;
	for (int i = 1; i < n; i++)
	{
		if (h[i] >= h[i - 1])
			a[i] = a[i - 1] + 1;
		else
			a[i] = 1;
	}
	b[n - 1] = 1;
	for (int i = n - 2; i >= 0; i--)
	{
		if (h[i] >= h[i + 1])
			b[i] = b[i + 1] + 1;
		else
			b[i] = 1;
	}
	int ans = -1;
	for (int i = 0; i < n; i++)
	{
		if (a[i] + b[i] - 1 > ans)
			ans = a[i] + b[i] - 1;
	}
	if (b[0] > ans)
		ans = b[0];
	if (a[n - 1] > ans)
		ans = a[n - 1];
	printf("%d\n", ans);
	system("pause");
	return 0;
}
*/

/*
#include <iostream>
using namespace std;

const int MAXN = 20;
bool used[MAXN];
int v[MAXN];
int n, ans, tot;

void check(int sold)
{
	int t[MAXN];
	int num = 0, sum = 0;
	for (int i = 0; i < n; i++)
	{
		if (!used[i])
		{
			t[num++] = v[i];
			sum += v[i];
		}
	}
	if (sold > ans)
		return;
	sum /= 2;
	bool dp[MAXN * MAXN] = {false};
	dp[0] = true;
	for (int i = 0; i < num; i++)
	{
		for (int j = sum - v[i]; j >= 0; j--)
		{
			if (dp[j] == true)
			{
				dp[j + v[i]] = true; 
			}
		}
		if (dp[sum])
		{
			break;
		}
	}
	if (dp[sum])
	{
		ans = sold;
	}
}

void dfs(int step, int sum)
{
	if (step == n)
	{
		if ((tot - sum) % 2 == 0)
		{
			check(sum);
		}
		return;
	}
	used[step] = true;
	dfs(step + 1, sum + v[step]);
	used[step] = false;
	dfs(step + 1, sum);
}
int main()
{
	int sum = 1;
	for (int i = 1; i <= 16; i++)
	{
		sum *= 3;
	}
	while (scanf("%d", &n) && n)
	{
		tot = 0;
		for (int i = 0; i < n; i++)
		{
			scanf("%d", &v[i]);
			v[i] /= 1000000;
			tot += v[i];
		}
		ans = 700;
		dfs(0, 0);
		printf("%d\n", ans * 1000000);
	}
	//system("pause");
	return 0;
}
*/
/*
#include <cmath>
#include <iostream>
using namespace std;

struct P
{
	double x, y;
};
P c[60], v[60];
double dis[60];

inline double dist(P a, P b)
{
	return sqrt((a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y));
}

int main()
{
	int t, n, m;
	scanf("%d", &t);
	while (t--)
	{
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; i++)
		{
			scanf("%lf%lf", &c[i].x, &c[i].y);
		}
		for (int i = 0; i < m;i++)
		{
			dis[i] = 0;
			scanf("%lf%lf", &v[i].x, &v[i].y);
		}

		double temp;
		for (int i = 0; i < m; i++)
		{
			for (int j = 0; j < n; j++)
			{
				temp = dist(v[i], c[j]);
				if (dis[i] == 0 || (temp < dis[i]))
					dis[i] = temp;
			}
		}

		double ans = 0, Min = 10000000, set[60];
		int pos;
		memcpy(set, dis, sizeof(dis));
		bool used[60] = {false};
		
		for (int i = 0; i < m; i++)
		{
			Min = 10000000;
			for (int j = 0; j < m; j++)
			{
				if (!used[j] && set[j] < Min)
				{
					Min = set[j];
					pos = j;
				}
			}
			used[pos] = true;
			if (Min >= dis[pos])
				ans += dis[pos];
			else
				ans += Min;
			for (int j = 0; j < m; j++)
			{
				if (!used[j] && (temp = dist(v[pos], v[j])) < set[j])
					set[j] = temp;
			}

		}
		printf("%.4lf\n", ans);
	}
	system("pause");
	return 0;
}
*/

/*
#include <iostream>
using namespace std;

const int MAXN = 20;
int v[MAXN], ans, s1, s2, s3, tot, n, end;
//每一个元素有三种可能的情况，属于s1 或者 属于s2 或者 属于s3
void dfs(int step)
{
	if (step == n)
	{
		if (s1 == s2 && s3 < ans)
			ans = s3;
		return;
	}
	
	if (s1 > end || s2 > end)
		return;

	s1 += v[step];
	dfs(step + 1);
	s1 -= v[step];

	s2 += v[step];
	dfs(step + 1);
	s2 -= v[step];
	
	if (s3 + v[step] < ans)
	{
		s3 += v[step];
		dfs(step + 1);
		s3 -= v[step];
	}
}
int main()
{
	while (scanf("%d", &n) && n)
	{
		tot = 0;
		for (int i = 0; i < n; i++)
		{
			scanf("%d", &v[i]);
			tot += v[i];
		}
		end = tot / 2;
		s1 = 0, s2 = 0, s3 = 0, ans = 2000000000;
		dfs(0);
		printf("%d\n", ans);
	}
	system("pause");
	return 0;
}
*/
/*
#include <iostream>
using namespace std;

char str[1000010];
int main()
{
	int len, i = 0, count, precount;
	char ch;
	bool st;
	while ((str[i] = getchar()) != EOF)
	{
		if (str[i] == '\n')
		{
			st = false;
			len = i;
			count = 1;
			precount = -1;
			ch = str[0];
			for (i = 1; i < len; i++)
			{
				if (str[i] == str[i - 1])
				{
					count++;
					if (count == 9)
					{
						printf("9%c", ch);
						count = 0;
					}
				}
				else
				{
					if (count == 1)
					{
						if (ch == '1')
							printf("1");
						if (st == false)
						{
							st = true;
							printf("1%c", ch);
						}
						else
							printf("%c", ch);
					}
					else
					{
						if (precount == 1)
						{
							printf("1%d%c", count, ch);
							st = false;
						}
						else
							printf("%d%c", count, ch);
					}
					ch = str[i];
					precount = count;
					count = 1;
				}
			}
			if (count == 1)
			{
				if (st == false)
					printf("1");
				if (ch == '1')
					printf("1");
				printf("%c1\n",ch);
			}
			else
			{
				if (precount == 1)
					printf("1%d%c\n", count, ch);
				else
					printf("%d%c\n", count, ch);
			}
			i = 0;
		}
		else
			i++;
	}
	return 0;
}
*/
/*
#include <iostream>
using namespace std;

const int MAXN = 1000010;

struct HeapElement
{
	int score, index;
};
HeapElement A[MAXN], B[MAXN];

int num1, num2;
bool used[MAXN];

inline void Swap(HeapElement &a, HeapElement &b)
{
	int temp;
	
	temp = b.index;
	b.index = a.index;
	a.index = temp;
	temp = b.score;
	b.score = a.score;
	a.score = temp;
}

void MaxHeap(int index)
{
	int l = 2 * index, r = 2 * index + 1, largest;
	
	if (l <= num1 && A[l].score > A[index].score)
		largest = l;
	else 
		largest = index;
	
	if (r <= num1 && A[r].score > A[largest].score)
		largest = r;

	if (largest != index)
	{
		Swap(A[index], A[largest]);
		MaxHeap(largest);
	}
}

HeapElement GetMax()
{
	HeapElement Max = A[1];
	A[1] = A[num1];
	num1 = num1 - 1;
	MaxHeap(1);
	return Max;
}

void MaxHeapInsert(HeapElement key)
{
	A[++num1] = key;
	int index = num1;
	while (index > 1 && A[index / 2].score < A[index].score)
	{
		Swap(A[index / 2], A[index]);
		index = index / 2;
	}
}

void MinHeap(int index)
{
	int l = 2 * index, r = 2 * index + 1, smallest;
	if (l <= num2 && B[index].score > B[l].score)
		smallest = l;
	else
		smallest = index;

	if (r <= num2 && B[r].score < B[smallest].score)
		smallest = r;

	if (smallest != index)
	{
		Swap(B[smallest], B[index]);
		MinHeap(smallest);
	}
}

HeapElement GetMin()
{
	HeapElement Min = B[1];
	B[1] = B[num2];
	num2 = num2 - 1;
	MinHeap(1);
	return Min;
}

void MinHeapInsert(HeapElement key)
{
	B[++num2] = key;
	int index = num2;
	while (index > 1 && B[index / 2].score > B[index].score)
	{
		Swap(B[index / 2], B[index]);
		index = index / 2;
	}
}

int main()
{
	int n, score, count = 0;
	char str[10];
	HeapElement temp;
	
	num1 = 0, num2 = 0;
	memset(used, false, sizeof(used));

	scanf("%d", &n);
	while (n--)
	{
		scanf("%s", str);
		if (str[0] == 'p')
		{
			scanf("%d", &score);
			temp.index = ++count;
			temp.score = score;
			MaxHeapInsert(temp);
			MinHeapInsert(temp);
			continue;
		}
		if (num1 == 0 || num2 == 0)
		{
			printf("-1\n");
			continue;
		}
		if (str[0] == 'e')
		{
			temp = GetMax();
			while (used[temp.index] && num1 > 0)
			{
				temp = GetMax();
			}
			if (used[temp.index])
			{
				printf("-1\n");
				continue;
			}
			printf("%d\n", temp.score);
			used[temp.index] = true;
			continue;
		}
		if (str[0] == 't')
		{
			temp = GetMin();
			while (used[temp.index] && num2 > 0)
			{
				temp = GetMin();
			}
			if (used[temp.index])
			{
				printf("-1\n");
				continue;
			}
			printf("%d\n",  temp.score);
			used[temp.index] = true;
			continue;
		}
	}
	return 0;
}
*/

/*
void GetM()
{
	return A[1];
}

void MaxHeap(int index)
{
	int l = 2 * index, r = 2 * index + 1, largest;
	
	if (l <= num && A[l] > A[index])
		largest = l;
	else 
		largest = index;
	if (r <= num && A[r] > A[largest])
		largest = r;

	if (largest != index)
	{
		swap(A[index], A[largest]);
		MaxHeap(largest);
	}
}

void MaxHeapInsert(int key)
{
	A[++num] = key;
	
	int index = num;
	while (index > 1 && A[index / 2] < A[index])
	{
		swap(A[index / 2], A[index]);
		index = index / 2;
	}
}

void MaxHeapDel(int pos)
{
}


void MinHeapInsert(int key)
{
	A[++num] = key;
	
	int index = num;
	while (index > 1 && A[index / 2] > A[index])
	{
		swap(A[index / 2], A[index]);
		index = index / 2;
	}
}

int MinHeap(int index)
{
	int l = 2 * index, r = 2 * index + 1, smallest;
	if (l <= num && A[index] > A[l])
		smallest = l;
	else
		smallest = index;

	if (r <= num && A[r] < A[smallest])
		smallest = r;

	if (smallest != index)
	{
		swap(A[smallest], A[index]);
		MinHeap(smallest);
	}
}
void MinHeapDel(int pos)
{
}
*/
/*
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
using namespace std;

typedef long long ll;
const ll mod = 1000000007ll;
map<ll, int>m;

int count(int b1, int q1, int n1, int b2, int q2, int n2)
{
	ll temp = ll(b1) % mod;
	m[temp]++;
	for (int i = 1; i < n1; i++)
	{
		temp *= ll(q1);
		m[temp %= mod]++;
	}

	temp = ll(b2) % mod;
	m[temp]++;
	for (int i = 1; i < n2; i++)
	{
		temp *= ll(q2);
		m[temp %= mod]++;
	}
	return m.size();
}

int main()
{
	int b1, q1, n1, b2, q2, n2;
	while (cin >> b1 >> q1 >> n1 >> b2 >> q2 >> n2)
	{
		m.clear();
		cout << count(b1, q1, n1, b2, q2, n2) << endl;
	}
	return 0;
}
*/
/*
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <string.h>
#include <cstring>
#include <iostream>
using namespace std;

typedef long long ll;
ll num[110][40];
ll dp[110][2];
int L[110];
int H[110];

int main()
{
	int t, n, l, h, sum = 0;
	
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
	{
		scanf("%d", &n);
		memset(num, 0, sizeof(num));
		memset(dp, 0, sizeof(dp));

		for (int j = 1; j <= n; j++)
		{
			scanf("%d%d", &L[j], &H[j]);
			
			l = L[j] - 1, h = H[j], sum = 0;
			for (int k = 30; k >= 0; k--)
			{
				num[j][k] += sum;
				if (l & (1 << k))
				{
					l ^= (1 << k);
					num[j][k] += (l + 1);
					if (k)
					{
						sum += (1 << (k - 1));
					}
				}
				num[j][k] = -num[j][k];
			}
			
			sum = 0;
			for (int k = 30; k >= 0; k--)
			{
				num[j][k] += sum;
				if (h & (1 << k))
				{
					h ^= (1 << k);
					num[j][k] += (h + 1);
					if (k)
					{
						sum += (1 << (k - 1));
					}
				}
			}
		}
		long long ans = 0;
		for (int k = 0; k <= 30; k++)
		{
			memset(dp, 0, sizeof(dp));
			dp[1][0] = H[1] - L[1] + 1 - num[1][k];
			dp[1][1] = num[1][k];
			for (int i = 2; i <= n; i++)
			{
				dp[i][0] = (H[i] - L[i] + 1 - num[i][k]) * dp[i - 1][0] + num[i][k] * dp[i - 1][1];
				dp[i][1] = num[i][k] * dp[i - 1][0] + (H[i] - L[i] + 1 - num[i][k]) * dp[i - 1][1];
				dp[i][0] %= 1000000007;
				dp[i][1] %= 1000000007;
			}
			ans += dp[n][1] * (1 << k);
			if (ans >= 1000000007)
			{
				ans %= 1000000007;
			}
		}
		printf("Case #%d: ", i);
		printf("%lld\n", ans);
	}
	system("pause");
	return 0;
}
*/

//problem 1455
/*
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <cstring>
#include <string.h>
#include <iostream>

using namespace std;

int wmax[100010];
int p[100010];
int res[100010];

void init()
{
	p[0] = 1;
	for (int i = 1; i <= 90000; i++)
		p[i] = (p[i - 1] * 2) % 1000000007;
	for (int i = 2; i <= 90000; i++)
		wmax[i] = i / 2 * (i - i / 2);
}
int GetMinLen(int w)
{
	int l = 2, r = 80000, mid, ans = 100000;
	while (l <= r)
	{
		mid = (l + r) / 2;
		
		if (wmax[mid] < w)
			l = mid + 1;
		else
		{
			if (ans > mid)
				ans = mid;
			r = mid - 1;
		}
	}
	return ans;
}



int GetAns(int n, int w)
{
	int ans = 0, cnt = 0;
	while (w)
	{
		while (wmax[n] >= w)
			n--;
		ans += p[cnt + n];
		ans %= 1000000007;
		w -= n;
		n--;
		cnt++;
	}
	return ans;
}

int main()
{
	int t, n, w;
	int ans;
	init();
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
	{
		scanf("%d", &w);
		n = GetMinLen(w);
		ans = GetAns(n, w);
		printf("Case #%d: %d\n",i, ans);
	}
	//system("pause");
	return 0;
}
*/
//1447
/*
#include <cmath>
#include <cstdio>
#include <string>
#include <cstdlib>
#include <cstring>
#include <string.h>
#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
	
	return 0;
}
*/
/*
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string.h>
using namespace std;

const int MAXN = 200010;
int couple[MAXN];
int seq[MAXN];
bool used[MAXN];
int main()
{
	int n, a, b, num, count;
	bool NO;
	while (scanf("%d", &n) && n)
	{
		memset(used, false, sizeof(used));
		for (int i = 1; i <= n; i++)
		{
			scanf("%d%d", &a, &b);
			couple[a] = b;
			couple[b] = a;
		}
		count = 0;
		n *= 2;
		while (1)
		{
			num = 0;
			for (int i = 1; i <= n; i++)
			{
				if (!used[i])
				{
					seq[++num] = i;
				}
			}
			NO = true;
			for (int i = 1; i < num; i++)
			{
				if (couple[seq[i]] == seq[i + 1])
				{
					count++;
					used[seq[i]] = used[seq[i + 1]] = true;
					NO = false;
				}
			}
			if (num != 2 && couple[seq[num]] == seq[1])
			{
				count++;
				used[seq[num]] = used[seq[1]] = true;
				NO = false;
			}
			if (count == n / 2)
			{
				printf("Yes\n");
				break;
			}
			if (NO)
			{
				printf("No\n");
				break;
			}
		}
	}
	return 0;
}
*/
//栈模拟
/*
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <stdio.h>
#include <string.h>
using namespace std;

const int MAXN = 200010;
int couple[MAXN];
int stack[MAXN];

int main()
{
	int n, a, b, ptr;
	while (scanf("%d", &n) && n)
	{
		for (int i = 1; i <= n; i++)
		{
			scanf("%d%d", &a, &b);
			couple[a] = b;
			couple[b] = a;
		}

		ptr = -1, n *= 2;
		for (int i = 1; i <= n;i++)
		{
			if (ptr == -1 || stack[ptr] != couple[i])
				stack[++ptr] = i;
			else
				--ptr;
		}

		if (ptr == -1)
			printf("Yes\n");
		else
			printf("No\n");
	}
	return 0;
}
*/
//poj 3171
/*
#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <stdio.h>
#include <string.h>
using namespace std;

typedef long long ll;
const int MAXN = 100010;
const int MAXS = 87000;
const ll MAXV = 1LL << 60;

ll dp[MAXS];

struct Time
{
	int begin, end;
	ll salary;

	bool operator< (Time t)
	{
		if (begin != t.begin)
		{
			return begin < t.begin;
		}
		return end < t.end;
	}
};
Time seg[MAXN];

struct Node
{
	int l, r;
	ll MinValue;
};
Node tree[4 * MAXS];

void BuildTree(int s, int l, int r)
{
	tree[s].l = l;
	tree[s].r = r;
	tree[s].MinValue = MAXV;
	
	if (l == r)
		return;
	int mid = ((l + r) >> 1);
	BuildTree(2 * s, l, mid);
	BuildTree(2 * s + 1, mid + 1, r);
}

void Update(int s, int l, int r, ll v)
{
	tree[s].MinValue = min(tree[s].MinValue, v);//重点的一步。
	if (tree[s].l == l && tree[s].r == r)
	{
		return;
	}

	int mid = (tree[s].l + tree[s].r) >> 1;
	if (mid >= r)
	{
		Update(2 * s, l, r, v);
	}
	else
	{
		if (mid < l)
		{
			Update(2 * s + 1, l, r, v);
		}
		else
		{
			Update(2 * s, l, mid, v);
			Update(2 * s + 1, mid + 1, r, v);
		}
	}
}

ll Query(int s, int l, int r)
{
	if (tree[s].l == l && tree[s].r == r)
	{
		return tree[s].MinValue;
	}
	int mid = (tree[s].l + tree[s].r) >> 1;
	if (mid >= r)
	{
		return Query(2 * s, l, r);
	}
	else
	{
		if (mid < l)
		{
			return Query(2 * s + 1, l, r);
		}
		else
		{
			return min(Query(2 * s, l, mid), Query(2 * s + 1, mid + 1, r));
		}
	}
}

int main()
{
	int n, m, e, right;
	
	scanf("%d%d%d", &n, &m, &e);
	right = e;
	for (int i = 0; i < n; i++)
	{
		scanf("%d%d%I64d", &seg[i].begin, &seg[i].end, &seg[i].salary);
		if (seg[i].end > right)
			right = seg[i].end;
	}

	BuildTree(1, m, right);
	sort(seg, seg + n);
	fill(dp, dp + right + 1, MAXV);
	int j;
	for (j = 0; j < n; j++)
	{
		if (seg[j].begin <= m)
		{
			dp[seg[j].end] = min(dp[seg[j].end], seg[j].salary);
			Update(1, seg[j].end ,seg[j].end, seg[j].salary);
		}
		else
		{
			break;
		}
	}
	for (j; j < n; j++)
	{
		dp[seg[j].end] = min(dp[seg[j].end], Query(1, seg[j].begin - 1, seg[j].end) + seg[j].salary);
		Update(1, seg[j].end, seg[j].end, dp[seg[j].end]);
	}
	
	ll ans = MAXV;
	for (j = 0; j < n; j++)
	{
		if (seg[j].end < e)
			continue;
		ans = min(ans, dp[seg[j].end]);
	}
	if (ans == MAXV)
	{
		printf("-1\n");
	}
	else
	{
		printf("%I64d\n", ans);
	}
	system("pause");
	return 0;
}
*/
//poj 3170
/*
#include <iostream>
#include <stdio.h>
#include <cstdio>
#include <cstdlib>
#include <string.h>
#include <string>
using namespace std;

int main()
{
	return 0;
}
*/
//H
/*
#include <map>
#include <algorithm>
#include <iostream>
#include <string>
using namespace std;

const int MAXN = 310;
int a[MAXN][MAXN];
int num[MAXN], q[3 *MAXN];

int main()
{
	int n, count = 0;
	char name1[MAXN];
	char name2[MAXN];
	char name3[MAXN];
	map<string, int>m;
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
			scanf("%s%s%s", name1, name2, name3);
			if (m[name1] == 0)
			{
				m[name1] = ++count;
			}
			if (m[name2] == 0)
			{
				m[name2] = ++count;
			}
			if (m[name3] == 0)
			{
				m[name3] = ++count;
			}
			int t1 = m[name1], t2 = m[name2], t3 = m[name3];
			a[t1][++a[t1][0]] = t2;
			a[t1][++a[t1][0]] = t3;
			a[t2][++a[t2][0]] = t1;
			a[t2][++a[t2][0]] = t3;
			a[t3][++a[t3][0]] = t1;
			a[t3][++a[t3][0]] = t2;
	}
	memset(num, -1, sizeof(num));
	if (m.find("Isenbaev") != m.end())
	{
		int temp = m["Isenbaev"];
		int head = 0, tail = 0;
		q[head++] = temp;
		num[temp] = 0;
		while (tail < head)
		{
			int cur = q[tail];
			for (int i = 1; i <= a[cur][0]; i++)
			{
				if (num[a[cur][i]] == -1)
				{
					num[a[cur][i]] = num[cur] + 1;
					q[head++] = a[cur][i];
				}
			}
			tail++;
		}
	}
	map<string, int>::iterator it1 = m.begin();
	map<string, int>::iterator it2 = m.end();
	for (it1; it1 != it2; it1++)
	{
		cout << it1->first << " ";
		if (num[it1->second] == -1)
		{
			printf("undefined\n");
		}
		else
			printf("%d\n", num[it1->second]);
	}
	system("pause");
}
*/
/*
#include <cstdio>
#include <stdio.h>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <string.h>
#include <string>
using namespace std;

const int MAXN = 3000;
const int MAXM = 40010;

struct per
{
	int Min, Max;
};
per p[MAXN];
bool comp(per A, per B)
{
	if (A.Max != B.Max)
	{
		return A.Max < B.Max;
	}
	else
	{
		return A.Min < B.Min;
	}
}

int w[MAXM];
bool used[MAXN];

int main()
{
	int n, m, count;
	while (scanf("%d%d", &n, &m) != EOF)
	{
		memset(used, false, sizeof(used));
		for (int i = 0; i < n; i++)
		{
			scanf("%d%d", &p[i].Min, &p[i].Max);
		}
		sort(p, p + n, comp);
		for (int i = 0; i < m; i++)
		{
			scanf("%d", &w[i]);
		}
		sort(w, w + m);
		int temp = 0;
		count = 0;
		for (int i = 0; i < n && temp != m;)
		{
			if (used[i])
			{
				i++;
				continue;
			}
			if (w[temp] < p[i].Min)
			{
				int j;
				for (j = i + 1; j < n; j++)
				{
					if (!used[j] && p[j].Min <= w[temp])
					{
						used[j] = true;
						temp++;
						count++;
						break;
					}
				}
				if (j == n)
				{
					temp++;
				}
				continue;
			}
			if (w[temp] > p[i].Max)
			{
				i++;
				continue;
			}
			i++;
			temp++;
			count++;
		}
		printf("%d\n", count);
	}
	return 0;
}
*/
//zoj problem 3502
//转化，状态压缩DP， 用string记录路径。。
/*
#include <iostream>
#include <cstdio>
#include <stdio.h>
#include <cstdlib>
#include <string>
#include <string.h>
#include <algorithm>
using namespace std;

const int MAXN = (1 << 12) - 1;
int dp[MAXN][20];
int p[20][20];
string path[MAXN][20];

int main()
{
	int t, n, Max;
	while (scanf("%d", &t) != EOF)
	{
		while (t--)
		{
			scanf("%d", &n);
			for (int i = 0; i < n; i++)
			{
				for (int j = 0; j < n; j++)
				{
					scanf("%d", &p[i][j]);
				}
			}
			memset(dp, -1, sizeof(dp));
			int end = (1 << n) - 1;
			dp[0][0] = 0;
			for (int i = 0; i <= end; i++)
			{
				for (int j = 0; j < n; j++)
				{
					path[i][j] = "";
				}
			}
			for (int i = 0; i <= end; i++)
			{
				for (int j = 0; j < n; j++)
				{
					if (dp[i][j] == -1 || ((i & (1 << j)) == 0 && i * i + j * j != 0))
						continue;
					
					for (int k = 0; k < n; k++)
					{
						if (i & (1 << k))
						{
							continue;
						}
						Max = p[k][k];
						for (int m = 0; m < n; m++)
						{
							if (i & (1 << m))
							{
								Max = max(Max, p[m][k]);
							}
						}
						if (dp[i | (1 << k)][k] < dp[i][j] + Max)
						{ 
							dp[i | (1 << k)][k] = dp[i][j] + Max;
							path[i | (1 << k)][k] = path[i][j] + char('A' + k);
						}
						else
						{
							if (dp[i | (1 << k)][k] == dp[i][j] + Max)
							{
								string temp = path[i][j] + char('A' + k);
								if (temp < path[i | (1 << k)][k])
								{
									path[i | (1 << k)][k] = temp; 
								}
							}
						}
					}
				}
			}
			int pos = 0;
			for (int i = 1; i < n; i++)
			{
				if (dp[end][i] > dp[end][pos] || dp[end][i] == dp[end][pos] && path[end][i] < path[end][pos])
				{
					pos = i;
				}
			}
			printf("%.2lf\n", double(dp[end][pos]) / 100.0);
			cout << path[end][pos] << endl;
		}
	}
	return 0;
}
*/
/*
#include <ctime>
#include <cstdlib>
#include <iostream>
using namespace std;

int main()
{
	int t = 10;
	srand(time(0));
	freopen("mytest.txt", "w", stdout);
	for (int i = 2; i <= 10; i++)
	{
		cout << 7 << endl;
		for (int j = 1; j <= 7; j++)
		{
			for (int k = 1; k <= 7;k++)
			{
				if (k == j)
					cout << 0 << " ";
				else
					cout << rand() % 10001 << " ";
			}
			cout << endl;
		}
	}
	return 0;
}
*/
/*
#include <cstdio>
#include <stdio.h>
#include <cstdlib>
#include <string>
#include <string.h>
#include <iostream>
using namespace std;

const int MAXN = (1 << 10);
int dp[MAXN][11];
int p[11][11];

int main()
{
	int n;
	freopen("mytest.txt", "r", stdin);
	freopen("ans1.txt", "w", stdout);
	while (scanf("%d", &n) && n)
	{
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				scanf("%d", &p[i][j]);
			}
		}
		memset(dp, -1, sizeof(dp));
		for (int i = 0; i < n; i++)
		{
			dp[1 << i][i] = 0;
		}
		int end = (1 << n) - 1;
		for (int i = 0; i <= end; i++)
		{
			for (int j = 0; j < n; j++)
			{
				if (dp[i][j] == -1 || (i & (1 << j)) == 0)
					continue;
				for (int k = 0; k < n; k++)
				{
					if (i & (1 << k))
						continue;
					if (dp[i | (1 << k)][k] < dp[i][j] + p[k][j])
					{
						dp[i | (1 << k)][k] = dp[i][j] + p[k][j];
					}
				}
			}
		}
		int ans = 0;
		for (int i = 0; i < n; i++)
		{
			if (dp[end][i] > ans)
			{
				ans = dp[end][i];
			}
		}
		printf("%d\n", ans);
	}
	return 0;
}
*/
/*
#include <cstdio>
#include <stdio.h>
#include <cstdlib>
#include <string>
#include <string.h>
#include <iostream>
using namespace std;

const int MAXN = 1 << 10;
int dp[MAXN];
int p[11][11];

int main()
{
	int n;
	//freopen("mytest.txt", "r", stdin);
	//freopen("ans3.txt", "w", stdout);
	while (scanf("%d", &n) && n)
	{
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				scanf("%d", &p[i][j]);
			}
		}
		memset(dp, 0, sizeof(dp));
		int end = (1 << n) - 1;
		for (int i = 0; i <= end; i++)
		{
			for (int j = 0; j < n; j++)
			{
				if ((i & (1 << j)) == 0)
					continue;
				for (int k = 0; k < n; k++)
				{
					if ((1 << k) & i)
						continue;
					dp[i | (1 << k)] = max(dp[i | (1 << k)], dp[i] + p[j][k]);
				}
			}
		}
		printf("%d\n", dp[end]);
	}
}
*/
/*
#include <iostream>
#include <cstdio>
#include <stdio.h>
#include <cstdlib>
#include <string>
#include <string.h>
using namespace std;

const int MAXN = 100010;
int dp[MAXN][20];
int a[MAXN];
int n, m;

void RMQ()
{
}

int main()
{
	scanf("%d%d", &n, &m);
	for (int i = 0; i < n; i++)
	{
		scanf("%d", &a[i]);
	}
	RMQ();
	int head, tail;

}
*/
/*
#include <iostream>
using namespace std;

int main()
{
	char *s;
	s = new char[10];
	for (int i = 0; i < 5; i++)
	{
		cin >> s[i];
	}
	s[5] = '\0';
	cout << *(s + 1) << endl;
	system("pause");
	return 0;
}
*/
//zoj problem 3505
/*
#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;

int n;
long long k;
long long num[30];
char str[30];
char ans[30];
void init()
{
	num[0] = 0;
	num[1] = 3;
	for (int i = 2; i <= 20; i++)
	{
		num[i] = num[i - 1] * 3;
	}
	for (int i = 2; i <= 20; i++)
	{
		num[i] += num[i - 1];
	}
}

long long GetId(int nu, char s, char *st)
{
	if (*st == '\0')
		return 0;
	long long m = 1;
	for (char temp = '0'; temp < *st; temp++)
	{
		if (temp == s)
			continue;
		m += (num[nu - 1] + 1);
	}
	//cout << m << " " << nu << " " << *st << endl;
	m += GetId(nu - 1, *st, st + 1);
	return m;
}

void StrId(int nu, long long m , char s, char a[])
{
	if (m == 0)
	{
		a[n - nu] = '\0'; 
		return;
	}
	--m;
	for (char t = '0'; ; ++t)
	{
		if (t == s)
			continue;
		if (m >= num[nu - 1] + 1)
		{
			m -= (num[nu - 1] + 1);
		}
		else
		{
			a[n - nu] = t;
			StrId(nu - 1, m, a[n - nu], a);
			break;
		}
	}
}

int main()
{
	init();
	while (scanf("%d%lld%s", &n, &k, str) != EOF)
	{
		k = GetId(n, '0', str) - k;
		//cout << k << endl;
		StrId(n, k, '0', ans);
		int i = 0;
		while (ans[i] == '0')
			i++;
		while (ans[i] != '\0')
		{
			printf("%c", ans[i]);
			i++;
		}
		printf("\n");
	}
	return 0;
}
*/
/*
#include <stdio.h>
#include <stdlib.h>
#include <cstring>
#include <string>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string.h>
using namespace std;

const int MAX = 1000010;
const int MAXN = 1010;

int n, k, edgenum,v[MAXN],num[MAXN],Link[MAXN], dp[MAXN][30];
bool used[MAXN];
struct Edge
{
	int v, next;
};
Edge tree[MAXN];

void init()
{
	edgenum = 0;
	memset(num, 0, sizeof(num));
	memset(used, false, sizeof(used));
	memset(Link, -1, sizeof(Link));
}

void addEdge(int u, int v)
{
	edgenum++;
	tree[edgenum].v = v;
	tree[edgenum].next = Link[u];
	Link[u] = edgenum;
	edgenum++;
	tree[edgenum].v = u;
	tree[edgenum].next = Link[v];
	Link[v] = edgenum;
}

void DP(int root)
{
	used[root] = true;
	num[root] = 1;
	fill(dp[root], dp[root] + k + 1, MAX);
	dp[root][0] = 0;
	int MIN = MAX;
	for (int i = Link[root]; i != -1; i = tree[i].next)
	{
		if (!used[tree[i].v])
		{
			DP(tree[i].v);
			num[root] += num[tree[i].v];
			for (int j = k; j >= 1; j--)
			{
				MIN = MAX;
				for (int p = 0; p <= j; p++)//不能在中间就修改dp[root][j]的值，要全部找完才能更新
				{
			
					MIN = min(MIN, dp[root][p] + dp[tree[i].v][j - p]);
				}
				for (int p = 1; p <= j && p <= num[tree[i].v]; p++)
				{
					MIN = min(MIN, dp[root][j - p]);
				}
				dp[root][j] = MIN;
			}
			dp[root][0] += dp[tree[i].v][0];
		}
	}
	for (int i = 0; i <= k; i++)
	{
		dp[root][i] += v[root];
	}
}

int GetAns()
{
	//for (int i = 1; i <= n; i++)
	//{
	//	for (int j = 0; j <= k; j++)
	//	{
	//		cout << "dp[" << i << "][" << j << "] = " << dp[i][j] << " ";
	//	}
	//	cout << endl;
	//}
	int ans = dp[1][k];
	for (int i = 2; i <= n; i++)
	{
		for (int j = 1; j <= min(n - num[i], k); j++)
		{
			if (dp[i][k - j] < ans)
				ans = dp[i][k - j];
		}
	}
	return ans;
}

int main()
{
	int a, b;
	while (scanf("%d%d", &n, &k) != EOF)
	{
		init();
		for (int i = 1; i <= n; i++)
		{
			scanf("%d", &v[i]);
		}
		for (int i = 1; i < n; i++)
		{
			scanf("%d%d", &a, &b);
			addEdge(a, b);
		}

		DP(1);
		printf("%d ", GetAns());
		for (int i = 1; i <= n; i++)
		{
			v[i] = -v[i];
		}
		memset(used, false, sizeof(used));
		memset(num , 0, sizeof(num));
		DP(1);
		printf("%d\n", -GetAns());
	}
	return 0;
}
*/
/*
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
	int n, k;
	vector<int>a;
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		cin >> k;
		a.push_back(k);
	}
	cin >> k;
	cout << *upper_bound(a.begin(), a.end(), k) << " " << *lower_bound(a.begin(), a.end(), k) << endl;;
	system("pause");
	return 0;
}
*/
/*
#include <string.h>
#include <iostream>
#include <queue>
#include <cstdio>
using namespace std;

const int MAXN = 10010;

bool IsPrime[MAXN];
void init()
{
	memset(IsPrime, true, sizeof(IsPrime));
	IsPrime[1] = false;
	for (int i = 2; i <= 10000; i++)
	{
		if (IsPrime[i])
		{
			for (int j = i + i; j <= 10000; j += i)
			{
				IsPrime[j] = false;
			}
		}
	}
}

int used[MAXN];
void work(int a, int b)
{
	memset(used, -1, sizeof(used));
	int da[5],cur, temp, c;
	queue<int>q;
	used[a] = 0;
	q.push(a);
	while (!q.empty())
	{
		cur = q.front();
		q.pop();
		da[0] = cur % 10;
		da[1] = cur / 10 % 10;
		da[2] = cur / 100 % 10;
		da[3] = cur / 1000;
		for (int i = 0; i <= 2; i++)
		{
			c = da[i];
			for (int j = 0; j <= 9; j++)
			{
				da[i] = j;
				temp = da[0] + da[1] * 10 + da[2] * 100 + da[3] * 1000;
				if (IsPrime[temp] && used[temp] == -1)
				{
					q.push(temp);
					used[temp] = used[cur] + 1;
				}
			}
			da[i] = c;
		}
		for (int i = 1; i <= 9; i++)
		{
			da[3] = i;
			temp = da[0] + da[1] * 10 + da[2] * 100 + da[3] * 1000;
			if (IsPrime[temp] && used[temp] == -1)
			{
				q.push(temp);
				used[temp] = used[cur] + 1;
			}
		}
		if (used[b] != -1)
			break;
	}
	if (used[b] == -1)
		printf("Impossible\n");
	else
		printf("%d\n", used[b]);
}

int main()
{
	init();
	int Case, a, b;
	scanf("%d", &Case);
	while (Case--)
	{
		scanf("%d%d", &a, &b);
		work(a, b);
	}
	return 0;
}
*/
/*
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string.h>
#include <cmath>
#include <cstdlib>
using namespace std;

const int MAXN = 10010;
const double pi = acos(-1.0);
const double eps = 1e-5;

double area[MAXN];
int main()
{
	int Case,n, f, count;
	double left, right, mid, ans;
	scanf("%d", &Case);
	while (Case--)
	{
		right = 0, count = 0, left = 2000000000.0;
		scanf("%d%d", &n, &f);
		for (int i = 0; i < n; i++)
		{
			scanf("%lf", &area[i]);
			area[i] = pi * area[i] * area[i];
			if (left > area[i] + eps)
				left = area[i];
			right += area[i];
		}
		left = 0, ans = 0;
		while (left + eps < right)
		{
			mid = (left + right) / 2;
			count = 0;
			for (int i = 0; i < n; i++)
			{
				double cur = mid;
				while (cur + eps <= area[i])
				{
					count++;
					cur += mid;
				}
			}
			if (count > f)
			{
				if (ans < mid + eps)
					ans = mid;
				left = mid;
			}
			else
				right = mid;
		}
		printf("%.2lf\n", ans);
	}
	return 0;
}
*/
/*
#include <iostream>
#include <cstdio>
#include <queue>
#include <string.h>
#include <cstdlib>
using namespace std;

const int MAXN = 1010;

int r, c,dir[8][2] = {{-1, 0}, {-1, 1}, {0, 1}, {1, 1}, {1, 0}, {1, -1}, {0, -1}, {-1, -1}};
char map[MAXN][MAXN];
int used[MAXN][MAXN];

struct Node
{
	int x, y, step;
	friend bool operator<(Node A, Node B)
	{
		return A.step > B.step;
	}
};
priority_queue<Node>q;
int search(int sx, int sy, int ex, int ey)
{
	while (!q.empty())
	{
		q.pop();
	}
	Node e;
	e.x = sx;
	e.y = sy;
	e.step = 0;
	memset(used, -1, sizeof(used));
	q.push(e);
	used[sx][sy] = 0;
	while (!q.empty())
	{
		int curx = q.top().x;
		int cury = q.top().y;
		int curs = q.top().step;
		q.pop();
		for (int i = 0; i < 8; i++)
		{
			e.x = curx + dir[i][0];
			e.y = cury + dir[i][1];
			if (e.x >= 0 && e.y >= 0 && e.x < r && e.y < c && used[e.x][e.y] == -1)
			{
				if (i == map[curx][cury] - '0')
				{
					e.step = curs;
					used[e.x][e.y] = e.step;
				}
				else
				{
					e.step = curs + 1;
					used[e.x][e.y] = e.step;
				}
				q.push(e);
			}
		}
		if (used[ex][ey] != -1)
			return used[ex][ey];
	}
}
int main()
{
	int n, sx, sy, ex,ey;
	freopen("test.txt", "r", stdin);
	freopen("ans.txt", "w", stdout);
	scanf("%d%d", &r, &c);
	for (int i = 0; i < r; i++)
	{
		getchar();
		for (int j = 0; j < c; j++)
		{
			scanf("%c", &map[i][j]);
		}
	}
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		scanf("%d%d%d%d", &sx, &sy, &ex, &ey);
		printf("%d\n", search(sx - 1, sy - 1, ex - 1, ey - 1));
	}	
	return 0;
}
*/
/*
#include <iostream>
#include <ctime>
using namespace std;

int main()
{
	freopen("test.txt", "w", stdout);
	srand(time(0));
	for (int i = 0; i <= 2; i++)
	{
		cout << 50 << " " << 50 << endl;
		for (int i = 0; i < 50; i++)
		{
			for (int j = 0; j < 50; j++)
			{
				cout << rand() % 8;
			}
			cout << endl;
		}
		cout << 50;
		for (int i = 0; i < 50; i++)
		{
			cout << rand() % 50 + 1 << " " << rand() % 50 + 1 << " " << rand() % 50 + 1 << " " << rand() % 50 + 1 << endl;
		}
	}
	return 0;
}
*/
/*
#include <cmath>
#include <iostream>
using namespace std;

const int MAXN = 110;
int a[MAXN], b[MAXN];
int pa[MAXN], pb[MAXN];
int main()
{
	int t, n, pos;
	char ch;
	freopen("A.txt", "r", stdin);
	freopen("A.out", "w", stdout);
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
	{
		scanf("%d", &n);
		a[0] = b[0] = 0;
		for (int j = 0; j < n; j++)
		{
			cin >> ch >> pos;
			if (ch == 'O')
				a[++a[0]] = pos, pa[a[0]] = j;;
			if (ch == 'B')
				b[++b[0]] = pos, pb[b[0]] = j;
		}
		int sa = 1, sb = 1, apos = 1, bpos = 1, count = 0;
		while (sa <= a[0] || sb <= b[0])
		{
			if (sa > a[0])
			{
				count += abs(b[sb] - bpos) + 1;
				bpos = b[sb];
				sb++;
				continue;
			}
			if (sb > b[0])
			{
				count += abs(a[sa] - apos) + 1;
				apos = a[sa];
				sa++;
				continue;
			}
			int Min = min(abs(a[sa] - apos), abs(b[sb] - bpos));
			apos = apos < a[sa] ? (apos + Min) : (apos - Min);
			bpos = bpos < b[sb] ? (bpos + Min) : (bpos - Min);
			count += Min;
			if (apos == a[sa])
			{
				if (pa[sa] < pb[sb])
				{
					count++;
					sa++;
					if (pb[sb] != bpos)
					{
						bpos = bpos < b[sb] ? (bpos + 1) : (bpos - 1);
					}
				}
				else
				{
					count += abs(pb[sb] - bpos) + 2;
					bpos = b[sb];
					sb++;
					bpos = bpos < b[sb] ? (bpos + 1) : (bpos - 1);
					sa++;
				}
				continue;
			}
			if (bpos == b[sb])
			{
				if (pb[sb] < pa[sa])
				{
					count++;
					sb++;
					if (pa[sa] != apos)
					{
						apos = apos < a[sa] ? (apos + 1) : (apos - 1);
					}
				}
				else
				{
					count += abs(pa[sa] - apos) + 2;
					apos = a[sa];
					sa++;
					apos = apos < a[sa] ? (apos + 1) : (apos - 1);
					sb++;
				}
				continue;
			}
		}
		cout << "Case #" << i << ": " << count << endl; 
	}
	//system("pause");
	return 0;
}
*/
/*
#include <cmath>
#include <iostream>
using namespace std;

const int MAXN = 110;
int a[MAXN], b[MAXN];
int pa[MAXN], pb[MAXN];
int main()
{
	int t, n, pos;
	char ch;
	freopen("A.txt", "r", stdin);
	freopen("A.out", "w", stdout);
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
	{
		scanf("%d", &n);
		a[0] = b[0] = 0;
		for (int j = 0; j < n; j++)
		{
			cin >> ch >> pos;
			if (ch == 'O')
				a[++a[0]] = pos, pa[a[0]] = j;;
			if (ch == 'B')
				b[++b[0]] = pos, pb[b[0]] = j;
		}
		int sa = 1, sb = 1, apos = 1, bpos = 1, count = 0;
		while (sa <= a[0] || sb <= b[0])
		{
			if (sa > a[0])
			{
				count += abs(b[sb] - bpos) + 1;
				bpos = b[sb];
				sb++;
				continue;
			}
			if (sb > b[0])
			{
				count += abs(a[sa] - apos) + 1;
				apos = a[sa];
				sa++;
				continue;
			}
			count++;
			if (bpos == b[sb])
			{
				if (pa[sa] > pb[sb])
				{
					sb++;
					if (apos != a[sa])
					{
						apos = apos < a[sa] ? (apos + 1) : (apos - 1);
					}
				}
				else
				{
					if (apos != a[sa])
					{
						apos = apos < a[sa] ? (apos + 1) : (apos - 1);
					}
					else
						sa++;
				}
			}
			else
			{
				bpos = bpos < b[sb] ? (bpos + 1) : (bpos - 1);
				if (pa[sa] > pb[sb])
				{
					if (apos != a[sa])
						apos = apos < a[sa] ? (apos + 1) : (apos - 1);
				}
				else
				{
					if (apos == a[sa])
					{
						sa++;
					}
					else
						apos = apos < a[sa] ? (apos + 1) : (apos - 1);
				}
			}
		}
		cout << "Case #" << i << ": " << count << endl; 
	}
	//system("pause");
	return 0;
}
*/
/*
#include <iostream>
#include <cstdio>
#include <string>
#include <cstdlib>
using namespace std;

bool op[110][110];
char com[110][110];
int main()
{
	int t, c, d, n;
	char in[110];
	bool used[110];
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
	{
		memset(used, false, sizeof(used));
		memset(op, false, sizeof(op));
		for (int p = 0; p <= 100; p++)
		{
			for (int q = 0; q <= 100; q++)
			{
				com[p][q] = ' ';
			}
		}
		scanf("%d", &c);
		for (int j = 0; j < c; j++)
		{
			scanf("%s", in);
			com[in[0] - 'A'][in[1] - 'A'] = in[2];
			com[in[1] - 'A'][in[0] - 'A'] = in[2];
		}
		scanf("%d", &d);
		for (int j = 0; j < d; j++)
		{
			scanf("%s", in);
			op[in[0] - 'A'][in[1] - 'A'] = true;
			op[in[1] - 'A'][in[0] - 'A'] = true;;
		}
		char ans[110];
		int ptr = 0;
		scanf("%d", &n);
		scanf("%s", in);
		ans[0] = in[0];
		ptr++;
		for (int j = 1; j < n; j++)
		{
			if (ptr == 0)
			{
				ans[ptr++] = in[j];
				continue;
			}
			if (com[in[j] - 'A'][ans[ptr - 1] - 'A'] != ' ')
			{
				ans[ptr - 1] = com[in[j] - 'A'][ans[ptr - 1] - 'A'];
				continue;
			}
			for (int k = ptr - 1; k >= 0; k--)
			{
				if (op[ans[k] - 'A'][in[j] - 'A'] == true)
				{
					ptr = 0;
					break;
				}
				if (k == 0)
					ans[ptr++] = in[j];
			}
		}
		cout << "Case #" << i << ": " << "[";
		for (int j = 0; j < ptr - 1; j++)
		{
			cout << ans[j] << ", ";
		}
		if (ptr != 0)
			cout << ans[ptr - 1];
		cout << "]" << endl;
	}
	return 0;
}
*/

#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

const int MAXN = 1010;
int a[MAXN];

int main()
{
	int t, n, temp = 0;
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
	{
		temp = 0;
		scanf("%d", &n);
		for (int j = 0; j < n; j++)
		{
			scanf("%d", &a[j]);
			temp = (temp ^ a[j]);
		}
		cout << "Case #" << i << ": ";
		if (temp != 0)
			cout << "NO" << endl;
		else
		{
			sort(a, a + n);
			temp = 0;
			for (int j = 1; j < n; j++)
				temp += a[j];
			cout << temp << endl;
		}
	}
	//system("pause");
	return 0;
}