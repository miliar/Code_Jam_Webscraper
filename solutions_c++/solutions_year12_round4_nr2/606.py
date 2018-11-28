#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cmath>
#include <cassert>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <algorithm>
#include <numeric>
#include <complex>
#include <list>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <bitset>
#include <utility>
#include <functional>
#include <iterator>

using namespace std;

#define dump(n) cerr<<"# "<<#n<<"="<<(n)<<endl
#define repi(i,a,b) for(int i=int(a);i<int(b);i++)
#define peri(i,a,b) for(int i=int(b);i-->int(a);)
#define rep(i,n) repi(i,0,n)
#define per(i,n) peri(i,0,n)
#define iter(c) __typeof__((c).begin())
#define foreach(i,c) for(iter(c) i=(c).begin();i!=(c).end();++i)
#define all(c) (c).begin(),(c).end()
#define mp make_pair

typedef unsigned int uint;
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef pair<double,double> pdd;

template<typename T>
ostream& operator<<(ostream& os,const vector<T>& a)
{
	os<<'[';
	rep(i,a.size())
		os<<(i?" ":"")<<a[i];
	return os<<']';
}
template<typename T1,typename T2>
ostream& operator<<(ostream& os,const pair<T1,T2>& p)
{
	return os<<'('<<p.first<<','<<p.second<<')';
}

struct Rect{
	int w,h,i;
	Rect(){}
	Rect(int w,int h,int i):w(w),h(h),i(i){}
	bool operator<(const Rect& r)const{return max(w,h)<max(r.w,r.h);}
	bool operator>(const Rect& r)const{return max(w,h)>max(r.w,r.h);}
};

void solve()
{
	int n,w,h; cin>>n>>w>>h;
	vi rs(n);
	rep(i,n) cin>>rs[i];
	
	if(n==1){
		puts("0.0 0.0");
		return;
	}
	
	vector<pii> os(2*n-1);
	vi ps(n,-1);
	priority_queue<Rect,vector<Rect>,greater<Rect> > pq;
	rep(i,n)
		pq.emplace(2*rs[i],2*rs[i],i);
	
	while(pq.size()>=2){
		Rect a=pq.top(); pq.pop();
		Rect b=pq.top(); pq.pop();
		int index=ps.size();
		ps.push_back(-1);
		ps[a.i]=ps[b.i]=index;
		if(w-(a.w+b.w)>=h-(a.h+b.h)){
			os[b.i].first+=a.w;
			if(a.h<b.h) os[a.i].second+=(b.h-a.h)/2;
			if(a.h>b.h) os[b.i].second+=(a.h-b.h)/2;
			pq.emplace(a.w+b.w,max(a.h,b.h),index);
		}
		else{
			os[b.i].second+=a.h;
			if(a.w<b.w) os[a.i].first+=(b.w-a.w)/2;
			if(a.w>b.w) os[b.i].first+=(a.w-b.w)/2;
			pq.emplace(max(a.w,b.w),a.h+b.h,index);
		}
	}
	
	vi oxs(n),oys(n);
	rep(i,n){
		oxs[i]=oys[i]=rs[i];
		for(int j=i;j!=-1;j=ps[j]){
			oxs[i]+=os[j].first;
			oys[i]+=os[j].second;
		}
	}
	int mx=*min_element(all(oxs)),my=*min_element(all(oys));
	rep(i,n){
		oxs[i]-=mx;
		oys[i]-=my;
	}
	rep(i,n){
		assert(oxs[i]<=w && oys[i]<=h);
		if(i) putchar(' ');
		printf("%d %d",oxs[i],oys[i]);
	}
	puts("");
}

int main()
{
	int cases; scanf("%d ",&cases);
	rep(i,cases){
		printf("Case #%d: ",i+1);
		solve();
	}
	
	return 0;
}
