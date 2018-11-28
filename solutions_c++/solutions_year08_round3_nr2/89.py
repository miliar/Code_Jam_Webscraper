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
int n,num;
ilo res;
char s[LEN],d[LEN];

ilo jop(){
	ilo r=0,t=s[0]-'0',z=0;
	REP(i,n-1)
		if(!d[i])
			t=t*10+s[i+1]-'0';
		else{
			if(z<2)r+=t;
			else r-=t;
			t=s[i+1]-'0';
			z=d[i];
		}
	if(z<2)r+=t;
	else r-=t;
	return r;
}

void dfs(int dep){
	if(dep==n-1){
		ilo k=jop();
		if(!(k%2)||!(k%3)||!(k%5)||!(k%7))
			res++;
		return;
	}
	REP(i,3){
		d[dep]=i;
		dfs(dep+1);
	}
}

int main(){
	freopen(fin,"r",stdin);
	freopen(fout,"w",stdout);
	saf("%d\n",&num);
	REP(z,num){
		res=0;
		gets(s);
		n=strlen(s);
		dfs(0);
		pif("Case #%d: %ld\n",z+1,res);
	}
	exit(0);
}
