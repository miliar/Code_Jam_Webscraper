#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;

#define LL long long
LL ti,t,ans;
int m,n,c,a[2000000],tes;

void search(int i,int tt,LL ti)
{
	if (ans>=0 && ti>=ans) return ;
	if (i==n)
	{
		if (ti<ans || ans<0) ans=ti;
		return ;
	}
	int l=a[i%c];
	if (tt<m) 
	{ 
			LL tti;
			if (ti>=t) tti=ti+l;
			else
			if (ti+2*l>=t)
			{
				tti=l+(t+ti)/2;
			}
			else tti=ti+l*2;
			search(i+1,tt+1,tti);	
	}
	search(i+1,tt,ti+l*2);
}

LL solve()
{
	ans=-1;
	search(0,0,0);
	return ans;
}



int main()
{
	freopen("b.out","w",stdout);
	scanf("%d",&tes);
	for (int ttt=1;ttt<=tes;ttt++)
	{
		printf("Case #%d: ",ttt);
		scanf("%d%I64d%d%d",&m,&t,&n,&c);
		for (int i=0;i<c;i++) scanf("%d",&a[i]);
		printf("%I64d\n",solve());
		
	}
	return 0;
}
