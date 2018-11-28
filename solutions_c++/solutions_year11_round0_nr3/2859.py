#include <fstream>

using namespace std;

ifstream in("candy.in");
ofstream out("candy.out");

const int N = 16;

int n;
int v[N];

int best;
bool sol[N];

void Check()
{
	int a = 0, b = 0, sa = 0, sb = 0;

	for (int i = 1; i <= n; ++i)
	{
		if (sol[i])
		{
			a ^= v[i];
			sa += v[i];
		}
		else
		{
			b ^= v[i];
			sb += v[i];
		}
	}

	if (a == b && sa && sb)
	{
		if (sb > sa)
			sb ^= sa ^= sb ^= sa;

		if (sa > best)
			best = sa;
	}
}

void Back(int pos)
{
	if (pos == n + 1)
	{
		Check();
		return;
	}

	sol[pos] = true;
	Back(pos + 1);

	sol[pos] = false;
	Back(pos + 1);
}

void Solve(int test)
{
	in >> n;

	for (int i = 1; i <= n; ++i)
		in >> v[i];

	out << "Case #" << test << ": ";

	best = 0;
	Back(1);

	if (!best)
	{
		out << "NO\n";
		return;
	}
	out << best << "\n";
}

int main()
{
	int t;
	in >> t;

	for (int i = 1; i <= t; ++i)
		Solve(i);

	return 0;
}
