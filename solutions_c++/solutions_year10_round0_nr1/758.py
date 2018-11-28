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
typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;
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

int main ()
{
	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);
	int T, n, K;
	ll k, start, step;
	cin >> T;
	For(tests, T)
	{
		cin >> n >> K;
		k = K;
		bool ok = false;
		for(;n<=30;++n)
		{
			start = (1LL<<n) - 1LL;
			step = (1LL<<(n + 1));
			if(k >= start)
			{
				if((k - start) % step == 0)
				  ok = true;
			}
		}
		string res = (ok) ? "ON" : "OFF";
		printf("Case #%d: %s\n", tests + 1, res.c_str());
	}
	return 0;
}
