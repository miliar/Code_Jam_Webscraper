#include <vector>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <queue>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <list>
#include <ctime>
#include <string>
#include <cassert>

using namespace std;

//----------------------zjut_DD for Topcoder-------------------------------
typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<string> VS;
#define PB push_back
#define MP make_pair
#define ff first
#define ss second
#define two(w) (1<<(w))
#define test(x,w) (x&two(w))
#define sz(v) (int)v.size()
#define all(c) c.begin(),c.end() 
#define clr(buf,val) memset(buf,val,sizeof(buf))
#define rep(i,l,r) for(int i=(l);i<(r);i++)
#define repv(i,v)  for(int i=0;i<(int)v.size();i++)
#define repi(it,c) for(typeof(c.begin()) it=c.begin();it!=c.end();++it)
//------------------------------------------------------------------------

const double eps=1e-14;



int main(){
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	int T; cin>>T;
	rep(Te, 1, T+1){
		int n; cin>>n;
		VI v; 
		rep(i, 0, n){
			int a; cin>>a;
			v.PB(a);
		}
		map<int, int> mp;
		int s1=-1, s2=-1;
		rep(s, 1, (1<<n)){
			int sum=0;
			rep(i, 0, n) if( test(s, i) ) sum+=v[i];
			if( mp.find(sum)!= mp.end() ){
				s1=mp[sum];
				s2=s;
				break;
			}
			mp[sum]=s;
		}
		if( s1==-1 ){
			printf("Case #%d:\nImpossible\n", Te);
		}else {
			printf("Case #%d:\n", Te);
			int tmp=s1&s2;
			s1^=tmp;
			s2^=tmp;
			bool f=true;
			rep(i, 0, n) if( test(s1, i) ){
				if( !f ) putchar(' ');
				printf("%d", v[i]);
				f=false;
			} puts("");
			f=true;
			rep(i, 0, n) if( test(s2, i) ){
				if( !f ) putchar(' ');
				printf("%d", v[i]);
				f=false;
			} puts("");
		}
	}
}










