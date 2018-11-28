#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>
#include<algorithm>
#include<iterator>
#include<map>
#include<vector>
#include<list>
#include<set>
#include<queue>
#include<cassert>
#include<deque>
#include<stack>
#include<bitset>
#include<functional>
#include<numeric>
#include<utility>
#include<sstream>
#include<iomanip>
#include<string>
#include<cmath>
#include<ctime>

using namespace std;

#define REP(i,n)         for(int i=0;i<(n);++i)
#define FOR(i,a,b)       for(int i=(a);i<=(b);++i)
#define FORD(i,a,b)      for(int i=(a);i>=(b);--i)
#define FOREACH(it,c)    for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define ALL(c)           (c).begin(),(c).end()
#define debug(x)         cerr << #x << " = " << (x) << "\n";
#define debugv(v)        cerr << #v << " = "; FOREACH(it,v) cerr << *it << ",";cerr<<"\n";
#define SZ(c)            (c).size()
#define PB               push_back
#define PF               push_front
#define MP               make_pair
#define ABS(x)           ((x)<0?-(x):(x))

typedef long long LL;
typedef vector<int> VI;
typedef vector<char*> VS;
typedef long double ld;


template<class T> inline int size(const T&c) { return c.size(); }
template<class T> string show(T x) { ostringstream o;o<<x;return o.str(); }
template<class T> T parse(string s) { istringstream i(s);T x;i>>x;return x; }
template<class A, class B> A cvt(B x) {stringstream s;s<<x;A r;s>>r;return r;}

int main() { 
	int test;cin>>test;
	FOR(a,1,test) {
		int s;cin>>s;
		getchar();
		char st[100][100];
		REP(i,s) {
			gets(st[i]);
		}
		int q;cin>>q;getchar();
		char t[1000][100];
		REP(i,q) {
			gets(t[i]);
		}
		int minm=0;
		int j,m=0,mm;
		while(m<q) {
			int maxm=0;
			REP(i,s) {
				j=m;
				int temp=0;
				while(j<q) {
					if(strcmp(st[i],t[j])==0) { break; }
					temp++;
					j++;
				}
				//cout<<temp<<' '<<st[i]<<endl;	
				if(temp>maxm)  { mm=j;maxm=temp; }
			}
			m=mm;
			if(m<q) ++minm;
		}
		cout<<"Case #"<<a<<": "<<minm<<endl;
	}
}
