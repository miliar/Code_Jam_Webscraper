#include<iostream.h>
#include<math.h>
#include<stdlib.h>
#include<conio.h>

long rotate(long n,long b)
{
	long x=n,count=0;
	long len=floor(log10l(n))+1;
	for(long i=0;i<len-1;i++)
	{

		x= (fmodl(x,10))*pow(10,len-1) + x/10;
		if(x==n)
		break;

		if(x>=n&&x<=b)
		{
			//cout<<n<<"-"<<x<<",";
			count++;
		}
	}
	return count;

}


void main()
{
	long n,a[50],b[50],count[50];
	cin>>n;
	for(long i=0;i<n;i++)
	{
		count[i]=0;
	}
	for(i=0;i<n;i++)
	{
		cin>>a[i]>>b[i];
	}
	for(i=0;i<n;i++)
	{
		for(long j=a[i];j<b[i];j++)
		{
			count[i]+=rotate(j,b[i]);
		}
		//cout<<endl;
	}
	for(i=0;i<n;i++)
	{
		cout<<"Case #"<<i+1<<": "<<count[i];
		if(i!=0)
		cout<<endl;
	}
	getch();

}