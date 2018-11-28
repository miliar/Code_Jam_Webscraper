#include<stdio.h>
#include<stdlib.h>
#include<iostream>
using namespace std;

long long gcd(long long a,long long b)
{
	if(b==0)
		return a;
	return gcd(b,a%b);
}
int main(int argc,char* argv[])
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int T;
	int cas=1;
	scanf("%d",&T);
	while(T--)
	{
		long long T,pn,pg;
		cin>>T>>pn>>pg;
		long long qn=gcd(pn,100);
		long long qg=gcd(pg,100);
		pn=pn/qn;
		pg=pg/qg;
		qn=100/qn;
		qg=100/qg;
		if(pn==0)
			qn=1;
		if(pg==0)
			qg=1;

		if(T>=qn)
		{
			long long tmp=qn-pn;
			long long tmp2=qg-pg;
			//cout<<tmp2<<","<<tmp<<endl;
			if(tmp2!=0||(tmp2==0&&tmp==0))
			{
				if(tmp==0&&tmp2==qg)
					printf("Case #%d: Broken\n",cas++);
				else if(tmp2==qg&&tmp!=qn)
					printf("Case #%d: Broken\n",cas++);
				else
					printf("Case #%d: Possible\n",cas++);
			}
			else 
			{
				printf("Case #%d: Broken\n",cas++);
			}
		}
		else
			printf("Case #%d: Broken\n",cas++);
	}
	return 0;
}
/*
pn qn
pn+x / (qn +y )  == pg / qg
pn*qg + qg*x = pg*qn +pg*y
qg*x + pg*y =pg*qn - qg*pn
qg*x + pg*(x+a) = pg*qn -qg*pn
(qg+pg)*x+pg*a=pg*qn-qg*pn
*/
