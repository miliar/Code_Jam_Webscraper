#include <fstream>
#include <vector>
#include <string>

using namespace std;

ifstream in("bottrust.in");
ofstream out("bottrust.out");

struct push{
	int bt;
	char col;
};

const int N = 101;

int n;
push v[N];

vector <int> no; // next orange
vector <int> nb; // next blue

void ReadCase()
{
	in >> n;

	no.resize(0);
	nb.resize(0);

	for (int i = 1; i <= n; ++i)
	{
		in >> v[i].col >> v[i].bt;

		if (v[i].col == 'O')
			no.push_back(v[i].bt);
		else
			nb.push_back(v[i].bt);
	}
}

inline bool IsSame(push a, push b)
{
	if (a.bt != b.bt)
		return 0;

	if (a.col != b.col)
		return 0;

	return 1;
}

inline void MoveCloser(push &a, int pos)
{
	if (a.bt < pos)
		++a.bt;

	if (a.bt > pos)
		--a.bt;
}

void Solve(int test)
{
	ReadCase();

	int it = 1;
	int steps = 0;
	int noc = 0;
	int nbc = 0;

	push o;
	o.bt = 1;
	o.col = 'O';

	push b;
	b.bt = 1;
	b.col = 'B';

	while (it != n + 1)
	{
		while (!IsSame(o, v[it]) && !IsSame(b, v[it]))
		{
			MoveCloser(o, no[noc]);
			MoveCloser(b, nb[nbc]);
			++steps;
		}

		if (IsSame(o, v[it]))
		{
			++noc;
			MoveCloser(b, nb[nbc]);
		}
		else
		{
			++nbc;
			MoveCloser(o, no[noc]);
		}

		++steps;
		++it;
	}

	out << "Case #" << test << ": " << steps << "\n";
}

int main()
{
	int t;
	in >> t;

	for (int i = 1; i <= t; ++i)
		Solve(i);

	return 0;
}
