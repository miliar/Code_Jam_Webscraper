#include <functional>
#include <algorithm>
#include <iterator>
#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <numeric>
#include <utility>
#include <cstring>
#include <cstdlib>
#include <cstddef>
#include <vector>
#include <bitset>
#include <cstdio>
#include <cctype>
#include <deque>
#include <stack>
#include <queue>
#include <cmath>
#include <ctime>
#include <list>
#include <map>
#include <set>

using namespace std;

#define mp make_pair
#define pb push_back
#define mref mem_fun_ref
#define bid back_inserter
#define all(x) (x).begin(), (x).end()

typedef long long LL;
typedef pair<int,int> pint;
typedef istringstream iss;
typedef ostringstream oss;
template < class T > void OUT(T res) { cout << res << endl; exit(0); }

const double PI = 3.14159265358979323846264;
const int MAXP = 100001;
const long long MAXD = 1000001;
const long long MAXV = 1000001;
int last = 0;
int p[MAXV];
double mas[MAXV];

int n, d;
	
bool FL(double res)
{
	mas[0] = p[0] - res;

	for (int i = 1; i < last; ++ i)
	{
		double must = mas[i - 1] + d;
		if (must >= p[i])
		{
			mas[i] = must;
			if (must - p[i] > res) return 0;
		}
		else 
		{
			mas[i] = max(must, p[i] - res);
		}
	}
	return 1;
}

bool FR(double res)
{
	mas[last - 1] = p[last - 1] + res;

	for (int i = last - 2; i >= 0; -- i)
	{
		double must = mas[i + 1] - d;
		if (must <= p[i])
		{
			mas[i] = must;
			if (p[i] - must > res) return 0;
		}
		else 
		{
			mas[i] = min(must, p[i] + res);
		}
	}
	return 1;
}

void Solve()
{
	cin >> n >> d;

	last = 0;
	for (int i = 0; i < n; ++ i)
	{
		int addp, addv;
		cin >> addp >> addv;

		for (int j = 0; j < addv; ++ j)
		{
			p[last ++] = addp;
		}
	}

	double l = 0;
	double r = MAXD * MAXV;
	double EPS = 1e-7;

	while (r - l > EPS)
	{
		double c = (l + r) / 2;

		if (FL(c) || FR(c)) { if (r == c) break; r = c; }
		else { if (l == c) break; l = c; }
	}

	if (FL(l) || FR(l)) printf("%.18lf\n", l);
	else printf("%.18lf\n", r);
}

int main()
{
	/*{
		ofstream fout("input.txt");
		fout << 50 << endl;
		for (int test = 0; test < 50; ++ test)
		{
			fout << 200 << " " << rand() << endl;
			for (int i = 0; i < 200; ++ i)
			{
				fout << rand() << " " << 1000000 / 200 << endl;
			}
		}
	}*/
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int testCnt = 0;
	cin >> testCnt;

	for (int test = 0; test < testCnt; ++ test)
	{
		cout << "Case #" << test + 1 << ": ";
		Solve();
	}

	return 0;
}
