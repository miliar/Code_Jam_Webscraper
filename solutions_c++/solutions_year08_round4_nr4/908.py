#include <vector>
#include <list>
#include <map>
#include <set>
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

#define sz size()
#define PB push_back
#define clr(x) memset(x, 0, sizeof(x))
#define forn(i,n) for(__typeof(n) i = 0; i < (n); i++)
#define ford(i,n) for(int i = (n) - 1; i >= 0; i--)
#define forv(i,v) forn(i, v.sz)
#define For(i, st, en) for(__typeof(en) i = (st); i < (en); i++)

using namespace std;
typedef long long ll;

string permute(string s, vector<int> kv, int k)
{
	string ns = s;
	forn(i, s.sz/k)
		forn(j, k)
			ns[i*k+j] = s[i*k+kv[j]];
	return ns;
}

ll count(string s)
{
	ll ret = 1;
	For(i, 1, s.sz)
		if(s[i] != s[i-1])
			ret++;
	return ret;
}

int main()
{
	int cases = 0;
	cin >> cases;
	forn(i, cases)
	{
		int k;
		cin >> k;	
		string s;
		cin >> s;
		string ns = s;
		vector <int> kv(k, 0);
		forn(j, k)
			kv[j] = j;
		ll ret = count(ns);
		while(next_permutation(kv.begin(), kv.end()))
		{
			ret = min(ret, count(permute(s, kv, k)));
		}
		printf("Case #%d: %lld\n", i+1, ret);
	}
	return 0;
}
