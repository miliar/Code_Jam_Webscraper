#if 1
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <functional>
#include <cstring>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <ctime>
#include <cassert>
#include <sstream>
#include <iostream>
#include <bitset>

using namespace std;

typedef long long LL;
typedef long double LD;
typedef pair<int , int> pii;
typedef vector <int> veci;
typedef vector <veci> graph;
const LD eps = 1e-9;
const LD pi = acos(-1.0);
const int inf = 1000 * 1000 * 1000;
const LL inf64 = LL(inf) * inf;

#define mp make_pair
#define pb push_back
#define X first
#define Y second
#define iss istringstream
#define oss ostringstream
#define dbg(x) {cerr << #x << " = " << x << endl;}
#define dbgv(x) {cerr << #x << " ={"; for (int _i = 0; _i < x.size(); _i++) {if (_i) cerr << ", "; cerr << x[_i];} cerr << "}" << endl;}
#define NAME "problem"

string get_map(string s, string t)
{
	string f(26, '-');
	for(int i = 0; i < s.length(); ++i)
		if(f[s[i] - 'a'] == '-')
			f[s[i] - 'a'] = t[i];
	return f;
}
string p;

void solve(int test)
{
	string msg;
	getline(cin, msg);
	string res;
	for(int i = 0; i < msg.length(); ++i)
		if(msg[i] != ' ')
			res += p[msg[i] - 'a'];
		else
			res += msg[i];
	cout << "Case #" << test << ": " << res << endl;
		
}
int main()
{
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	//freopen(NAME ".in","r",stdin);freopen(NAME ".out","w",stdout);

	string s = "zy qeeejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";
	string t = "qa zooour language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";

	p = get_map(s, t);
	int tests; cin >> tests;
	getline(cin, s);
	for(int test = 1; test <= tests; ++test)
		solve(test);
   
		

	return 0;
}
/*************************
*************************/
#endif
