#include <iostream>
#include <string>
#include <sstream>
using namespace std;

char sg[] = "N+-";
string w;
string str;
int mlen;

typedef long long ll;

bool ugly (ll p)
{
	return (p%2 == 0) || (p%3 == 0) || (p%5 == 0) || (p%7 == 0);
}

int gen (int x, ll ps, ll p, char l)
{
	p = p*10 + w[x] - '0';
	if (x == mlen-1)
		return ugly (ps + (l == '+' ? p : -p));
	int res = 0;

	ll ps1 = ps, p1 = p;
	char l1 = l;
	for (int i = 0; i < 3; ++i)
	{
		ps1 = ps;
		p1 = p;
		l1 = l;
		if (sg[i] != 'N')
		{
			ps1 += (l == '+' ? p : -p);
			p1 = 0;
			l1 = sg[i];
		}

		res += gen (x+1, ps1, p1, l1);
	}

	return res;
}


int main (int argc, char* argv[])
{
	if (argc >= 2)
		freopen (argv[1], "r", stdin);
	if (argc >= 3)
		freopen (argv[2], "w", stdout);

	int N;
	cin >> N;

	for (int t = 0; t < N; ++t)
	{
		cin >> w;

		mlen = w.length ();

		str.clear ();
		str.resize (mlen-1, '-');

		int res = gen (0, 0, 0, '+');

		cout << "Case #" << t+1 << ": " << res << '\n';
	}

	return 0;
}