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
	V<char> v;
	map<pair<char, char>, char> comb;
	set<pair<char, char> > opp;
	int c, d, n;
	string t;
	cin >> c;
	fi(i, c)
	{
		cin >> t;
		comb[mp(t[0], t[1])] = t[2];
	}
	cin >> d;
	fi(i, d)
	{
		cin >> t;
		opp.insert(mp(t[0], t[1]));
	}
	cin >> n >> t;
	fi(i, n)
	{
		v.pb(t[i]);	
		while (v.sz > 1)
		{
			char e1 = v[v.sz - 1], e2 = v[v.sz - 2];
			if (comb.count(mp(e1, e2)))
			{
				v.pop_back();
				v[v.sz - 1] = comb[mp(e1, e2)];
			}
			else if (comb.count(mp(e2, e1)))
			{
				v.pop_back();
				v[v.sz - 1] = comb[mp(e2, e1)];
			}
			else
				break;
		}
		fv(i, v)
			fab(j, i + 1, v.sz - 1)
				if (opp.count(mp(v[i], v[j])) || opp.count(mp(v[j], v[i])))
				{
					v.clear();
					break;
				}
	}
	string sep = "";
	cout << "[";
	fv(i, v)
	{
		cout << sep << v[i];
		sep = ", ";
	}
	cout << "]";
}

int main()
{
#ifdef debug
	cerr << "Debug mode." << endl;
	is_debugging = 1;
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	cerr << "Starting program \"B\" ..." << endl;
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
	cerr << "Starting program \"B\" ..." << endl;
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
