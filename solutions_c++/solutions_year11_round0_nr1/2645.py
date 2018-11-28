#include <vector>
#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
using namespace std;
const int maxn = 150;
#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define pb push_back

int sgn (int x) {if (x<0) return -1;return x>0;};
void solve(int);

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int t;
	cin >> t;
	forn(i, t) solve(i+1);
	
	return 0;
};
void solve(int I)
{
	vector<int> q, w;
	vector<int> t;
	
	int n, x;
	string s;
	cin >> n;
	forn(i, n)
	{
		cin >> s >> x;
		t.pb(s == "O");
		if (t.back()) q.pb(x);
		else w.pb(x);
	}
	q.pb(1000);
	w.pb(1000);
	reverse(q.begin(), q.end());
	reverse(w.begin(), w.end());
	int qp = 1, wp = 1;
	int sum = 0;
	int pos = 0;
	//forn(i, q.size()) cout << q[i] << " ";cout<<endl;
	//forn(i, w.size()) cout << w[i] << " ";cout<<endl;
	//forn(i, t.size()) cout << t[i] << " ";cout<<endl;
	while (pos < (int)t.size())
	{
		sum++;
		if (t[pos] && qp == q.back())
		{
			pos++;
			q.pop_back();
			wp += sgn(w.back() - wp);
		}
		else if (!t[pos] && wp == w.back())
		{
			pos++;
			w.pop_back();
			qp += sgn(q.back() - qp);
		}
		else
		{
			wp += sgn(w.back() - wp);
			qp += sgn(q.back() - qp);
		}
	}
	cout << "Case #" << I << ": " << sum << endl;
};
