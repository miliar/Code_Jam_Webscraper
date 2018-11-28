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
	int n, l, h;
	cin >> n >> l >> h;
	VI a(n);
	fi(i, n)
		cin >> a[i];
	fab(i, l, h)
	{
		bool ok = 1;
		fi(j, n)
			ok &= (i % a[j] == 0 || a[j] % i == 0);
		if (ok)
		{
			cout << i << endl;
			return;
		}
	}
	cout << "NO" << endl;
}

int main()
{
#ifdef debug
	cerr << "Debug mode." << endl;
	is_debugging = 1;
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	cerr << "Starting program \"C\" ..." << endl;
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
	cerr << "Starting program \"C\" ..." << endl;
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
