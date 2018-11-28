#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

typedef vector<int> vint;
typedef vector<vint> vvint;
//typedef double D;
typedef long long LL;

const int inf = 1000 * 1000 * 1000;
const LL INF = 1000000000ll * 1000000000ll;



int d, c, t;
vector<pair<LL, LL> > Ven;

bool f(LL time)
{
	LL p = -INF;
	for(int i = 0; i < Ven.size(); ++i)
	{
		LL L = Ven[i].first - time;
		p = max(p, L);	
		p += d * Ven[i].second;
		if (p - Ven[i].first - d > time)
			return 0;
	}
	return 1;
}

int main()
{
	freopen("B.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> t;
	LL sum = 0;
	for(int I = 1; I <= t; ++I)
	{
		cin >> c >> d;
		Ven.assign(c, pair<LL, LL>());
		for(int i = 0; i < c; ++i)
		{
			cin >> Ven[i].first >> Ven[i].second;
			sum += Ven[i].second;
			Ven[i].first *= 2;
		}
		sort(Ven.begin(), Ven.end());
		d *= 2;
		LL L = 0, R = sum * d + 1ll; 
		LL m;
		while (R - L > 1)
		{
			m = (R + L) / 2;
			if (f(m))
				R = m;
			else
				L = m;
		}
		cout << "Case #" << I << ": ";
		if (f(L))
		{
			cout << L / 2;
			if (L & 1)
				cout << ".5";
			cout << endl;
		}
		else
		{
			cout << R / 2;
			if (R & 1)
				cout << ".5";
			cout << endl;
		}
	}
	return 0;

}