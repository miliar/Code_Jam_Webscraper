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

struct sub
{
	double beg;
	double end;
	double w;
	sub(){}
	sub(int a, int b, int c)
	{
		beg=a;
		end=b;
		w=c;
	}
	void scan()
	{
		scanf("%lf%lf%lf",&beg,&end,&w);
	}
};

bool operator< (sub a, sub b)
{
	return a.w>b.w;
}

void test(int id)
{
	double x,s,r,t,n;
	scanf("%lf%lf%lf%lf%lf",&x,&s,&r,&t,&n);
	sub* mas=new sub[n];
	priority_queue<sub> q;
	for(int i=0; i<n; ++i)
	{
		mas[i].scan();
		q.push(mas[i]);
		x-=mas[i].end-mas[i].beg;
	}
	double res=0;
	double T=t;
	if(t<=x/r)
	{
		res+=t;
		x-=r*t;
		q.push(sub(0,x,0));
		T=0;
	}
	else
		q.push(sub(0,x,0));
	while(!q.empty())
	{
		sub cur=q.top();
		q.pop();
		if(T*(r+cur.w)<=cur.end-cur.beg)
		{
			res+=T;
			cur.end-=T*(r+cur.w);
			res+=(cur.end-cur.beg)/(double)(cur.w+s);
			T=0;
		}
		else
		{
			res+=(cur.end-cur.beg)/(double)(cur.w+r);
			T-=(cur.end-cur.beg)/(cur.w+r);
		}
	}
	printf("Case #%d: %.7lf\n",id,res);
}

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int t;
	scanf("%d",&t);
	for(int i=1; i<=t; ++i)
		test(i);
	return 0;
}