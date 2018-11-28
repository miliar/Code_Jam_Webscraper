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
#if __GNUC__ > 2
#include <ext/hash_set>
#include <ext/hash_map>
using namespace __gnu_cxx;
#else
#include <hash_set>
#include <hash_map>
#endif
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
#ifndef M_PI
const long double M_PI=acos((long double)-1);
#endif
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

struct state
{
	string s1,s2;
	int i,j;
	bool operator<(const state&s)const
	{
		return make_pair(make_pair(i,j),make_pair(s1,s2))<make_pair(make_pair(s.i,s.j),make_pair(s.s1,s.s2));
	}
};
int main() {
#ifndef ONLINE_JUDGE
	freopen("B-small-attempt0_2.in","rt",stdin);
	freopen("3.out","wt",stdout);
#endif

	int t;
	cin>>t;
	rep2(T,1,t)
	{
		int r,c,f;
		cin>>r>>c>>f;
		vector<string> b;
		rep(i,r)
		{
			string str;
			cin>>str;
			b.push_back(str);
		}
		set<pair<int,state> > q;
		state s={b[0],b[1],0,0};
		q.insert(make_pair(0,s));
		set<state> vis;
		int res=-1;
		while(!q.empty())
		{
			pair<int,state> s=*q.begin();
			q.erase(q.begin());
			if(!vis.insert(s.second).second)
				continue;
			if(s.second.i==b.size()-1)
			{
				res=s.first;
				break;
			}
			state ss=s.second;
			if(ss.s2[ss.j]=='.')
			{
				int ni;
				rep2(k,ss.i+2,b.size())
				{

					if((k-ss.i)-1>f)
						goto next;
					if(k==b.size() || b[k][ss.j]=='#')
					{
						ni=k-1;
						break;
					}
				}
				ss.s1=ss.s2;
				ss.s2=b[ni];
				if(ni!=ss.i+1)
					ss.s1=b[ni];
				if(ni+1!=b.size())
					ss.s2=b[ni+1];
				ss.i=ni;
				q.insert(make_pair(s.first,ss));
			}
			else
			{
				for(int k=-1;k<2;k+=2)
					if(ss.j+k<c && ss.j+k >=0 && ss.s1[ss.j+k]!='#')
					{
						state sss=ss;
						sss.j+=k;
						q.insert(make_pair(s.first,sss));
						if(ss.s2[ss.j+k]=='#')
						{
							sss=ss;
							sss.s2[ss.j+k]='.';
							q.insert(make_pair(s.first+1,sss));
						}
					}
			}
			next:;
		}
		if(res!=-1)
			printf("Case #%d: Yes %d\n",T,res);
		else
			printf("Case #%d: No\n",T);
	}
	return 0;
}
