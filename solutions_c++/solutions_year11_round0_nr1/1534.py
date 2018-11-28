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

const int n = 100;

int nbut;
map<string, int> M;

int p[3], t[3];

int main(){
	int T,N;
	char ss[10];
	string s;

	int i,j,k;

	M.clear();
	ss[0] = 'O';
	ss[1] = '\0';
	s = string(ss);
	M[s] = 1;

	ss[0] = 'B';
	ss[1] = '\0';
	s = string(ss);
	M[s] = 2;

	INT(T);
	for(N=1;N<=T;N++){
		INT(nbut);

		t[1] = t[2] = 0;
		p[1] = p[2] = 1;
		while(nbut--){
			scanf("%s%d",ss,&i);
			s = string(ss);
			k = M[s];
			t[k] = max(t[k] + abs(i-p[k]) + 1, t[3-k] + 1);
			p[k] = i;
		}
		
		printf("Case #%d: %d\n",N, max(t[1],t[2]));
	}

	return 0;
}
