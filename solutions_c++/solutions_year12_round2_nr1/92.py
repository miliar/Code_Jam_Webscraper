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

VI v;
double sum;

int sgn(double a){
	return a>eps?1:(a<-eps?-1:0);
}

bool check(int id, double per){
	double final=v[id]+sum*per;
	double need=0.0;
	repv(i, v) if( i!=id && sgn(v[i]-final)<0 ){
		need+=(final-v[i])/sum;
	}
	if( sgn(need+per-1.0)>0 ) return true;
	return false;
}

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T; cin>>T;
	rep(Te, 1, T+1){
		int n; cin>>n;
		v.clear();
		sum=0;
		rep(i, 0, n) {
			int a; cin>>a;
			v.PB(a);
			sum+=a;
		}
		printf("Case #%d:", Te);
		repv(i, v){
			double left=0, right=1;
			rep(step, 0, 200){
				double mid=(left+right)/2;
				if( check(i, mid) ) right=mid;
				else left=mid;
			}
			printf(" %.10lf", left*100);
		}
		puts("");
	}
}










