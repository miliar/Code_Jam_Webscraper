#include <iostream>
#include <cmath>
#include <iomanip>
#include <algorithm>

using namespace std;

struct Pair
{
	long long value;
	long long count;
};


bool operator<(Pair& a, Pair& b)
{
	return a.value > b.value;
};


int testNum = 0;
long long L, t, N, C;
long long result, aSum;
Pair a[10000];

void read()
{
	cin >> L >> t >> N >> C;
	int i;
	aSum = 0;
	for (i = 1; i <= C; ++i)
	{
		cin >> a[i].value;
		a[i].count = N / C;
		aSum += a[i].value;
	}
}

void printOut()
{
	cout << "Case #" << testNum << ": " << result << "\n";
}

void solve()
{
	read();
	int i, j, k;
	result = 2 * aSum * (N / C);
	for (i = 1; i <= N % C; ++i)
	{
		result += 2 * a[i].value;
		++a[i].count;
	}
	// resulti mej stacanq obshi champen, aranc boosteri!
	for (i = 1; i <= C; ++i)
	{
		a[i].count -= t / (aSum * 2);
	}

	t = t % (aSum * 2); // mnac taki poch@! // t-n besamp mets test case! tsatskes anpayman!!!!!!!!!!
	for (i = 1; t > 0; ++i)
	{
		t -= a[i].value * 2;
		--a[i].count; // One less posibility to facilitate this
	}

	++C;
	a[C].value = - t / 2; // the last chance of half optimization
	a[C].count = 1;

	sort(a + 1, a + 1 + C);

	for (i = 1; i <= C; ++i)
	{
		if (a[i].count <= 0)
			continue; // to handle huge t test cases!
		if (L >= a[i].count)
		{
			result -= a[i].count * a[i].value;
			L -= a[i].count;
		}
		else
		{
			result -= L * a[i].value;
			break ;
		}
	}
	printOut();
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	while(t)
	{
		cerr << testNum << "\n";
		++testNum;
		solve();
		--t;
	}
return 0;
}