#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <map>
using namespace std;

int L,P,C;
int mintry;
int trys(int l,int p)
{
	if(l*C==p)
	{
//		mintry = min(mintry,step);
//		return;
	}
	//select a testpoint;
	int res=1<<20;
	for(int i=l+1;i<p;i++)
	{
		//try 2kinds of answer;
		//yes
	}
}
void solve()
{
	scanf("%d%d%d",&L,&P,&C);
	
	double t = P*1.0/L;

	long long tc = C;
	int step = 0;
	while(1)
	{
		if((tc*L>=P) != (tc>=P*1.0/L)) printf("err\n");
		if(tc*L>=P) break;
		step ++;
		tc*=tc;
	}
	printf("%d\n",step);

}

int main()
{
	int Ti,T;
	scanf("%d",&T);
	for(Ti = 1; Ti <= T; Ti++)
	{
		printf("Case #%d: ",Ti);
		solve();
	}
}
