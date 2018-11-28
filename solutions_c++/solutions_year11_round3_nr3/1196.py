#include <fstream>

using namespace std;

ifstream in("freq.in");
ofstream out("freq.out");

const int N = 10001;

int n, l, h;
int v[N];

bool Try(int val)
{
	for (int i = 1; i <= n; ++i)
		if (v[i]%val != 0 && val%v[i] != 0)
			return 0;

	return 1;
}

void SolveCase(int test)
{
	in >> n >> l >> h;

	for (int i = 1; i <= n; ++i)
		in >> v[i];

	out << "Case #" << test << ": ";

	for (int i = l; i <= h; ++i)
		if (Try(i))
		{
			out << i << "\n";
			return;
		}

	out << "NO\n";
}

int main()
{
	int t;
	in >> t;

	for (int i = 1; i <= t; ++i)
		SolveCase(i);

	return 0;
}
