#include <iostream>
#include <fstream>
#include <cassert>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
//download TTMath from http://www.ttmath.org/
//#include <ttmath/ttmath.h>

using namespace std;
//using namespace ttmath;

#define metafor(iter,container) \
	for ((iter) = (container).begin(); (iter) != (container).end(); ++(iter))
#define FOR(i,n) for (size_t i = 0; i < (n); ++i)

__int64 dcm(__int64 a, __int64 b)
{
	//if (a < 0) a = -a;
	//if (b < 0) b = -b;
	if (a < b) swap(a,b);
	while (b != 0) {
		__int64 r = a%b;
		a = b; b = r;
	}
	return a;
}

__int64 capped_mcm(__int64 a, __int64 b, __int64 cap)
{
	__int64 d = dcm(a, b);
	b /= d;
	if (a > cap/b+1) // => a*b > (floor(cap/b)+1)*b > cap/b*b == cap
		return cap+1;
	return a*b; //OVERFLOW?
}

__int64 factor(__int64 L, __int64 n)
{
	assert(L <= n);
	if (L == n) return n;
	assert(L < n);
	cerr << "chk factor" << L << '\t' << n << '\n';
	vector<__int64> gr;
	for (__int64 d = 1; d*d <= n; ++d)
		if (n % d == 0)
			if (L <= d) return d;
			else gr.push_back(n/d);
	for (int i = gr.size()-1; i >= 0; --i)
		if (L <= gr[i]) return gr[i];
	assert(false);
	return n;
}

__int64 solve_case(vector<__int64> & notes, __int64 L, __int64 H)
{
	if (L == 1) return 1;

	sort(notes.begin(), notes.end());

	const size_t N = notes.size();
	vector<__int64> d(N);
	d[N-1] = notes[N-1];
	for (int i = N-2; i >= 0; --i)
		d[i] = dcm(notes[i],d[i+1]);

	if (L <= d[0] && d[0] <= H)
		return factor(L, d[0]);

	__int64 m = notes[0];
	for (int j = 1; j < N; ++j) {
		if (m > H) return -1;
		if (d[j] % m == 0 && m <= H)
			if (L <= m) return m;
			else {
				assert(L > m);
				cerr << "chk3: " << m << '\t' << L << '\t' << H << '\t' << 0 << '\n';
				for (__int64 k = 1; k <= d[j]/m && k <= H/m; ++k)
					if (L <= k*m && k*m <= H && d[j]%(k*m) == 0) return k*m;
			}
		m = capped_mcm(m,notes[j], H);
	}
	if (m > H) return -1;
	if (L <= m && m <= H) return m;
	assert(L > m && m <= H);
	assert(L <= H);
	cerr << "chk1: " << m << '\t' << L << '\t' << H << '\n';
	if (L % m == 0) return L;
	__int64 k = L/m + 1;
	cerr << "chk2: " << m << '\t' << L << '\t' << H << '\t' << k << '\n';
	assert(L <= k*m);
	if (k*m <= H) return k*m;
	return -1;
}

void solve(istream & in, ostream & out)
{
	int TC_NCases;
	in >> TC_NCases;
	for (int t = 1; t <= TC_NCases; ++t)
	{
		int N; __int64 L, H;
		in >> N >> L >> H;
		vector<__int64> notes(N);
		FOR(i,N)
			in >> notes[i];
		cerr << "Case #" << t << endl;
		__int64 result = solve_case(notes, L, H);
		if (result < 0)
			out << "Case #" << t << ": " << "NO" << "\n";
		else
			out << "Case #" << t << ": " << result << "\n";
	}
}


int main()
{
	//ifstream in("C-sample.in");
	//ofstream out("C-sample.txt");

	//ifstream in("C-small-attempt0.in");
	//ofstream out("C-small-out.txt");

	ifstream in("C-large.in");
	ofstream out("C-large-out.txt");

	solve(in,out);

	return 0;
}