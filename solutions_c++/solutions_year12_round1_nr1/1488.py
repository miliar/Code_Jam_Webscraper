#include <iostream>
#include <stdio.h>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;
double p[100002];
double fac[100002];
int main()
{
	//freopen("D:\\Visual Studio 2008\\Google Code Jam\\A-large.in", "r", stdin ) ;

	//freopen("D:\\Visual Studio 2008\\Google Code Jam\\A-large.out", "w", stdout ) ;

	int cases;
	cin>>cases;
	for(int k=1;k<=cases;++k)
	{
		int A,B;
		cin>>A>>B;
		double ans=999999999;
		cin>>p[1];
		fac[1]=p[1];
		for(int i=2;i<=A;++i)
		{
			cin>>p[i];
			fac[i]=fac[i-1]*p[i];
		}
		ans=min(ans,fac[A]*(B-A+1)+(1-fac[A])*(B-A+1+B+1));
		for(int i=1;i<A;++i)
		{
			ans=min(ans,fac[A-i]*(i+(B-(A-i))+1)+(1-fac[A-i])*(i+(B-(A-i))+1+B+1));
		}
		ans=min(ans,A+B+1.0);
		ans=min(ans,1+B+1.0);
		printf("Case #%d: %.6lf\n",k,ans);
	}
	return 0;
}