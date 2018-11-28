int Debug = 1;
/*
 * SOUR:
 * ALGO:
 * DATE:2011 5月22 00时06分37秒
 * COMM:
 * */
#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<cassert>
#include<cmath>
#include<queue>
#include<vector>
#include<map>
#include<stack>
#include<set>
using namespace std;
#define pb(x) push_back(x)
#define fi first
#define se second
#define rab(i,a,b) for(int i(a), _n(b); i <= (_n); i++)
#define rep(i,n) rab(i,0,(n)-1)
 
typedef std::vector < int >vi;
typedef std::pair < int, int > pii;
typedef long long LL;
 
template <class T> void ckmin(T &a,T b) { if (a > b) { a = b; } }
template <class T> void ckmax(T &a,T b) { if (a < b) { a = b; } }
template <class T> void pr(T &a) { cout << a << ' '; }
template <class T> void print(T &a) { a.__str__(); }
template <class T> int size(const vector<T> &v) { return (int)v.size(); }
#define fpr(...) \
	fprintf(stderr, "%s(%d)-%s: ",__FILE__,__LINE__,__FUNCTION__); \
fprintf(stderr, __VA_ARGS__);
int countbit(int n) { return n == 0 ? 0 : 1 + countbit(n & (n - 1)); }
 
const int maxint = 0x7fffffff;
const long long max64 = 0x7fffffffffffffffll;
/*Every problem has a simple, fast and wrong solution.*/
/*std::ios::sync_with_stdio(false);*/
 
const double eps = 1e-13;
int n,D;
pair<int,int> p[1010];
int v[1010];

bool find(double T){
	double last=p[0].first-T-D;
	int i;
	for(i=0;i<n;++i){
		double l=p[i].first-T;
		double r=p[i].first+T;
		double now=max(l,last+D);
		//if(Debug)printf("%d (%lf %lf) %lf ",i,l,r,now);
		now+=(p[i].second-1)*D;
		//if(Debug)printf("->%lf\n",now);
		if(now<l-eps || now>r+eps)return false;
		last=now;
	}
	return true;
}
int main()
{
	int Cas,ca=0;
	scanf("%d",&Cas);
	while(Cas--){
		printf("Case #%d: ",++ca);
		scanf("%d%d",&n,&D);
		int i;
		for(i=0;i<n;++i){
			int t,v;
			scanf("%d%d",&t,&v);
			p[i]=make_pair(t,v);
		}
		sort(p,p+n);
		for(i=0;i<n;++i){
			int sum=0;
			if(i)sum=v[i-1];
			v[i]=sum+p[i].second;
		}
		//for(i=0;i<n;++i)printf("%d(%d) ",p[i].first,p[i].second);putchar(10);
		double l=0,r=1e13;
		while(l<r-eps){
			double mid=(l+r)/2;
			if(find(mid))r=mid;
			else l=mid;
		}
		printf("%.13lf\n",l+eps);
	}
    return 0;
}

