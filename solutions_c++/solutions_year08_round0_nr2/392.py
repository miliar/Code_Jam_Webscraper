#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <deque>
#include <list>
#include <map>
#include <set>
using namespace std;
#define all(a) (a).begin(),(a).end()
#define mset(a,v) memset(a,v,sizeof(a))
#define pb push_back
#define sz(a) a.size()
#define rep(i,n) for(i=0; i<n; i++)
#define forr(i,a,b) for(i=a; i<=b; i++)
#define ford(i,a,b) for(i=a; i>=b; i--)
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
#define X first
#define Y second
typedef long long ll;
typedef pair<int,int> PI;
typedef vector<int> VI;

bool comp (PI a, PI b)
{ return(a.X<b.X || a.X==b.X && a.Y<b.Y); }

FILE* fi; FILE* fo;
int i,j,v, u,n, t,na,nb, ka,kb;
int h1,m1,h2,m2;
PI a[200], b[200];
bool ya[200],yb[200];

int main()
{
	fi=fopen("b-large.in","r");
	fo=fopen("b-large.res","w");
	fscanf(fi,"%d",&n);
	rep(u,n)
	{
		ka=0, kb=0;
		fscanf(fi,"%d%d%d",&t,&na,&nb);
		rep(i,na)	fscanf(fi,"%d:%d %d:%d",&h1,&m1,&h2,&m2), 
			a[i]=make_pair(h1*60+m1, h2*60+m2);
		rep(j,nb)	fscanf(fi,"%d:%d %d:%d",&h1,&m1,&h2,&m2), 
			b[j]=make_pair(h1*60+m1, h2*60+m2);
		mset(ya,0); mset(yb,0);
		sort(a,a+na,comp); sort(b,b+nb,comp);
		
	i=0; j=0;
	while(i<na || j<nb)
	{
		if(i<na && (j==nb || a[i].X<=b[j].X))
		{
			if(!ya[i]) ka++;
			rep(v,nb) if((b[v].X>=a[i].Y+t) && !yb[v]) { yb[v]=1; break; }
			i++;
		}
		else
		{
			if(!yb[j]) kb++;
			rep(v,na) if((a[v].X>=b[j].Y+t) && !ya[v]) { ya[v]=1; break; }
			j++;
		}
	}
		fprintf(fo,"Case #%d: %d %d\n",u+1,ka,kb);
	}
	fclose(fi); fclose(fo);
	return 0;
}
