#include<stdio.h>
#include<math.h>
int no_of_digits(int a)
{
	int cnt=0;
	while(a)
	{
		cnt++;
		a/=10;
	}
	return cnt;
}
int recycle(int x,int y)
{
	int num1,rem,rest,temp,i,cnt=0,var=1;
	double temp1;
	num1=no_of_digits(x);
	temp1=pow(10,num1);
	for(i=1;i<num1;i++)
	{
		var*=10;
		temp1/=10;
		rem=x%var;
		rest=x/var;
		temp=(temp1*rem) + rest;
		if((temp>x)&&(temp<=y))
			cnt++;
	}
	return cnt;
}
int main()
{
	int t,n,m,a,b,count=0,flag,cas=0;
	FILE *p,*p1;
	p= fopen("try.txt","r");
	p1=fopen("output.txt","a");
	fscanf(p,"%d",&t);
	while(t--)
	{
		cas++;
		count=0;
		fscanf(p,"%d%d",&a,&b);
		for(n=a;n<b;n++)
		{
				flag=recycle(n,b);
				if(flag)
				count+=flag;
		}
		fprintf(p1,"Case #%d: %d\n",cas,count);
	}
	return 0;
}