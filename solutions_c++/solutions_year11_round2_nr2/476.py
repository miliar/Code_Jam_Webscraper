#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<cmath>
#include<map>
#pragma comment(linker, "/STACK:167767260")
typedef long long ll;
const int INF = 1000000000;
#define FOR(i,a,b) for(i=a;i<=b;i++)
#define pb push_back 
#define mp make_pair
using namespace std;
ll k[201],x[201],d,n;
int i,j,tes,o;
double uns;
bool f(double t)
{
	double v;
	int i,j;
	v=double(-10000000000000.);
	FOR(i,1,n)
	FOR(j,1,k[i])
	{
		double xx=max(v+double(d),double(x[i])-t);
		v=xx;
		if(abs(v-x[i])>t+0.000000001)return false;
	}
	return true;
}
void run(double l,double r)
{
	if(r-l<0.00000001)
	{
		uns=r;
	}else
	{
	double m;
	m=(l+r)/double(2);
	if(f(m)==true)run(l,m);else run(m,r);
	}
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>tes;
	FOR(o,1,tes)
	{
		cin>>n>>d;
		FOR(i,1,n)cin>>x[i]>>k[i];

		FOR(i,1,n)
			FOR(j,i+1,n)
			if(x[i]>x[j])
			{
				swap(x[i],x[j]);swap(k[i],k[j]);
			}

		run(0,1000000000000.);
		printf("Case #%d: %.6f\n",o,uns);
	}
}