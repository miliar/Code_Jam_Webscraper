#include <iostream>
#include <cmath>
#include <algorithm>
#include <numeric>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <bitset>
#include <deque>
#include <map>
#include <stack>
#include <sstream>

using namespace std;

typedef vector<int> vi;
typedef long long ll;
typedef vector<string> vs;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<vi> vvi;

#define mp make_pair
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define sz(x) ((x).size())
#define sqr(x) ((x)*(x))
#define slen(x) ((x).length())

template<class T> T abs(T x) { return x > 0 ? x : -x;}

int n, m;

ll solve(ll a)
{
	int dig[30];
	int i = 0;
	int c = 0;
	ll sa = a;
	vi toUse;
	vi notZero;
	
	while (a != 0)
	{
		dig[i++] = a % 10;
		a /= 10;
	}
	c = i;
		
	i = 1;
	int m = dig[0];
	toUse.pb(dig[0]);
	while (i < c && dig[i] >= m)
	{
		toUse.pb(dig[i]);
//		cout << "add:" << dig[i] << " " << dig[0] << endl;
		m = max(dig[i], m);
		i++;		
	}
	if (i == c)
	{
		int mm = 100000;
		int imin;
		for (i = 0; i < c; i++)
			if (dig[i] != 0 && dig[i] < mm)
			{
				mm = dig[i];
				imin = i;
			}
		cout << dig[imin] << "0";// << "*";
		toUse.clear();
		for (i = 0; i < c; i++)
			if (i != imin)
				toUse.pb(dig[i]);
		sort(toUse.begin(), toUse.end());
		for (i = 0; i < toUse.size(); i++)
			cout << toUse[i];
		return 0;
	}
//	cout << "last:" << dig[i] << endl;
//	toUse.pb(dig[i]);
	int last = dig[i];	
	sort(toUse.begin(), toUse.end());
	int j = c - 1;
	for (i = toUse.size() + 1; i < c; i++)
		cout << dig[j--];
//		cout << "*";
	int imin;
	for (i = 0; i < toUse.size(); i++)
		if (toUse[i] > last)
		{
			cout << toUse[i];
			imin = i;
			break;
		}
//	cout << "*";
//	cout << toUse[imin];
	vi newUse;
	for (i = 0; i < toUse.size(); i++)
		if (i != imin)
			newUse.pb(toUse[i]);
	newUse.pb(last);
	sort(newUse.begin(), newUse.end());
	for (i = 0; i < newUse.size(); i++)
		cout << newUse[i];
}

int main()
{
	int i, j;
	ll a;
	
//	freopen("input", "r", stdin);
//	freopen("output", "w", stdout);
	cin >> n;
	for (i = 0; i < n; i++)
	{
		cin >> a;
		cout << "Case #" << i + 1 << ": ";
		solve(a);
		cout << endl;
	}
	
	return 0;
}
