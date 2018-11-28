#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<cmath>
#include<map>
#include<set>
#pragma comment(linker, "/STACK:167767260")
typedef long long ll;
const int INF = 1000000000;
#define FOR(i,a,b) for(i=a;i<=b;i++)
#define FORN(i,a,b) for(i=a;i>=b;i--)
#define pb push_back 
#define mp make_pair
using namespace std;
double uns,t;
int tes,o,X,S,R,N,x,p,len[10001],sp[10001],i,a[10001],b[10001],w[10001],j,sp22[10001];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>tes;
	FOR(o,1,tes)
	{
		cin>>X>>S>>R>>t>>N;
		FOR(i,1,N)cin>>a[i]>>b[i]>>w[i];

		x=0;
		p=0;

		FOR(i,1,N)
		{
			p++;len[p]=a[i]-x;sp[p]=S;
			p++;len[p]=b[i]-a[i];sp[p]=S+w[i];
			x=b[i];
		}
		p++;len[p]=X-x;sp[p]=S;

		FOR(i,1,p)
			FOR(j,i+1,p)
			if(sp[i]>sp[j])
			{
				swap(sp[i],sp[j]);
				swap(len[i],len[j]);
			}

		uns=0;
		
		FOR(i,1,p)
		{
			double tt;

			if(sp[i]==S)
				tt=min(len[i]/double(R),double(t));else
				tt=min(len[i]/double(sp[i]-S+R),double(t));

			t-=tt;

			if(sp[i]==S)uns+=tt+(len[i]-R*tt)/double(sp[i]);else
				uns+=tt+(len[i]-tt*(sp[i]-S+R))/double(sp[i]);
		}

		printf("Case #%d: %.6f\n",o,uns);
	}
}