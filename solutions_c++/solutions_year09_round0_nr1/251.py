/*
TASK:
LANG: C++
 */
#include <algorithm>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include<iostream>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<list>
#include<bitset>
#include<cstring>
#include<climits>
#include<deque>
#include<utility>
#include <complex>
#include <numeric>
#include <functional>
#include <stack>
#include <iomanip>
#include <ctime>
#ifdef _MSC_VER
#include <hash_set>
#include <hash_map>
using namespace stdext;
#else
#include <ext/hash_set>
#include <ext/hash_map>
using namespace __gnu_cxx;
#endif
template<class key>
struct hashtemp
{

	enum
	{
		bucket_size = 4, min_buckets = 8
	};
	virtual size_t operator()(const key &p) const=0;

};

using namespace std;

#define rep(i,n) for(int  i=0;i<(int)(n);++i)
long double ZERO=0;
const long double INF=1/ZERO,EPSILON=1e-12;
#define all(c) (c).begin(),(c).end()
#define rep2(i,a,b) for(int i=(a);i<=((int)b);++i)
#define foreach(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)

#define sz(v) ((int)((v).size()))
#define let(x,y) __typeof(y) x(y)

#define rrep(i,n) for(int  i=((int)n)-1;i>=0;--i)
#define rall(c) (c).rbegin(),(c).rend()
#define rrep2(i,a,b) for(int i=(a);i>=((int)b);--i)
#define rforeach(it,c) for(__typeof((c).rbegin()) it=(c).rbegin();it!=(c).rend();++it)
#define rep2d(i, j, v) rep(i, sz(v)) rep(j, sz(v[i]))
#define foreach2d(i, j, v) foreach(i,v) foreach(j,*i)

int main() {
#ifndef ONLINE_JUDGE
	freopen("A-large.in","rt",stdin);
	freopen("A-small.out","wt",stdout);
#endif
	int l,d,n;
	cin>>l>>d>>n;
	vector<string> words;
	rep(i,d)
	{
		words.push_back("");
		cin>>words.back();
	}
	rep2(t,1,n)
	{
		string s;
		cin>>s;
		vector<string> q;
		stringstream ss(s);
		rep(i,l)
			if(ss.peek()=='(')
				q.push_back(""),ss.ignore(1),getline(ss,q.back(),')');
			else
				q.push_back(string(1,ss.get()));
		int res=0;
		rep(i,d)
		{
			rep(j,sz(words[i]))
				if(q[j].find(words[i][j])==-1)
					goto next;
			res++;
			next:;
		}
		cout<<"Case #"<<t<<": "<<res<<endl;
	}
	return 0;
}
