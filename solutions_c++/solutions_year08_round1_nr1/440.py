#include <iostream>
#include <string>
using namespace std;

#define INPUTFILENAME "A-large.in.txt"
#define OUTPUTFILENAME "output.txt"

int n;
int a[1000];
int b[1000];

void init()
{
	cin >> n;
	for (int i = 0; i < n; i++)
		cin >> a[i];
	for (int i = 0; i < n; i++)
		cin >> b[i];
}

void qsortA(int l, int r)
{
	if (r - l <= 0) return;
	int i, j;
	i = (l + r) >> 1;
	int mid = a[i];
	i = l; j = r;
	while (i < j)
	{
		while (a[i] < mid) i++;
		while (mid < a[j]) j--;
		if (i <= j)
		{
			int tmp = a[i];
			a[i] = a[j];
			a[j] = tmp;
			i++;
			j--;
		}
	}
	if (l < j) qsortA(l, j);
	if (i < r) qsortA(i, r);
}

void qsortB(int l, int r)
{
	if (r - l <= 0) return;
	int i, j;
	i = (l + r) >> 1;
	int mid = b[i];
	i = l; j = r;
	while (i < j)
	{
		while (b[i] > mid) i++;
		while (mid > b[j]) j--;
		if (i <= j)
		{
			int tmp = b[i];
			b[i] = b[j];
			b[j] = tmp;
			i++;
			j--;
		}
	}
	if (l < j) qsortB(l, j);
	if (i < r) qsortB(i, r);
}

void solve(int testnumber)
{
	qsortA(0, n - 1);
	qsortB(0, n - 1);
	long long ans = 0;
	long long tmp;
	for (int i = 0; i < n; i++)
	{
		tmp = a[i];
		tmp *= b[i];
		ans += tmp;
	}
	cout << "Case #" << testnumber << ": " << ans << endl;
}	

int main()
{
	int testnumber;
	freopen(INPUTFILENAME, "r", stdin);
	freopen(OUTPUTFILENAME, "w", stdout);
	cin >> testnumber;
	for (int i = 0; i < testnumber; i++)
	{
		init();
		solve(i + 1);
	}
	return 0;
}