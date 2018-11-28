#include <iostream>
#include <vector>
#include <list>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <bitset>
#include <algorithm>
#include <string>
#include <sstream>
#include <limits>
#include <cmath>
#include <cassert>
using namespace std;

double x, s, r, t;
int n;

vector< pair< pair<int,int> ,int> > seq;

double prova_a_correre (double v_base, double spazio)
{
//	cout << "+ " << v_base << " " << spazio << endl;
	double t_cor = min (t, spazio / (v_base + r));
	double s_rim = spazio - t_cor * (v_base + r);
	double t_non = s_rim / (v_base + s);
//	cout << t_cor << " " << s_rim << " " << t_non << endl;
	t -= t_cor;
	return t_cor + t_non;
}

void solve ()
{
	cin >> x >> s >> r >> t >> n;

	seq.clear ();

	int b, e, w;
	for (int i = 0; i < n; i += 1)
	{
		cin >> b >> e >> w;
		seq.push_back (make_pair (make_pair (b, e), w));
	}

	sort (seq.begin (), seq.end ());

	double no_space = seq[0].first.first + x - seq[n-1].first.second;
//	cout << no_space << endl;

	for (int i = 1; i < n; i += 1)
	{
		no_space += seq[i].first.first - seq[i-1].first.second;
	}

	double result = prova_a_correre (0, no_space);
//	cout << result << endl;

	priority_queue< pair<int,int> > coda;

	for (int i = 0; i < n; i += 1)
	{
		coda.push (make_pair (-seq[i].second, seq[i].first.second - seq[i].first.first));
	}

	while (!coda.empty ())
	{
		pair<int,int> top = coda.top ();
		coda.pop ();

		result += prova_a_correre (-top.first, top.second);
//		cout << result << endl;
	}

	cout << result << endl;
}

int main ()
{
	cout.setf (ios::fixed);
	cout.precision (9);
	int tc;
	cin >> tc;
	for (int i = 0; i < tc; i += 1)
	{
		cout << "Case #" << i+1 << ": ";
		solve ();
	}
}

