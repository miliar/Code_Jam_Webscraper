#include <iostream>
#include <cmath>
#include <iomanip>
#include <algorithm>

using namespace std;

double eps = 0.00000001;

struct Pair
{
	double place;
	long long count;
};


bool operator<(Pair& a, Pair& b)
{
	return a.place < b.place;
};

int testNum = 0;
int n;
double result;
double d;
Pair p[10000];

void read()
{
	cin >> n >> d;
	int i;
	for (i = 1; i <= n; ++i)
		cin >> p[i].place >> p[i].count;
	sort(p + 1, p + 1 + n);
}

void printOut()
{
	cout << "Case #" << testNum << ": " << fixed << setprecision(6) << result << "\n";
}

double st, end;

bool CanBeDoneIn(double time)
{
	int i, j;
	double maxLeft = p[1].place - time;
	--p[1].count; // temporarily decrease
	for (i = 1; i <= n; ++i)
		for (j = 1; j <= p[i].count; ++j)
		{
			if (p[i].place - time > maxLeft + d)
				maxLeft = p[i].place - time;
			else
			{
				if (fabs(maxLeft + d - p[i].place) - eps <= time)
					maxLeft = maxLeft + d;
				else // dzev chunem teghavorvem!, tqel a!!!!
				{
					++p[1].count; // increase back
					return false;
				}
			}
		}
	++p[1].count; // increase back
	return true;
}

void solve()
{
	read();
	st = 0.0;
	end = d * 1000000.0; // maximum xelqin motik!
	int i, j, k, c;
	while (end - st > 0.00000001)
	{
		if (CanBeDoneIn((end + st) / 2))
			end = (end + st) / 2;
		else
			st = (end + st) / 2;
	}
	result = end;
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
		++testNum;
		solve();
		--t;
	}
return 0;
}