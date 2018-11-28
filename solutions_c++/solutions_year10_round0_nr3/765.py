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

inline bool equal(const vi&a, const vi&b)
{
	int n = a.size();
	For(i, n) if(a[i] != b[i]) return false;
	return true;
}

int main ()
{
	freopen("C-large.in", "rt", stdin);
	freopen("C-large.out", "wt", stdout);
	int T, R, k, N;
	cin >> T;
	For(tests, T)
	{
		cin >> R >> k >> N;
		vector<int>v(N);
		For(i, N) cin >> v[i];
		vector<vi >vv;
		vector<int>vectSum;
		int iter = 0, idx;
		ll res;
		for(iter = 0; ;++iter)
		{
			bool found = false;
			for(idx = 0; idx < sz(vv); ++idx) if(equal(vv[idx], v)) { found = true; break; }
			if(found) break;
			int sum = 0, i = 0;
			while(i < N && (sum + v[i]) <= k)
			{
				sum += v[i];
				++i;
			}
			//out(v);
			vv.push_back(v);
			vectSum.push_back(sum);
			rotate(v.begin(), v.begin() + i, v.end());
		}
		//out(vectSum);
		if(R <= iter)
		{
			res = 0LL;
			For(i, R) res += (ll)vectSum[i];
		}
		else
		{
			//db(idx);
			int len = iter - idx;
			//db(len);
			int q = (R - iter) / len;
			//db(q);
			ll sumCycle = 0LL;
			Fori(i, idx, iter) sumCycle += (ll)vectSum[i];
			//db(sumCycle);
			int rem = R - (iter + len * q);
			//db(rem);
			res = 0LL;
			For(i, iter) res += (ll)vectSum[i];
			res += sumCycle * (ll)q;
			For(z, rem) res += (ll)vectSum[idx + z];
		}
		printf("Case #%d: %lld\n", tests + 1, res);
	}
	return 0;
}
