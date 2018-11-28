#if 1
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <stack>
#include <cstdlib>
#include <cassert>
#include <cstring>
#include <functional>
#include <algorithm>
#include <cmath>
#include <bitset>
#include <cstdio>
#include <list>
#include <ctime>
using namespace std;

typedef long long LL;
typedef long double LD;
typedef unsigned long long ULL;
const LD eps = 1e-9;
const LD pi = acos(-1.0);

typedef pair<int, int> pii;
typedef pair<LD, LD> pdd;
#define mp make_pair
#define pb push_back
#define X first
#define Y second
#define iss istringstream
#define oss ostringstream
#define dbg(x) cerr << #x << " = " << x << endl;
#define dbgv(x) { cerr << #x << ": {"; for(int i = 0; i < x.size(); ++i) { if(i) cerr << ", "; cerr << x[i]; } cerr << "}" << endl; }
#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()
#define START clock_t _clock = clock();
#define END cerr << endl << "time: " << (clock() - _clock) / LD(CLOCKS_PER_SEC) << endl;

string i2s(int a) { ostringstream os; os << a; return os.str(); }
int s2i(string a) { int b; istringstream is(a); is >> b; return b; }

int main()
{
	//START
    // freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);

    freopen("/home/nsv/Рабочий стол/inp.txt", "r", stdin);
    freopen("/home/nsv/Рабочий стол/out.txt", "w", stdout);

    int T; cin >> T;
    for (int t = 0; t < T; ++t)
    {
    	set<pii> st;
    	int a, b; cin >> a >> b;
    	for (int i = a; i <= b; ++i)
    	{
    		string s = i2s(i);
    		for (int j = 1; j < s.size(); ++j)
    		{
    			string r = s.substr(j) + s.substr(0, j);
    			int val = s2i(r);
    			if (val > i && val >= a && val <= b)
    				st.insert(mp(i, val));
    		}
    	}
    	cout << "Case #" << t + 1 << ": " << st.size() << endl;
    }

	//END
    return 0;
}
/***************
freopen("/home/nsv/Рабочий стол/inp.txt", "r", stdin);
freopen("/home/nsv/Рабочий стол/out.txt", "w", stdout);
***************/
#endif