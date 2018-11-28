#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstddef>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

// Constants
const int INF = 1000000000;
const long double EPS = 1e-10L;
const long double PI = acos(-1.0);

#define For(i,b) for(int i = 0; i < (int)b; ++i)
#define Fori(i,a,b) for(int i = a; i < (int)b; ++i)
#define All(t) t.begin(),t.end()
#define Fill(a,b) memset(a,b,sizeof(a))
#define Forstl(it,x) for(typeof(x.begin()) it=x.begin(); it!=x.end(); ++it)
#define db(x) cout << #x << " = " << x << endl
#define mod(A, B) ((((A) % (B)) + (B)) % (B))
#define Exist(container, element) (container.find(element) != container.end())
#define sz(a) int((a).size())
#define ARRSIZE(x) (sizeof(x)/sizeof(x[0]))
#define pb push_back
#define mp make_pair
#define rad(a) ((1.*(a)*PI)/180.)
#define sqr(a) ((a)*(a))
#define bet(a,b,c) (((a)<=(b))&&((b)<=(c)))

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<ll> vi;
typedef vector<string> vs;

string itos (int i) {stringstream s; s << i; return s.str();}
int stoi (string s) {istringstream in(s); int ret; in >> ret; return ret;}

template <class T>
void out(vector<T> v)
{
  cout << "{";
  For(_i,v.size()) {if(_i) cout<<","; cout<<v[_i];}
  cout<<"}"<<endl;
}

const string FILENAME = "A-small-attempt0";

bool inline ok(vi v)
{
	int n = sz(v);
	For(i,n)
	{
		ll mask = (1 << (n-i-1)) - 1;
		ll val = v[i] & mask;
		//db(mask), db(val);
		if(val > 0) return false;
	}
	return true;
}

int main ()
{
	freopen(string(FILENAME + ".in").c_str(), "rt", stdin);
	freopen(string(FILENAME + ".out").c_str(), "wt", stdout);
	int TT;
	cin >> TT;
	For(tests, TT)
	{
		int n;
		cin >> n;
		vi v(n);
		For(i,n)
		{
			ll x = 0;
			char c;
			For(j, n)
			{
				cin >> c;
				x = x * 2LL + (ll)(c-'0');
			}
			v[i] = x;
		}
		
		queue<vi > Q;
		Q.push(v);
		map<vi, int> my;
		my[v] = 0;
		int res;
		while(!Q.empty())
		{
			vi top = Q.front(); Q.pop();
			int move = my[top];
			if(ok(top))
			{
				res = move;
				break;
			}
			For(i, n-1)
			{
				vi next = top;
				swap(next[i], next[i+1]);
				if(!my.count(next))
				{
					my[next] = move + 1;
					Q.push(next);
				}
			}
		}
		printf("Case #%d: %d\n", tests + 1, res);
	}
	return 0;
}
