#pragma comment(linker,"/STACK:16777216")
#include<cstdio>
#include<iostream>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#include<set>
#include<map>
#include<string>
#include<cstring>
#include<ctime>
#include<cmath>
#include<functional>

using namespace std;

#define ll long long
#define ld long double
#define si short int
#define pii pair<int,int>
#define vi vector<int>
#define vit vector<int>::iterator
#define sq(x) (x)*(x)

struct star
{
	ll t;
	ll tbef;
};

class c1
{
public:
	bool operator()(star a, star b)
	{
		return a.t<b.t;
	}
};

class c2
{
public:
	bool operator()(star a, star b)
	{
		return a.tbef<b.tbef;
	}
};

star* mas=new star[1000001];
int l,n,c;
ll t;
void test(int T)
{
	ll answ=0;
	scanf("%d%lld%d%d",&l,&t,&n,&c);
	ll sum=0;
	for(int i=0; i<c; ++i)
	{
		mas[i].tbef=sum;
		scanf("%lld",&mas[i].t);
		sum+=mas[i].t;
	}
	mas[n].tbef=t>>1;
	mas[n].t=-1;
	for(int j=c; j<n; ++j)
	{
		mas[j].tbef=sum;
		mas[j].t=mas[j%c].t;
		sum+=mas[j].t;
	}
	sort(mas,mas+n+1,c2());
	int pos=n;
	for(int i=1; i<n; ++i)
	{
		if(mas[i].t==-1)
		{
			ll k=mas[i].tbef-mas[i-1].tbef;
			mas[i].t=mas[i-1].t-k;
			mas[i-1].t=k;
			pos=i;
			break;
		}
	}
	sort(mas+pos,mas+n+1,c1());
	for(int i=n; i>=pos; --i)
	{
		if(mas[i].t>0)
			if(l>0)
			{
				answ+=mas[i].t;
				--l;
			}
			else
				answ+=mas[i].t<<1;
	}
	for(int i=0; i<pos; ++i)
		if(mas[i].t>0)
			answ+=mas[i].t<<1;
	printf("Case #%d: %lld\n",T+1,answ);
}

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int T;
	cin>>T;
	for(int i=0; i<T; ++i)
		test(i);
	return 0;
}