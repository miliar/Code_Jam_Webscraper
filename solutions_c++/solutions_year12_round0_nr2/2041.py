/*************************************************************************
    > File Name: B.cpp
    > Author: mawenxuan
    > Mail: mawenxuan618@gmail.com 
    > Created Time: 六  4/14 23:34:51 2012
 ************************************************************************/

#include<iostream>
using namespace std;
int N,S,p;
int t[200];
int surpMax[200],normMax[200];
int solve()
{
	int ans=0;
	int sure=0,deffer=0;
	int x,y;
	for (int i=0;i<N;i++)
	{		
		if (t[i]==0)
		{
			if (0>=p)sure++;
			continue;
		}
		x=t[i]/3;
		y=t[i]%3;
		if (y==0)
		{
			normMax[i]=x;// 0 0 0 
			surpMax[i]=x+1;// 0 1 -1 
		}
		if (y==1)
		{
			normMax[i]=x+1;// 0 0 1
			surpMax[i]=-1;// 1 -1 1  same, do not consider
		}
		if (y==2)
		{
			surpMax[i]=x+2;// 0 2 0
			normMax[i]=x+1;// 0 1 1
		}
		if (normMax[i]>=p)sure++;
		else if (surpMax[i]>=p)deffer++;
	}
	ans+=sure;
	if (deffer>=S)ans+=S;
	else ans+=deffer;
	return ans;

}
int main()
{
	int T;
	scanf("%d",&T);
	for (int i=0;i<T;i++)
	{
		scanf("%d%d%d",&N,&S,&p);
		for (int j=0;j<N;j++)scanf("%d",&t[j]);
		printf("Case #%d: %d\n",i+1,solve());
	}
}
