#include <iostream>
#include <stdio.h>
#include <fstream>
#include <memory.h>
#include <cstring>
#include <cmath>

using namespace std;

int t,a,b,cas;
double p[100001],pro[100001],ans1,ans2,ans3,sum;

void try1()
{
	ans1 = sum*(b-a+1)+(1-sum)*(2*b-a+2);
}
void try2()
{
	double tmp,k;
	ans2 = 100000000;
	for(int i=a-1; i>=0; i--)
	{
		sum /= p[i];
		k = sum*(a+b-2*i+1)+(1-sum)*(a+2*b-2*i+2);
		ans2 = k<ans2?k:ans2;
	}
}
void try3()
{
	ans3 = b+2;
}

int main()
{
	freopen("A-small-attempt1.in","r",stdin);
	freopen("output.out","w",stdout);
	int i,j;
	double ans;
	cas = 1;
	scanf("%d",&t);
	while(t--)
	{
		printf("Case #%d: ",cas++);
		scanf("%d%d",&a,&b);
		//ans1 = ans2 = ans3 = 0;
		sum = 1;
		for(i=0; i<a; i++)
		{
			scanf("%lf",&p[i]);
			sum *= p[i];
		}
		try1();
		try2();
		try3();
		ans = ans1<ans2?ans1:ans2;
		ans = ans<ans3?ans:ans3;
		printf("%lf\n",ans);
	}
	return 0;
}
