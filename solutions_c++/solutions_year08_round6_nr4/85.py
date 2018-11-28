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
int mat[105][105];

int mat2[105][105];

int mp[105],taken[105],sf;

void bktk(int lev){
	int i;
	if(lev==m){

		int j,k,ccc;

		ccc = 1;
		for(j=0;j<m;j++)for(k=0;k<m;k++)if(mat[ mp[j] ][ mp[k] ] != mat2[j][k]){
			ccc = 0;
			goto ooo;
		}
ooo:
		if(ccc){
			sf = 1;

//			for(i=0;i<m;i++)
//				printf("%d :: %d\n",i,mp[i]);
		}
	
		return;
	}
	for(i=0;i<n && !sf;i++){
		if(taken[i])continue;
		taken[i]=1;
		mp[lev]=i;

		bktk(lev+1);

		taken[i]=0;
	}
}

int main(){

	int T,N;

	int i,j,k;

	scanf("%d",&T);
	for(N=1;N<=T;N++){

		scanf("%d",&n);
		for(i=0;i<n;i++)for(j=0;j<n;j++)mat[i][j] = 0;
		for(i=0;i<n-1;i++){
			scanf("%d%d",&j,&k);
			j--;k--;
			mat[j][k]=mat[k][j] = 1;
		}

		scanf("%d",&m);
		for(i=0;i<m;i++)for(j=0;j<m;j++)mat2[i][j] = 0;
		for(i=0;i<m-1;i++){
			scanf("%d%d",&j,&k);
			j--;k--;
			mat2[j][k]=mat2[k][j] = 1;
		}

//		printf(">>> %d %d\n",n,m);

		sf = 0;

		bktk(0);

		printf("Case #%d: ",N);

		if(sf)printf("YES\n");
		else	printf("NO\n");

	}
	return 0;
}



