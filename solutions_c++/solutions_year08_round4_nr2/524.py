#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <cctype>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <queue>
#include <string>
#include <sstream>
#include <vector>
#include <map>
#include <bitset>
#include <list>
#include <set>

using namespace std;

const double eps=1e-5,pi=4*atan(1.0);
const int inf=1000000000,sux=-1;

#define FOR(i,a,b) for(int i=a;i<b;i++)
#define REP(i,b) FOR(i,0,b)
#define EQ(a,b) (abs((a)-(b))<=eps)
#define ALL(c) (c).begin(), (c).end()
#define SOR(c) sort(ALL(c))
#define REV(c) reverse(ALL(c))
#define UNI(c) SOR(c),(c).resize(unique(ALL(c))-(c).begin())
#define X first
#define Y second
#define sqr(a) ((a)*(a))
#define dist(a,b) sqrt(sqr(a.X-b.X)+sqr(a.Y-b.Y))
#define pb push_back
#define sz size()
#define pif printf
#define saf scanf

typedef long long ilo;
typedef vector< int > VI;
typedef vector< VI > VVI;
typedef pair< int,int > II;
typedef vector< II > VII;
typedef vector< string > VS;
typedef stringstream SS;

inline bool prim(ilo p){if(2==p)return 1;if(p<2 || !(p%2))return 0;ilo k=(ilo)sqrt(double(p))+1;for(ilo i=3;i<=k;i+=2)if(!(p%i))return 0;return 1;}
ilo ipow(ilo x,ilo p){if(!x)return 0;if(!p || 1==x)return 1;ilo k=ipow(x,p/2);k*=k;if(p%2)k*=x;return k;}

char fin[]="b.in",fout[]="b.out";
const int NUM=10000,LEN=1000;
int n,m,num,res;
double a;

inline double xuj(int x1,int y1,int x2,int y2,int x3,int y3){
	double a,b,c,p;
	a=sqrt(double(sqr(x2-x1)+sqr(y2-y1)));
	b=sqrt(double(sqr(x2-x3)+sqr(y2-y3)));
	c=sqrt(double(sqr(x3-x1)+sqr(y3-y1)));
	p=(a+b+c)/2;
	return sqrt(p*(p-a)*(p-b)*(p-c));
}

int main(){
	freopen(fin,"r",stdin);
	freopen(fout,"w",stdout);
	cin>>num;
	REP(zo,num){
		cout<<"Case #"<<zo+1<<": ";
		res=0;
		cin>>n >>m >>a;
		if(a/2>double(m*n)/2)
			;
		else{
			int x1=0,y1=0;
			REP(x2,n+1)
			REP(x3,x2+1)
			REP(y2,m+1)
			REP(y3,m+1)
				if(EQ(xuj(x1,y1,x2,y2,x3,y3),a/2)){
					pif("%d %d %d %d %d %d\n",x1,y1,x2,y2,x3,y3);
					goto SHIT;
				}
		}
		pif("IMPOSSIBLE\n");
SHIT:	
		;
	}
	exit(0);
}
