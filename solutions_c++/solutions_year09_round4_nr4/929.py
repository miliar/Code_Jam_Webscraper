#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <set>
#include <algorithm>
#include <utility>
#include <string>
#include <functional>
#include <sstream>
#include <fstream>
#include <cmath>
using namespace std;
#define FOR(i,a,b) for (i=(a);i<=(b);i++)
#define fori(it,v) for (it=(v).begin();it!=(v).end();it++)
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define all(c) c.begin(),c.end()
#define pf push_front
#define popb pop_back
#define popf pop_front
typedef pair<long long ,long long> ii;
FILE *in,*out;
long long raza[50],n;
bool a[50][50];
const long long ct=100000;
pair<ii,long long> b[50];
vector<long long> g1,g2;
long double dist(ii x,ii y)
{
	return sqrt((x.fi-y.fi)*(x.fi-y.fi)+(x.se-y.se)*(x.se-y.se))*ct;
}
int ok(int x,int y)
{
	if (raza[x]+raza[y]>=dist(b[x].fi,b[y].fi))
		return 1;
	return 0;
}
int ver(long long x)
{
	int first,in1,in2,i,j;
	g1.clear();
	g2.clear();
	memset(a,0,sizeof(a));
	memset(raza,0,sizeof(raza));
	FOR(i,1,n)
	{
		if (x<b[i].se)
			return 0;
		raza[i]=x-b[i].se;
	}
	first=1;
	FOR(i,1,n)
		FOR(j,i+1,n)
			if (ok(i,j))
			{
				a[i][j]=1;
				a[j][i]=1;
			}
			else
				if (first)
				{
					g1.pb(i);
					g2.pb(j);
					first=0;
				}
	if (first)
		return 1;
	FOR(i,1,n)
	{
		a[i][i]=1;
		in1=1;
		for(j=0;j<g1.size();j++)
			if (!a[i][g1[j]])
			{
				in1=0;
				break;
			}
		if (in1)
		{
			g1.pb(i);
			continue ;
		}
		in2=1;
		for(j=0;j<g2.size();j++)
			if (!a[i][g2[j]])
			{
				in2=0;
				break;
			}
		if (in2)
		{
			g2.pb(i);
			continue ;
		}
		return 0;
	}
	return 1;

}
int main()
{
	int t,T;
	long long i,rez,x,y,z;
	double rezd;
	in=fopen("test.in","r");
	out=fopen("test.out","w");
	fscanf(in,"%d",&t);
	FOR(T,1,t)
	{
		fscanf(in,"%lld",&n);
		memset(b,0,sizeof(b));
		FOR(i,1,n)
		{
			fscanf(in,"%lld%lld%lld",&x,&y,&z);
			b[i]=mp(mp(x,y),z*ct);
		}
		rez=0;
		for(i=((long long)1)<<32;i;i>>=1)
		{
			rez+=i;
			if (ver(rez))
				rez-=i;
		}
		rez++;
		rezd=((double)rez)/ct;
		fprintf(out,"Case #%d: %lf\n",T,rezd);

	}
	fclose(in);
	fclose(out);
        return 0;
}
