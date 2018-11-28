#include<iostream>
#include <cmath>
#include <cstdio>
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
#define INF 1000000000

#define S(x)	((x)*(x))
#define Z(x)	(_abs(x) < EPS)
#define N(x)	(x < 0 && !Z(x))
#define P(x)	(x > 0 && !Z(x))
#define ZN(x)	(x < 0 || Z(x))
#define ZP(x)	(x > 0 || Z(x))

#define E(x,y)	(Z((x)-(y)))

#define D2(a,b)	(S(a.x-b.x) + S(a.y-b.y))
#define D1(a,b)	(sqrt(D2(a,b)))

#define T2(a,b,c)	((a.x*b.y+b.x*c.y+c.x*a.y) - (a.y*b.x+b.y*c.x+c.y*a.x))

typedef pair<int,int> PII;

#define ALL(x)  x.begin(),x.end()
#define PB push_back
#define FT first
#define SD second
typedef long long ll;
typedef pair<int,int> PII;
typedef pair<double,double> PDD;
#define MP make_pair
typedef vector<int> VI;
PII operator+(PII a, PII b){ return MP(a.FT+b.FT,a.SD+b.SD); }
PDD operator+(PDD a, PDD b){ return MP(a.FT+b.FT,a.SD+b.SD); }

//typedef __int64 LL;
int u;
	
int win[1<<20][4][4];
string b[16];
int r,c;
int ir[]={-1,-1,-1,0,1,1,1,0},ic[]={-1,0,1,1,1,0,-1,-1};

int recur(int st, int m, int n){
	if (win[st][m][n]>100*u) return win[st][m][n]-100*u-1;
	int ret=1,i,j,k;
	for (k=0; k<8; k++){
		i=m+ir[k];
		j=n+ic[k];
		if (i<0 || j<0 || i>=r || j>=c) continue;
		if ((st&(1<<(i*c+j)))) continue;
		if (recur((st|(1<<(c*i+j))),i,j)==1) ret=0;
	}
	win[st][m][n]=100*u+ret+1;
	return ret;
}

int main(){
	int t,i,j,m,n,k;
	cin>>t;
	for (u=1; u<=t; u++){
		cin>>r>>c;
		int st=0;
		m=n=0;
		for (i=k=0; i<r; i++){
			cin>>b[i];
			for (j=0; j<c; j++,k++){
				if (b[i][j]=='K'){ 
					m=i;
					n=j;
					b[i][j]='#';
				}
				if (b[i][j]=='#') st=(st|(1<<(i*c+j)));
			}
		}
		cout<<"Case #"<<u<<": "<<(char)('A'+recur(st,m,n))<<endl;
	}
	return 0;
}



