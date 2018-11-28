#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
#include <vector>
#include <stack>
#include <queue>
#include <list>
#include <map>
#include <set>
#include <stdlib.h>
#include <sstream>
#include <assert.h>

#include <time.h>
#pragma comment(linker, "/STACK:20000000")

#define fr(i,a,b) for(int i=(int)(a);i<=(int)(b);i++)
#define fd(i,a,b) for(int i=(int)(a);i>=(int)(b);i--)
#define mp make_pair
#define pb push_back
#define ll long long

using namespace std;

int ri(){int x;scanf("%d",&x);return x;}
ll rll(){ll x;scanf("%lld",&x);return x;}

const int MAXN=1010;

struct wtf
{
	double x;
	double y;
	double r;
	int id;
	wtf(){}
	wtf(double x,double y,double r,int id) :x(x),y(y),r(r),id(id){}
};

wtf mas[MAXN];

#define sqr(x) (x)*(x)

bool check(int now,double x,double y)
{
	fr(i,1,now-1)
	{
		if (sqr(mas[i].x-x)+sqr(mas[i].y-y)<=sqr(mas[now].r+mas[i].r)+1e-2)
			return false;
	}
	return true;
}

ll big_rand()
{
	ll res=(ll)rand();
	res<<=16;
	res+=(ll)rand();
	res<<=16;
	res+=(ll)rand();
	return res;
}

bool checking(int n,double w,double l)
{
	fr(i,1,n)
		fr(j,1,n)
			if (i!=j && sqrt(sqr(mas[j].x-mas[i].x)+sqr(mas[j].y-mas[i].y))<=mas[j].r+mas[i].r+1e-2)
				return true;
	fr(i,1,n)
		assert(mas[i].x>=0 && mas[i].x<=w && mas[i].y>=0 && mas[i].y<=l);
	return false;
}

bool cmp1(wtf x,wtf y)
{
	return x.r>y.r || x.r==y.r && x.id<y.id;
}

bool cmp2(wtf x,wtf y)
{
	return x.id<y.id;
}

void solve()
{
	int test=ri();
	srand(100500);
	fr(testing,1,test)
	{
		
		int n=ri();
		ll w=rll(),l=rll();
		fr(i,1,n)
		{
			ll r=rll();
			mas[i].id=i;
			mas[i].r=r;
		}
		sort(mas+1,mas+1+n,cmp1);
		
		double x=0.0,y=0.0;
		int now=1;
		for(;now<=n && x<(double)w;now++)
		{
			while(x<(double)w)
			{
				if (check(now,x,y))
				{
					mas[now].x=x,mas[now].y=y,x+=mas[now].r;
					//x+=R[now+1];
					break;
				}
				x+=mas[now].r;
			}
			if (!(x<(double)w))
				break;
			//x+=R[now+1];
		}
		y=0;
		//y+=R[now-1];
		x=w;
		for(;now<=n && y<(double)l;now++)
		{
			while(y<(double)l)
			{
				if (check(now,x,y))
				{
					mas[now].x=x,mas[now].y=y,y+=mas[now].r;
					//X[now]=x,Y[now]=y,y+=R[now];
					//y+=R[now+1];
					break;
				}
				y+=mas[now].r;
				//y+=R[now];
			}
			if (!(y<(double)l))
				break;

		}
		x=w;
		//x-=R[now-1];
		y=l;
		for(;now<=n && x>=0;now++)
		{
			while(x>=0)
			{
				if (check(now,x,y))
				{
					mas[now].x=x,mas[now].y=y,x-=mas[now].r;
					//X[now]=x,Y[now]=y,x-=R[now];
					//x-=R[now+1];
					break;
				}
				x-=mas[now].r;
				//x-=R[now];
			}
			if (x<0)
				break;
		}
		y=l;
		x=0;
		for(;now<=n && y>=0;now++)
		{
			while(y>=0)
			{
				if (check(now,x,y))
				{
					mas[now].x=x,mas[now].y=y,y-=mas[now].r;
					//X[now]=x,Y[now]=y,y-=R[now];
					//y-=R[now+1];
					break;
				}
				y-=mas[now].r;
				//y-=R[now];
			}
			if (y<0)
				break;
		}
		while(now<=n)
		{
			//double x=big_rand()%(10*w),y=big_rand()%(l*10);
			x=(double)(big_rand()%(10*w)),y=(double)(big_rand()%(l*10));
			x/=10,y/=10;
			if (check(now,x,y))
			{
				mas[now].x=x,mas[now].y=y,now++;
				//X[now]=x,Y[now]=y,now++;
				continue;
			}
		}
		printf("Case #%d:",testing);
		sort(mas+1,mas+1+n,cmp2);
		fr(i,1,n)
			printf(" %.1lf %.1lf",mas[i].x,mas[i].y);
		if (checking(n,w,l)) assert(0);
		printf("\n");
	}
	
	
}

int main()
{
	#ifndef ONLINE_JUDGE
		freopen("C:/Users/CleRIC/Desktop/Универ/acm.timus.ru/input.txt","rt",stdin);
		freopen("C:/Users/CleRIC/Desktop/Универ/acm.timus.ru/output.txt","wt",stdout);
	#else
		//freopen("input.in","rt",stdin);
		//freopen("output.out","wt",stdout);
	#endif

	solve();

	#ifndef ONLINE_JUDGE
		printf("\n\ntime-%.3lf",clock()*1e-3);
	#endif

	return 0;
}