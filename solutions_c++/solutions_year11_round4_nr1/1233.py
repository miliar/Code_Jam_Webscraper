#pragma warning (disable:4996)
#pragma warning (disable:4786)

#include<stdio.h>
#include<string.h>
#include<math.h>
#include<assert.h>

#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<list>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<deque>
#include<algorithm>
#include<utility>
using namespace std;


template<class Class1,class Class2,class Class3> struct triplet{
	Class1 first;Class2 second;Class3 third;triplet(){}
	triplet(Class1 _first,Class2 _second,Class3 _third){	first = _first;	second = _second;third = _third;}
	friend bool operator==(const triplet &t1,const triplet &t2){return t1.first == t2.first && t1.second == t2.second && t1.third == t2.third;}
	friend bool operator!=(const triplet &t1,const triplet &t2){return !(t1 == t2);}
	friend bool operator<(const triplet &t1,const triplet &t2){if(t1.first != t2.first)return t1.first < t2.first;if(t1.second != t2.second)return t1.second < t2.second;return t1.third < t2.third;}
};

//	typedefs
typedef long long		LL;

typedef string			str;
typedef vector<int>		VI;
typedef vector<string>	VS;

typedef pair<LL,LL>		PII;
typedef pair<double,double> PDD;

typedef triplet<int,int,int> TI;

//	Macros
#define EPS 1e-9
#define INF	1000000000

#define _abs(x)		(((x)>0)?(x):-(x))
#define _max(x,y)	(((x)>(y))?(x):(y))
#define _min(x,y)	(((x)<(y))?(x):(y))

#define For3(i,a,b)	for(int i=(a);i<(b);i++)
#define For2(i,a)	for(int i=0;i<(a);i++)
#define fi			for(int i=0;i<n;i++)
#define fj			for(int j=0;j<n;j++)
#define fk			for(int k=0;k<n;k++)

#define S(x)	((x)*(x))
#define C(x)	((x)*(x)*(x))

#define Z(x)	(_abs(x) < EPS)
#define N(x)	(x < -EPS)
#define ZN(x)	(x < EPS)
#define P(x)	(x > EPS)
#define ZP(x)	(x > -EPS)

#define E(x,y)	(Z((x)-(y)))

#define D2(a,b)	(S(a.first-b.first) + S(a.second-b.second))
#define D1(a,b)	(sqrt(D2(a,b)))

#define T2(a,b,c)	((a.first*b.second+b.first*c.second+c.first*a.second) - (a.second*b.first+b.second*c.first+c.second*a.first))

#define all(x)	x.begin(),x.end()
#define pb 		push_back

#define hasV(vec, element)\
	(find(all(vec),element) != vec.end())

#define hasC(container, element)\
	(container.find(element) != container.end())

#define forV(vec, i)\
	for(int sz = vec.size(), i = 0; i < sz; ++i)

#define forC(container, it)\
	for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)

#define INT(x)		scanf("%d",&x)
#define DOUBLE(x)	scanf("%lf",&x)
#define LINT(x)		scanf("%lld",&x)


//	Global Methods
void parse(string s, vector<string> &vs){
	vs.clear();
	istringstream iss(s);
	while(iss >> s)
		vs.pb(s);
}

template<class X>
void remdup(vector<X> &v1, vector<X> &v2){
	v2.clear();
	if(v1.size()==0)
		return;
	sort(all(v1));
	v2.pb(v1[0]);
	int n = v1.size();
	for(int i=1;i<n;++i)if(v1[i]!=v1[i-1])
		v2.pb(v1[i]);
}

template<class X>
inline void minify(X &whom, X val){
	if(val < whom)
		whom = val;
}

template<class X>
inline void maxify(X &whom, X val){
	if(val > whom)
		whom = val;
}


//	My program

#define MAX 3000005

vector<PII> g;

int s,r;
bool myf(const PII &a, const PII &b){
//	double t1 = 1.*a.first/(a.second + r) + 1.*b.first/(b.second + s);
//	double t2 = 1.*a.first/(a.second + s) + 1.*b.first/(b.second + r);
//	return t1 < t2;
	return a.second < b.second;
}

int main(){

	int T, N;
	int x, t, n;
	int rest;
	int a,b,w;

	PII all;

	INT(T);

	int i;

	double tl, tt;

	for(N=1;N<=T;N++){
		
		scanf("%d%d%d%d%d",&x,&s,&r,&t,&n);
		
		rest = x;

		g.clear();
		for(i=0;i<n;i++){
			scanf("%d%d%d",&a,&b,&w);
			rest -= b-a;
			g.pb(PII(b-a,w));
		}

		g.pb(PII(rest,0));

		sort(g.begin(), g.end(), myf);

//		for(i=0;i<g.size();i++){
//			printf(">>>>>> %d %lld %lld\n",i, g[i].first, g[i].second);
//		}

		double tim = 0;
		tl = t;

		for(i=0;i<g.size();i++){

			tt = min(tl, 1.*g[i].first/(g[i].second + r) );	

			tim += tt + (g[i].first - (g[i].second+r)*tt ) / (g[i].second + s);

			tl -= tt;
		}
		
		printf("Case #%d: %.10lf\n", N, tim);
	}

	return 0;
}
