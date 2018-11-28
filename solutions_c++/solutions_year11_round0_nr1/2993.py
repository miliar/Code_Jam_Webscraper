#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <stack>
#include <deque>
#include <queue>
#include <ctime>
#include <algorithm>
#include <set>
#include <cstring>
#include <cassert>

#define fi(i, n) for (int i = 0; i < n;  ++i)
#define fv(i, v) for (int i = 0; i < v.size(); ++i)
#define fab(i, a, b) for (int i = a; i <= b; ++i)
#define fba(i, b, a) for (int i = b; i >= a; --i)

#define VI vector<int>
#define VS vector<string>
#define VL vector<long long>
#define SI set<int>
#define SS set<string>
#define SL set<long long>
#define V vector
#define S set
#define LL long long

#define mp(a, b) make_pair(a, b)
#define pb(x) push_back(x)
#define all(x) x.begin(), x.end()
#define sz size()

#define X first 
#define Y second

#define dbg if (is_debugging)

using namespace std;

bool is_debugging = 0;

void solveTheProblem()
{
	int n;
	cin >> n;
	int po = 1, pb = 1, ko = 0, kb = 0;
	V<pair<int, int> > vo, vb;
	fi(i, n)
	{
		char r;
		int p;
		cin >> r >> p;
		if (r == 'O')
			vo.pb(mp(i, p));
		else
			vb.pb(mp(i, p));
	}
	int r = 0;
	while (ko < vo.sz && kb < vb.sz)
	{
		//cerr << po << "/" << vo[ko].Y << ":" << ko << " " << pb << "/" << vb[kb].Y << ":" << kb << endl;
		bool p = 0;
		if (po < vo[ko].Y)
			++po;
		else if (po > vo[ko].Y)
			--po;
		else if (vo[ko].X < vb[kb].X)
			++ko, p = 1;
		if (pb < vb[kb].Y)
			++pb;
		else if (pb > vb[kb].Y)
			--pb;
		else if (vb[kb].X < vo[ko].X && !p)
			++kb;
		++r;
	}
	while (ko < vo.sz)
	{
		r += abs(po - vo[ko].Y) + 1;
		po = vo[ko].Y;
		++ko;
	}
	while (kb < vb.sz)
	{
		r += abs(pb - vb[kb].Y) + 1;
		pb = vb[kb].Y;
		++kb;
	}
	cout << r;
}

int main()
{
#ifdef debug
	cerr << "Debug mode." << endl;
	is_debugging = 1;
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	cerr << "Starting program \"A\" ..." << endl;
	cerr << "-------------------------------------------------------------------------------" << endl;
	int cl1 = clock();
	solveTheProblem();
	int cl2 = clock();
	cerr << "-------------------------------------------------------------------------------" << endl;
	double t = (cl2 - cl1) / (CLOCKS_PER_SEC * 1.0);
	cerr << "Finished!" << endl << endl;
	cerr << "Proc. time: " << t << " secs." << endl;
#else
#ifdef multitest
	cerr << "Multitest mode." << endl;
	is_debugging = 1;
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	cerr << "Starting program \"A\" ..." << endl;
	int num_tests;
	scanf("%d\n", &num_tests);
	fi(i, num_tests)
	{
		cout << "Case #" << (i + 1) << ": ";
		cerr << "Test #" << (i + 1) << ":" << endl;
		cerr << "-------------------------------------------------------------------------------" << endl;
		int cl1 = clock();
		solveTheProblem();
		int cl2 = clock();
		cerr << "-------------------------------------------------------------------------------" << endl;
		double t = (cl2 - cl1) / (CLOCKS_PER_SEC * 1.0);
		cerr << "Proc. time: " << t << " secs." << endl << endl;
		cout << endl;
	}
	cerr << "Finished!" << endl;
#else
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	solveTheProblem();
#endif
#endif
	return 0;
}
