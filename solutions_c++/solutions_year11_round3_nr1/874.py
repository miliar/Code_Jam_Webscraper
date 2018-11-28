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
	int r, c;
	cin >> r >> c;
	V<string> a(r);
	fi(i, r)
		cin >> a[i];
	fi(i, r - 1)
	{
		fi(j, c - 1)
		{
			if (a[i][j] == '#' && a[i + 1][j] == '#' && a[i][j + 1] == '#' && a[i + 1][j + 1] == '#')
			{
				a[i][j] = '/'; a[i][j + 1] = '\\';
				a[i + 1][j] = '\\'; a[i + 1][j + 1] = '/';
			}
		}
	}
	fi(i, r)
		fi(j, c)
		{
			if (a[i][j] == '#')
			{
				cout << "Impossible" << endl;
				return;
			}
		}
	fi(i, r)
		cout << a[i] << endl;
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
		cout << "Case #" << (i + 1) << ":" << endl;
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
