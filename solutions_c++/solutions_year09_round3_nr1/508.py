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
#include <queue>
using namespace std;
#define FORI(c, it) for(typeof(c.begin()) it = c.begin(); it != c.end(); it++) 
#define all(a) (a).begin(),(a).end()
#define FOR(i,x,y) for(int i=(x);i<(y);++i)
#define FORZ(i,y) FOR(i,0,y)
typedef long long int ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> ii;
#define PB push_back
#define SZ size()
int main()
{
    int nC;
    cin >> nC;
    for(int nc = 1; nc <= nC;++nc)
    {
	printf("Case #%d: ",nc);
	string str;
	cin >> str;
	int sz = str.SZ;
	ll cnt = 1;
	map<char,ll> mp;
	vector < ll > vec;
	bool ff = true;
	FORZ(i,sz)
	{
	    if(mp.find(str[i]) != mp.end())
	    {
		vec.PB(mp[str[i]]);
		continue;
	    }
	    if(cnt == 2 && ff)
	    {
		ff = false;
		mp[str[i]] = 0;
		vec.PB(0);
	    }
	    else
	    {
		mp[str[i]] = cnt;
		vec.PB(cnt);
		cnt ++;
	    }
	}
	ll base = cnt;
	ll mul = 0;
	ll ans = 0;
	for(int i = sz-1; i>=0; --i)
	{
	    ll a = 1;
	    FORZ(j,mul)
		a *= base;
	    ans += a * vec[i];
	    mul++;
	}
	cout << ans << endl;
    }
    return 0;
}
