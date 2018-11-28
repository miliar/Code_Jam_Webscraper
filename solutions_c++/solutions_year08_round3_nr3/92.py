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

char fin[]="c.in",fout[]="c.out";
const int NUM=1005,MOD=1000000007;
ilo n,m,x,y,res,z;
int num;
vector< ilo > a,sp,con;
ilo mas[NUM][NUM];

int main(){
	freopen(fin,"r",stdin);
	freopen(fout,"w",stdout);
	cin>>num;
	REP(no,num){
		res=0;
		a.clear();		sp.clear();con.clear();
		cin>> n>>m >>x >>y>>z;
		a.resize(m);
		sp.resize(n);con.resize(n,1);
		REP(i,m)cin>>a[i];
		REP(i,n){
			sp[i]=a[i%m];
			a[i % m] = (x * a[i %m] + y * (i + 1)) %z;
		}
		REP(i,n)
			REP(j,i)
				if(sp[j]<sp[i])
					con[i]=(con[i]+con[j])%MOD;
		REP(i,con.sz)res=(res%MOD+con[i]%MOD)%MOD;
		pif("Case #%d: ",no+1);
		cout<<res<<'\n';
	}
	exit(0);
}
