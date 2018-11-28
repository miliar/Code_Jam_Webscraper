#include<iostream>
#include<stdlib.h>

using namespace std;

int main()
{
	int t,k=1;
	scanf("%d" ,&t);
	while(t--)
	{
		int a,b,i,j;
		long double *c,*d,ptotal=1.0,best;
		cin>>a;cin>>b;
		c=new long double[a+1];
		d=new long double[a+3];
		for(i=0;i<a;i++)
		{
			cin>>c[i];
		}
		for(i=0;i<a;i++)
		{
			ptotal=ptotal*c[i];
		}
		d[0]=((ptotal)*(b-a+1))+((1-ptotal)*((2*b)+2-a));
		if(a==b)
		{
			d[1]=(ptotal*1)+((1-ptotal)*(b+2));
		}
		else
		{
			d[1]=b+2;
		}
		ptotal=1;
		if(d[0]<d[1])
			best=d[0];
		else
			best=d[1];
		for(i=2;i<a+2;i++)
		{
		for(j=0;j<a-1;j++)
			ptotal=ptotal*c[j];
		d[i]=((ptotal)*(b-a+((2*i)-1)))+((1-ptotal)*((2*b)+(2*i)-a));
		if(d[i]<best)
			best = d[i];
		}
		
		printf("Case #%d: %0.6Lf\n" , k , best);
		free(c);
		free(d);
		k++;
	}


	return 0;
}