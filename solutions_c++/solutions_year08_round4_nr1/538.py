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
const int inf=1000000,sux=-1;

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

char fin[]="a.in",fout[]="a.out";
const int NUM=10005,LEN=1000;
int m,num,res;
bool v;
bool g[NUM],c[NUM],w[NUM];
int ras[NUM][2];

int suk(int x,bool v){
	if(ras[x][v]==sux){
		int r=inf;
		if(x<(m-1)/2){
			if(v){
				if(g[x]){
					r=min(r,suk(2*x+1,1)+suk(2*x+2,1));
				}
				else{
					r=min(r,suk(2*x+1,1));
					r=min(r,suk(2*x+2,1));
				}
				if(c[x]){
					if(g[x]){
						r=min(r,1+suk(2*x+1,1));
						r=min(r,1+suk(2*x+2,1));
					}
					else{
						r=min(r,1+suk(2*x+1,1)+suk(2*x+2,1));
					}
				}
			}
			else{
				if(g[x]){
					r=min(r,suk(2*x+1,0));
					r=min(r,suk(2*x+2,0));
				}
				else{
					r=min(r,suk(2*x+1,0)+suk(2*x+2,0));
				}
				if(c[x]){
					if(g[x]){
						r=min(r,1+suk(2*x+1,0)+suk(2*x+2,0));
					}
					else{
						r=min(r,1+suk(2*x+1,0));
						r=min(r,1+suk(2*x+2,0));			
					}
				}
			}
		}
		else
			r=(v==w[x])?0:inf;
		ras[x][v]=r;
	}
	return ras[x][v];
}

int main(){
	freopen(fin,"r",stdin);
	freopen(fout,"w",stdout);
	cin>>num;
	REP(zo,num){
		res=0;
		cin>> m>>v;
		REP(i,m)
			REP(j,2)ras[i][j]=sux;

		REP(i,(m-1)/2)
			cin>>g[i]>>c[i];
		REP(i,(m+1)/2)
			cin>>w[(m-1)/2+i];
		res=suk(0,v);
		cout<<"Case #"<<zo+1<<": ";
		if(res<inf)
			cout<<res;
		else cout<<"IMPOSSIBLE";
		cout<<"\n";
	}
	exit(0);
}
