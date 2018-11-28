#pragma comment(linker, "/STACK:65000000")
#include<cstdio>
#include<iostream>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#include<set>
#include<map>
#include<cstring>
#include<string>
#include<cmath>
#include<complex>
#include<ctime>

using namespace std;

typedef long long ll;
typedef pair<ll,ll> pii;
typedef vector<ll> vi;
typedef vi::iterator vit;
typedef vector<pii> vpi;

#define sq(x) (x)*(x)
#define all(x) (x).begin(),(x).end()
#define cl(x) memset(x,0,sizeof(x))
#define LL "%I64d"
#define RLL(x) scanf(LL,&(x))

char mas[10][10];

void test(ll t)
{
	for(ll i=0; i<4; ++i)
		scanf(" %s",mas[i]);
	bool x=false;
	bool y=false;
	bool p=false;
	for(ll i=0; i<4; ++i)
		for(ll j=0; j<4; ++j)
			if(mas[i][j]=='.')
				p=true;
	for(ll i=0; i<4; ++i)
	{
		bool ok=true;
		for(int j=0; j<4; ++j)
			if(mas[i][j]=='O' || mas[i][j]=='.')
				ok=false;
		if(ok)
			x=true;
	}
	for(ll i=0; i<4; ++i)
	{
		bool ok=true;
		for(int j=0; j<4; ++j)
			if(mas[j][i]=='O' || mas[j][i]=='.')
				ok=false;
		if(ok)
			x=true;
	}
	bool ok=true;
	for(ll i=0; i<4; ++i)
	{
		if(mas[i][i]=='O' || mas[i][i]=='.')
			ok=false;
	}
	if(ok)
		x=true;
	ok=true;
	for(ll i=0; i<4; ++i)
	{
		if(mas[i][3-i]=='O' || mas[i][3-i]=='.')
			ok=false;
	}
	if(ok)
		x=true;
	for(ll i=0; i<4; ++i)
	{
		bool ok=true;
		for(ll j=0; j<4; ++j)
			if(mas[i][j]=='X' || mas[i][j]=='.')
				ok=false;
		if(ok)
			y=true;
	}
	for(ll i=0; i<4; ++i)
	{
		bool ok=true;
		for(ll j=0; j<4; ++j)
			if(mas[j][i]=='X' || mas[j][i]=='.')
				ok=false;
		if(ok)
			y=true;
	}
	ok=true;
	for(ll i=0; i<4; ++i)
	{
		if(mas[i][i]=='X' || mas[i][i]=='.')
			ok=false;
	}
	if(ok)
		y=true;
	ok=true;
	for(ll i=0; i<4; ++i)
	{
		if(mas[i][3-i]=='X' || mas[i][3-i]=='.')
			ok=false;
	}
	if(ok)
		y=true;
	if(x)
	{
		printf("Case #%d: X won\n",t);
		return;
	}
	if(y)
	{
		printf("Case #%d: O won\n",t);
		return;
	}
	if(p)
	{
		printf("Case #%d: Game has not completed\n",t);
		return;
	}
	printf("Case #%d: Draw\n",t);
}

int main()
{
	freopen("a.in","r",stdin);freopen("a.out","w",stdout);
	ll n;
	cin>>n;
	for(ll i=1; i<=n; ++i)
		test(i);
	return 0;
}