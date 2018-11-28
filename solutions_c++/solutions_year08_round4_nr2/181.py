#include <stdio.h>
#include <stdarg.h>
#include <algorithm>
#include <cassert>
#define IS_DEBUG 0

void dgb(const char * fmt, ...)
{
	#if IS_DEBUG
		va_list args;
		va_start(args, fmt);
		vfprintf(stdout, fmt, args);
		va_end(args);
	#endif
}

int N[100000100];
int M[100000100];
int temps[25000000];
int min(int a, int b)
{
	return a < b ? a : b;
}
int max(int a, int b)
{
	return a < b ? b : a;
}

int maxM, lastN, maxN;
int counter;
int tc;
class test_case
{
	public:
		int n,m,s,x1,x2,y1,y2,num;	
	void scan()
	{
		scanf("%d%d%d", &n, &m, &s);
		maxM = max(m,maxM);
		maxN = max(n,maxN);
		x1 = x2 = y1 = y2 = -1;
		num = ++counter;
	}
	bool operator < (const test_case & rhs) const
	{
		return n < rhs.n;
	}
	void solve()
	{
		for(int i = lastN; i <= n; i++)
			for(int j = 0; j <= maxM; j++)
			{
				int tmp = i*j;
				if (M[tmp] > j || M[tmp] == -1)
				{
					M[tmp] = j;
					N[tmp] = i;
					if (M[tmp] == -1)
						temps[tc++] = tmp;
				}
				if (tmp >= s && M[tmp-s] <= m && M[tmp-s] != -1 && j <= m)
				{
					x1 = i;
					y2 = j;
					x2 = N[tmp-s];
					y1 = M[tmp-s];
				}
			}
		for(int i = 0; i < tc; i++)
		{
			if (M[temps[i]] <= m && temps[i] >= s && M[temps[i]-s] >= 0 && M[temps[i]-s] <= m)
			{
				x1 = N[temps[i]];
				x2 = N[temps[i]-s];
				y1 = M[temps[i]];
				y2 = M[temps[i]-s];
			}
		}

		lastN = n;
	}
	void print(int test_num)
	{
		printf ("Case #%d: ", test_num);
		if (x1 == -1)
			printf("IMPOSSIBLE\n");
		else
		{
			printf("0 0 %d %d %d %d\n", x1,y1,x2,y2);
			assert(x1 <= n && x2 <= n && y1 <= m && y2 <= m && x1*y2-x2*y1==s 
				&& x1 >= 0 && x2 >= 0 && y1 >= 0 && y2 >= 0);
		}

	}
};

test_case ar[2000];
test_case res[2000];
void solve()
{
	int n;
	counter = 0;
	tc = 0;
	scanf("%d", &n);
	for(int i = 0; i < n; i++)
		ar[i].scan();
	std::sort(ar, ar+n);
	for(int i = 0; i <= maxM * maxN; i++)
		M[i] = N[i] = -1;
	for(int i = 0; i < n; i++)
		ar[i].solve();
	for(int i = 0; i < n; i++)
		res[ar[i].num] = ar[i];
	for(int i = 1; i <= n; i++)
		res[i].print(i);
	

	
}


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	maxM = lastN = maxN = 0;
	solve();
	return 0;
}