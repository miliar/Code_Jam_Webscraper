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
int tes,o,i,j,x,y,k,uns,n,m,l,k1,k2,v[10],rr,xx[1001],yy[1001],w,res[10];
vector<int> a[2001],b,c;
bool z[101];
void run(int l)
{
	int i,j;
	if(w>0){}else
	if(l==n+1)
	{
		bool zz=true;
		FOR(i,1,k)
		{
			FOR(j,1,rr)z[j]=false;
			FOR(j,0,a[i].size()-1)z[v[a[i][j]]]=true;
			FOR(j,1,rr)if(z[j]==false)zz=false;
		}
		if(zz)
		{
			w++;
			FOR(i,1,n)res[i]=v[i];
		}
	}else
	{
		FOR(i,1,rr)
		{
			v[l]=i;
			run(l+1);
		}
	}
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>tes;
	FOR(o,1,tes)
	{
		cin>>n>>m;
		k=1;
		a[1].clear();
		FOR(i,1,n)a[1].pb(i);

		FOR(i,1,m)cin>>xx[i];
		FOR(i,1,m)cin>>yy[i];

		FOR(i,1,m)
		{
			x=xx[i];
			y=yy[i];
			FOR(j,1,k)	
			{
				k1=k2=-1;
				FOR(l,0,a[j].size()-1)
					if(a[j][l]==x)k1=l;else
						if(a[j][l]==y)k2=l;
				if(k1!=-1 && k2!=-1)break;
			}

			if(k1>k2)swap(k1,k2);

			b.clear();
			FOR(l,0,k1)b.pb(a[j][l]);
			FOR(l,k2,a[j].size()-1)b.pb(a[j][l]);
			c.clear();
			FOR(l,k1,k2)c.pb(a[j][l]);

			a[j]=b;
			k++;
			a[k]=c;
		}

		rr=n;
		FOR(i,1,k)rr=min(rr,(int)a[i].size());
		memset(v,0,sizeof(v));
		if(rr==n)
		{
			uns=n;
			FOR(i,1,n)res[i]=i;
		}else
		{
			for(;;rr--)
			{
				w=0;
				run(1);
				if(w>0)break;
			}
			uns=rr;
		}
		printf("Case #%d: %d\n",o,uns);
		FOR(i,1,n)
		{
			if(i==1)cout<<res[i];else cout<<" "<<res[i];
		}
		cout<<endl;
	}
}