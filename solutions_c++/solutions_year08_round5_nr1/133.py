#include <iostream>
#include <vector>
#include <cmath>
#include <cstring>
#include <algorithm>
#define pb push_back
#define fi first
#define se second
#define INF 1000000000
#define MOD 3000
using namespace std;
typedef long long ll;
typedef pair<int,int> pi;
typedef pair<int,pi> pii;
int solve()
{
	int n;
	cin>>n;
	int x=0,y=0,dir=0;
	int mi[6005],ma[6005];
	for (int i=0; i<6002; i++)
	{
		mi[i]=INF;
		ma[i]=-INF;
	}
	int a=INF,b=-INF;
	int pole=0,p=0;
	for (int i=0; i<n; i++)
	{
		string s;
		int k;
		cin>>s>>k;
		for (int l=0; l<k; l++)
			for (int j=0; j<s.size(); j++)
			{
				if (s[j]=='L') dir=(dir+3)%4;
				if (s[j]=='R') dir=(dir+1)%4;
				if (s[j]=='F')
				{
					if (dir==0) pole+=p,y++;
					if (dir==1) p++,x++;
					if (dir==2) pole-=p,y--;
					if (dir==3) p--,x--;
					mi[x+MOD]=min(mi[x+MOD],y);
					ma[x+MOD]=max(ma[MOD+x],y);
				}
				a=min(a,x+MOD);
				b=max(b,x+MOD);
			}
	}
	if (pole<0) pole=-pole;
	int w=0;
	int aa=a,bb=b;
	p=max(mi[a],mi[b]);
	while (a<=b)
	{
		p=min(p,max(mi[a],mi[b]));
		if (p<=mi[a]) mi[a++]=p;
		else mi[b--]=p;
	}
	a=aa;
	b=bb;
	p=min(ma[a],ma[b]);
	while (a<=b)
	{
		p=max(p,min(ma[a],ma[b]));
		if (p>=ma[a]) ma[a++]=p;
		else ma[b--]=p;
	}
	for (int i=aa; i<bb; i++)
	{
		int ax=max(mi[i],mi[i+1]);
		int bx=min(ma[i],ma[i+1]);
		w+=bx-ax;
	}
	w-=pole;	
	return w;
}

int main()
{
	int tests;
	cin>>tests;
	for (int te=1; te<=tests; te++)
	{
		int w=solve();
		printf("Case #%d: %d\n",te,w);
	}
}
