#include <iostream>
#include <math.h>
using namespace std;

int n, ans;
char chr[1000];
int idx[1000], f[1000];
void init()
{
	cin >> n;
	n += 2;
	chr[0] = 'B';
	idx[0] = 1;
	chr[1] = 'O';
	idx[1] = 1;
	for (int i = 2; i < n; i++)
		cin >> chr[i] >> idx[i];
}

void process()
{
	f[0] = 0;
	f[1] = 0;
	for (int i = 2; i < n; i++)
	{
		int j;
		for (j = i - 1; j >= 0; j--)
			if (chr[j] == chr[i])
				break;
		f[i] = max(f[i - 1], f[j] + abs(idx[i] - idx[j])) + 1;
	}
//	cout << f[0] << f[1] << f[2] << f[3] << f[4] << f[5] << endl;
	ans = f[n - 1];
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int testCase = 0; testCase < t; testCase++)
	{
		init();
		process();
		printf("Case #%d: %d\n", testCase + 1, ans);
	
	}
	return 0;
}