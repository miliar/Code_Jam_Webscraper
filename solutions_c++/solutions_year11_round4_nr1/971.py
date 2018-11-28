#include <functional>
#include <algorithm>
#include <iterator>
#include <iostream>
#include <sstream>
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

const int MAXN = 10001;
const int MAXM = 0;
const double INF = 0;

struct Node
{
	int b, e;
	double w;
	void Read()
	{
		cin >> b >> e >> w;
	}
	double len() const
	{
		return e - b;
	}
	int run(double s, double r) const
	{
		return len() / (r + w);
	}
	Node() {}
	Node(int _b, int _e, double _w = 0): b(_b), e(_e), w(_w) {}
};


double s, r;

bool operator < (const Node& a, const Node& b)
{
	if (a.w != b.w) return a.w < b.w;
	else return a.len() > b.len();
}

Node mas[MAXN];

void Solve()
{

	int len;
	int n;
	double t; 

	cin >> len >> s >> r >> t >> n;

	for_each(mas, mas + n, mref(&Node::Read));

	int last = n;
	if (mas[0].b != 0) mas[last ++] = Node(0, mas[0].b);

	for (int i = 1; i < n; ++ i)
	{
		if (mas[i - 1].e != mas[i].b) mas[last ++] = Node(mas[i - 1].e, mas[i].b);
	}

	if (mas[n - 1].e != len) mas[last ++] = Node(mas[n - 1].e, len);

	n = last;

	sort(mas, mas + n);

	double res = 0;

	for (int i = 0; i < n; ++ i)
	{
		if (t == 0) res += mas[i].len() / (mas[i].w + s);
		else
		{
			double maxt = mas[i].len() / (mas[i].w + r);

			if (maxt <= t) { res += maxt; t -= maxt; }
			else
			{
				double len = mas[i].len();
				len -= t * (mas[i].w + r);

				res += t + len / (mas[i].w + s);
				t = 0;
			}
		}
	}

	printf("%.18lf\n", res);
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int ctest;
	cin >> ctest;

	for (int test = 0; test < ctest; ++ test)
	{
		cout << "Case #" << test + 1 << ": ";
		Solve();
	}

	return 0;
}
