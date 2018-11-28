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

#define MAX 20

int nc;
int n,m;
int c[MAX];

int nv;
vector<int> v[MAX],t;
int mat[MAX][MAX];

int sf;
int have[MAX][MAX], nhave[MAX];

void bktk(int lev){
	
	int i,j;
	if(lev==n){
		for(i=0;i<nv;i++)if(nhave[i] < nc)
			return;

		sf = 1;
		return;
	}
	
	for(i=1;i<=nc;i++){

		c[lev] = i;

		for(j=0;j<nv;j++){
			if(mat[j][lev]==1){
				have[j][i]++;
				if(have[j][i]==1)
					nhave[j]++;
			}
		}

		bktk(lev+1);
		if(sf)
			break;

		for(j=0;j<nv;j++){
			if(mat[j][lev]==1){
				have[j][i]--;
				if(have[j][i]==0)
					nhave[j]--;
			}
		}
		
		c[lev] = 0;
	}

}

struct Edge{
	int a, b, d;
	void form(){
		a--;b--;
		if(a>b) swap(a,b);
		d = b-a;
		if(a+n-b < d){
			d = a+n-b;
			swap(a,b);
		}
	}
};

bool operator<(const Edge &p, const Edge &q){
	return p.d < q.d;
}

Edge e[MAX];

int main(){
	int i,T,N,j,k,a,b;
	double ans;

	INT(T);
	for(N=1;N<=T;N++){
		INT(n);
		INT(m);

//		if(N%5==0)
			fprintf(stderr, ">> starting %d\n", N);

		nv = 1;
		v[0].clear();
		for(i=0;i<n;i++)
			v[0].pb(i);

		for(k=0;k<m;k++)
			INT(e[k].a);
		for(k=0;k<m;k++)
			INT(e[k].b);
		for(k=0;k<m;k++)
			e[k].form();

		sort(e,e+m);

		for(k=0;k<m;k++){
			a = e[k].a;
			b = e[k].b;

//			printf("\n>> %d %d\n",a, b);
//			printf("before: "); for(i=0;i<v[0].size();i++) printf("%d ",v[0][i]); printf("\n");

			int sz = v[0].size();

			for(j=0;j<sz;j++)if(v[0][j]==a)
				break;
			
			i = 0;

			v[nv].clear();
			v[nv].pb(a);
			
			t.clear();
			t.pb(a);

			j = (j+1)%sz;
			i++;

			while(i<sz){
				if(v[0][j]==b)
					break;
				v[nv].pb(v[0][j]);
				j = (j+1)%sz;
				i++;
			}

			v[nv].pb(b);
			t.pb(b);

			j = (j+1)%sz;
			i++;

			while(i<sz){
				t.pb(v[0][j]);
//				printf(">>> %d %d %d %d\n",t.size(), i, j, v[0][j]);
				j = (j+1)%sz;
				i++;
			}

			v[0] = t;
//			printf("after: "); for(i=0;i<v[0].size();i++) printf("%d ",v[0][i]); printf("\n");
//			printf("after: "); for(i=0;i<v[nv].size();i++) printf("%d ",v[nv][i]); printf("\n");
			nv++;
		}

/*		printf(">>> %d\n", nv);
		for(i=0;i<nv;i++){

			for(j=0;j<v[i].size();j++)
				printf("%d ",v[i][j]);

			printf("\n");
		}
*/		
		memset(mat, 0, sizeof(mat));
		for(i=0;i<nv;i++){
			for(j=0;j<v[i].size();j++)
				mat[i][v[i][j]] = 1;
		}

		memset(c,0,sizeof(c));
		memset(have,0,sizeof(have));
		memset(nhave,0,sizeof(nhave));

		for(nc=n;nc>=1;nc--){
			sf = 0;
			bktk(0);
			if(sf)
				break;
		}
			
		printf("Case #%d: %d\n", N, nc);
		for(i=0;i<n;i++){
			if(i)printf(" ");
			printf("%d", c[i]);
		}
		printf("\n");

	}
	return 0;
}
