#include <iostream>
#include <fstream>
#include <string>
#include <map>
using namespace std;

int n, k;
int d[110];

void Load()
{
	scanf("%d%d", &k, &n);
	int i;
	for (i = 0; i < n; i++) scanf("%d", &d[i]);
}

const int TSIZE = 1048576;
int sum[2 * TSIZE + 1];
int deck[1100000];

int GetSum(int l, int r)
{
	int res = 0;
	l += TSIZE - 1;
	r += TSIZE - 1;
	while (l <= r)
	{
		if ((l & 1) == 1)
		{
			res += sum[l];
			l++;
		}
		if ((r & 1) == 0)
		{
			res += sum[r];
			r--;
		}
		l >>= 1;
		r >>= 1;
	}
	return res;
}

int FindPos(int pos)
{
	int cur = 1;
	while (cur <= TSIZE - 1)
	{
		if (pos <= sum[cur << 1]) cur <<= 1;
		else
		{
			pos -= sum[cur << 1];
			cur = (cur << 1) + 1;
		}
	}
	return cur - TSIZE + 1;
}

void Solve()
{
	memset(sum, 0, sizeof(sum));
	int i;
	for (i = TSIZE; i <= 2 * TSIZE - 1; i++)
	{
		sum[i] = 1;
	}
	for (i = TSIZE - 1; i >= 1; i--) sum[i] = sum[2 * i] + sum[2 * i + 1];
	int lpos = -1;
	for (i = 1; i <= k; i++)
	{
		int cnum = i;
		if (lpos != -1)
		{
			cnum += GetSum(1, lpos);
		}
		//cerr << "After adding we are to find " << cnum << "\n";
		cnum--;
		cnum %= (k - i + 1);
		cnum++;
		//cerr << "Finding " << cnum << "\n";
		lpos = FindPos(cnum);
		//cerr << "got " << lpos << "\n";
		deck[lpos] = i;
		int cur = lpos;
		cur += TSIZE - 1;
		while (cur > 0) 
		{
			sum[cur]--;
			cur >>= 1;
		}
	}
	for (i = 0; i < n; i++)
	{
		printf("%d ", deck[d[i]]);
	}
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int nt, it;
	scanf("%d", &nt);
	for (it = 0; it < nt; it++)
	{
		cerr << "case " << it << "\n";
		printf("Case #%d: ", it + 1);
		Load();
		Solve();
		printf("\n");
	}
	return 0;
}