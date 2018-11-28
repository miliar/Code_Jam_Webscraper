#include <iostream>
#include <fstream>
#include <cassert>
#include <vector>
#include <algorithm>
using namespace std;

typedef long long number;

number gcd(number a, number b)
{
	assert(a > b && b >= 0);
	while (b > 0)
	{
		number c = a % b;
		a = b; b = c;
	}
	return a;
}

void test_gcd()
{
	for (int a = 1; a < 20; ++a)
	for (int b = 1; b < a; ++b)
	{
		cout << a << ',' << b << '=' << gcd(a,b) << ' ';
	}
	cout << endl;
}

number solve_fairwarning_case(size_t N, vector<number> & t)
{
	sort(t.begin(), t.end());
	vector<number>::iterator newend = unique(t.begin(), t.end());
	N = newend-t.begin();
	assert(N >= 2);

	number a = t[0];
	for (size_t i = N-1; i > 0; --i)
		t[i] -= t[i-1];
	assert(a == t[0]);
	sort(t.begin()+1, newend);

	number b = t[1];
	for (size_t i = 2; i < N; ++i)
		b = gcd(t[i], b);

	number r = a % b;
	number toapocalypse = r == 0 ? 0 : b-r;
	return toapocalypse;
}

void solve_fairwarning(istream & in, ostream & out)
{
	int C;
	in >> C;
	for (int t = 1; t <= C; ++t)
	{
		size_t N;
		in >> N;
		vector<number> sinceevent(N);
		for (size_t i = 0; i < N; ++i)
			in >> sinceevent[i];
		number toapocalypse = solve_fairwarning_case(N, sinceevent);
		out << "Case #" << t << ": " << toapocalypse << "\n";
	}
}


int main()
{
	//test_gcd();

	assert(sizeof(long long) == 8);
	//ifstream in("B-sample.in");
	//ofstream out("B-sample.txt");

	ifstream in("B-small-attempt0.in");
	ofstream out("B-small-out.txt");

	//ifstream in("B-large.in");
	//ofstream out("B-large-out.txt");
	solve_fairwarning(in,out);

	return 0;
}