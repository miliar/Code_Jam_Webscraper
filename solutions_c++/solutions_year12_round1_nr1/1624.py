#include<iostream>
#include<fstream>
#include<stdio.h>
using namespace std;
double p[110000],pp[110000];
double getp(int n)
{
	double ans=1;
	int i;
	for (i=1;i<=n-1;i++)
		ans=ans*p[i];
	return ans*(1-p[n]);
}
int main()
{
	ifstream in("D:/A-small-attempt0.in");
	FILE * out;
	out=fopen("D:/A-small-attempt0.out","w");

	long long j,i,t,tt,a,b;
	double pro,min;
	in>>t;
	for (tt=1;tt<=t;tt++)
	{
		in>>a>>b;
		for (i=1;i<=a;i++)
			in>>p[i];
		p[i]=0;
		for (i=1;i<=a+1;i++)
			pp[i]=getp(i);
		//不退格
		min=0; pro=0;
		for (i=1;i<=a+1;i++)
		{
			if (i==a+1)
				pro=pro+pp[i]*(b-a+1);
			else
				pro=pro+pp[i]*(b-a+1+b+1);
		}
		min=pro;
		for (i=1;i<=a;i++)//退格数目
		{
			pro=0;
			for (j=1;j<=a+1;j++)//第几个开始错
			{
				if (i>=a-j+1)
				{
					pro=pro+pp[j]*(2*i+b-a+1);
				}
				else
				{
					pro=pro+pp[j]*(2*i+b-a+1+b+1);
				}
			}
			if (min>pro) min=pro;
		}
		if (min>b+2) min=b+2;
	
		fprintf(out,"Case #%lld: %.6lf\n",tt,min);

	}
	in.close();
	fclose(out);

}