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


//	typedefs
typedef long long		LL;

typedef string			str;
typedef vector<int>		VI;
typedef vector<string>	VS;

typedef pair<int,int>		PII;
typedef pair<double,double> PDD;


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

#define MAX 505
//200

int n;
double d;
int v[MAX];
double x[MAX];
double l[MAX], r[MAX], t[MAX], g[MAX];

bool solve(double tim){
	int i;

	double last, left, ll, rr, tor, gap;

	last = -1e50;

	for(i=0;i<n;i++){
		left = tim-t[i];

		if(last > l[i]){
			tor = last - l[i];
			if(tor > left)
				return 0;
			
			ll = l[i] + tor;
			rr = r[i] + tor;
		}
		else{

			//no coll
			//place as left as poss
			gap = min(l[i]-last, left);

			ll = l[i] - gap;
			rr = r[i] - gap;
		}

		last = rr+d;
	}

	return 1;
}

int main(){
	int i,T,N;
	double ans;

	double lo, hi, m;

	INT(T);
	for(N=1;N<=T;N++){
		INT(n);
		DOUBLE(d);

		ans = 0;

		for(i=0;i<n;i++){
			DOUBLE(x[i]);
			INT(v[i]);

			if(v[i]%2==0){
				t[i] = (v[i]/2-1)*d + d/2.;
			}
			else{
				t[i] = (v[i]/2)*d;
			}
			l[i] = x[i]-t[i];
			r[i] = x[i]+t[i];
			maxify(ans, t[i]);

//			printf(">>> %d %d %lf %lf %lf\n",i,v[i],x[i],l[i],r[i]);
		}
		//ans is lobo now.

		lo = ans;
		hi = 1e20;

		int bc = 0;

		while(hi-lo > 1e-13 && ++bc < 200){
			m = (hi+lo)/2.;
			if(solve(m))
				hi=m;
			else
				lo=m;
		}
		m = (hi+lo)/2;

		printf("Case #%d: ", N);

		printf("%.9lf\n", m);// floor(m*10+0.5)/10.);



	}

	return 0;
}
