#include<stdio.h>
#include<assert.h>
#include<string.h>
#include<math.h>
#include<assert.h>

#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
#include<utility>
using namespace std;

#define _abs(x)		(((x)>0)?(x):-(x))
#define _max(x,y)	(((x)>(y))?(x):(y))
#define _min(x,y)	(((x)<(y))?(x):(y))

#define EPS 1e-10
#define INF 1000000

#define S(x)	((x)*(x))
#define Z(x)	(_abs(x) < EPS)
#define N(x)	(x < 0 && !Z(x))
#define P(x)	(x > 0 && !Z(x))
#define ZN(x)	(x < 0 || Z(x))
#define ZP(x)	(x > 0 || Z(x))

#define UND		0
#define BIRD	1
#define NOB		2

#define E(x,y)	(Z((x)-(y)))

#define D2(a,b)	(S(a.x-b.x) + S(a.y-b.y))
#define D1(a,b)	(sqrt(D2(a,b)))

#define T2(a,b,c)	((a.x*b.y+b.x*c.y+c.x*a.y) - (a.y*b.x+b.y*c.x+c.y*a.x))

template<class Class1,class Class2,class Class3> struct triple{
	Class1 a;	Class2 b;	Class3 c;
	triple(){}
	triple(Class1 _a,Class2 _b,Class3 _c){
		a = _a;
		b = _b;
		c = _c;
	}
	friend bool operator==(const triple &t1,const triple &t2){
		return t1.a == t2.a && t1.b == t2.b && t1.c == t2.c;
	}
	friend bool operator!=(const triple &t1,const triple &t2){
		return !(t1 == t2);
	}
	friend bool operator<(const triple &t1,const triple &t2){
		if(t1.a == t2.a){
			if(t1.b == t2.b)
				return t1.c < t2.c;
			return t1.b < t2.b;
		}
		return t1.a < t2.a;
	}
};

typedef triple<int,int,int> TI;
typedef pair<int,int> PII;
typedef pair<PII,int> PPI;
typedef pair<int,PII> PIP;
typedef pair<PII,PII> PPP;

int n,m;
vector<TI> v;
int bf;

PII hr,wr,hr2,wr2;


int main(){

	int h,w;
	int T,N;
	int i,j,k,l;
	char buf[123];

	scanf("%d",&T);
	for(N=1;N<=T;N++){

		bf = 0;
		v.clear();
		scanf("%d",&n);
		for(i=0;i<n;i++){
			scanf("%d%d%s",&j,&k,buf);
			if(buf[0]=='B'){
				v.push_back(TI(j,k,BIRD));
				if(bf == 0){
					bf = 1;
					hr.first = hr.second = j;
					wr.first = wr.second = k;
				}
				else{
					hr.first = _min(hr.first,j);
					hr.second= _max(hr.second,j);
					wr.first = _min(wr.first,k);
					wr.second= _max(wr.second,k);
				}
			}
			else{
				scanf("%s",buf);
				v.push_back(TI(j,k,NOB));
			}
		}
		
		printf("Case #%d:\n",N);
		scanf("%d",&m);

		if(!bf){
			for(l=0;l<m;l++){
				scanf("%d%d",&h,&w);

				for(i=0;i<n;i++)
					if(v[i].a == h && v[i].b == w)
						break;
				if(i<n)printf("NOT BIRD\n");
				else	printf("UNKNOWN\n");
			}
			continue;
		}


		for(i=0;i<n;i++){
			if(v[i].c==BIRD)continue;
			if(hr.first <= v[i].a && v[i].a <= hr.second && wr.first <= v[i].b && v[i].b <= wr.second){
				printf("!!!!!!!\n");
				assert(0);
			}
		}

		hr2.first =1;
		hr2.second=INF;

		wr2.first = 1;
		wr2.second = INF;

		for(i=0;i<n;i++){
			if(v[i].c == BIRD)
				continue;

			//hhhhhhh
			if(v[i].a+1 <= hr.first)
				hr2.first = _max(hr2.first , v[i].a+1);
			if(v[i].a-1 >= hr.second)
				hr2.second = _min(hr2.second, v[i].a-1);

			//wwwwwww
			if(v[i].b+1 <= wr.first)
				wr2.first = _max(wr2.first , v[i].b+1);
			if(v[i].b-1 >= wr.second)
				wr2.second = _min(wr2.second, v[i].b-1);

		}

		assert(hr.first <= hr.second);
		assert(wr.first <= wr.second);
		assert(hr2.first <= hr2.second);
		assert(wr2.first <= wr2.second);

//		printf(">>> %d %d\n",hr.first,hr.second);
//		printf(">>> %d %d\n",wr.first,wr.second);
//		printf(">>> %d %d\n",hr2.first,hr2.second);
//		printf(">>> %d %d\n",wr2.first,wr2.second);

		for(l=0;l<m;l++){
			scanf("%d%d",&h,&w);
			if( hr.first <= h && h<=hr.second && wr.first<=w&&w<=wr.second){
				printf("BIRD\n");
			}
			else if(hr2.first <= h && h<=hr2.second && wr2.first<=w&&w<=wr2.second){
				printf("UNKNOWN\n");
			}
			else
				printf("NOT BIRD\n");
		}
	}
	return 0;
}



