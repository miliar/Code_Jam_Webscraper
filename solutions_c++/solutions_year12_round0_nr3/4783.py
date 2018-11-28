#include<iostream>
using namespace std;
int check(long a,int n)
{
	int tr[n],i;
	if(n%2!=0)
		return 0;
	int index=n-1;
	do
	  {
	   tr[index]=a%10;
	   a = a/10;
	   index--;
	  }while(a!=0);
	int first=tr[0];
	int second=tr[1];
	for(i=2;i<n;i++)
	{
		if(i%2==0)
		{
			if(tr[i]!=first)
				return 0;
		}
		else
		{
			if(tr[i]!=second)
				return 0;
		}
	}
	if(i==n)
		return (n/2)-1;
	else
		return 0;
}
void fun(int cas,long a,long b)
{
	long temp,div,diff,k;
	int ndig,index,i,j,mindig,maxdig,count=0,flag=0;
	diff = b-a;
	//Find the length of the number
	div=10;
	ndig=0;
	temp=b;
	int c=0;
	do
	{
	maxdig=temp%10;
	temp = temp/10;
	ndig++;
	}while(temp!=0);
	//initialize an int array of size ndig
	int number[ndig];
	for(k=a;k<=b;k++)
	{
	  //convert the number to array
	  c=0;
	  flag=0;
	  temp = k;
	  index=ndig-1;
	  do
	  {
	   number[index]=temp%10;
	   temp = temp/10;
	   index--;
	  }while(temp!=0);
	  //process the array
	  for(j=1;j<ndig;j++)
	  {
			
		if(number[j]>number[0]&&number[j]<maxdig)
			{
			long x=number[j];
			for(i=j+1;i<ndig;i++)
			{
				x=x*10+number[i];
			}
			for(i=0;i<j;i++)
			{
				x=x*10+number[i];
			}
			//cout<<k<<" "<<x<<"\n";
			c++;
			}
		else if(number[j]==number[0]||number[j]==maxdig)
		{
			//form the number and check
			long x=number[j];
			for(i=j+1;i<ndig;i++)
			{
				x=x*10+number[i];
			}
			for(i=0;i<j;i++)
			{
				x=x*10+number[i];
			}
			if(x>k && x>=a && x<=b)
			{
				c++;
				//cout<<k<<" "<<x<<"\n";
			}
			
		}
	  }	
	  flag=check(k,ndig);
	  if(flag<=c)
	  	{ //cout<<"k "<<k<<" flag "<<flag<<"\n";
		  count=count+c-flag;
		}
	}
	cout<<"Case #"<<cas<<": "<<count<<"\n";	
}

int main()
{
	int n,i;
	long min,max;
	cin>>n;
	for(i=0;i<n;i++)
	{
		cin>>min>>max;
		fun(i+1,min,max);
	}
}
