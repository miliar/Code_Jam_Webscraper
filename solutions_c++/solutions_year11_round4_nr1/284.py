#include<stdio.h>
#include<string>
#include <string.h>
#include<math.h>
#include<utility>
#include<algorithm>
#include<vector>
#include<ctype.h>
#include<map>
#include <iostream>
using namespace std;

#define MAXN 1010

int dp[MAXN+10];

struct WWay{
	double B,E;
	double w;
};

WWay ways[MAXN];

bool cmp(WWay w1,WWay w2)
{
	return w1.w<w2.w;
}
int X,S,R,N;

double calc(WWay Way,double &t)
{
	double res=(Way.E-Way.B)/(Way.w+R);
	if(t>=res)
	{
		t-=res;
		return res;
	}

	double Left=Way.E-Way.B-t*(Way.w+R);
	res=t+(Left)/(Way.w+S);
	t=0;
	return res;
}

int main()
{
	//freopen("in.txt","r",stdin);
	int T;
	scanf("%d",&T);
	double t;
	int ct=1;
	while(T--)
	{
		scanf("%d %d %d %lf %d",&X,&S,&R,&t,&N);
		int cnt=0,curS=0;
		for(int i=0;i<N;i++)
		{
			int B,E,w;
			scanf("%d %d %d",&B,&E,&w);
			if(curS<B)
			{
				ways[cnt].B=curS;
				ways[cnt].E=B;
				ways[cnt].w=0;
				cnt++;
			}
			ways[cnt].E=E;
			ways[cnt].B=B;
			ways[cnt++].w=w;
			curS=E;
		}
		if(curS<X)
		{
			ways[cnt].B=curS;
			ways[cnt].E=X;
			ways[cnt].w=0;
			cnt++;
		}
		sort(ways,ways+cnt,cmp);
		double sum=0.0;
		for(int i=0;i<cnt;i++)
		{
			sum+=calc(ways[i],t);
		}
		printf("Case #%d: ",ct++);
		printf("%.6f\n",sum);

	}

	return 0;
}
