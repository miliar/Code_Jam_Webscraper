#include<iostream.h>
#include<math.h>
#include<fstream>
#include<stdio>
using namespace std;
long shift(long a,long j)
{
	long x,b;
	b=pow(10,j);
	x=a%b;
	a=a/b;
	long l=long(log10(a)+1);
	a=x*pow(10,l)+a;
	return a;
}
int search(long b[1000],long s,long count)
{
	for(int i=0;i<count;i++)
	{
		if(s==b[i])
		return 0;
	}
	return 1;
}
int fcount(long i,long a,long b)
{
	long s=0,c[10]={0},count=0;
	long l=long(log10(i));
	for(long j=1;j<=l;j++)
	{
		s=shift(i,j);
		if(s>=a&&s>i&&s<=b&&search(c,s,count)==1)
		{
			c[count]=s;
			count++;
		}
	 }
	 return count;
}
int main()
{
	ofstream myfile;
	myfile.open ("example.txt");
	long t,a,b,count=0,ans[100]={0};
	cin>>t;
	for(int k=1;k<=t;k++)
	{
		cin>>a>>b;
		count=0;
		for(long i=a;i<=b;i++)
		{
			count+=fcount(i,a,b);
		}
		ans[k-1]=count;
	}
	for(int l=0;l<t;l++)
	myfile<<"Case #"<<l+1<<": "<<ans[l]<<endl;
	return 0;
}