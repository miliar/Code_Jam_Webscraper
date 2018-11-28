#include<iostream>
#include<math.h>

using namespace std;

int digits(int a)
{
	int i;
	for(i=0;a!=0;i++)
	{
		a/=10;
	}
	
	return i;
	
}

int main()
{
	int k,*A,*B,i,j,a,*ar,num,temp,count=0,p,temp2;
	
	cin>>k;
	A=new int[k];
	B=new int[k];
		
	for(i=0;i<k;i++)
	{
		cin>>A[i]>>B[i];
	}

	cout<<endl;
		
	for(i=0;i<k;i++)
	{
		count=0;
		a=digits(A[i]);
		ar=new int[a];
		temp2=A[i];
						
		for(;temp2<=B[i];temp2++)
		{	
			A[i]=temp2;
			for(j=0;j<a;j++)
			{
				ar[a-j-1]=A[i]%10;
				A[i]/=10;
			}
		
			for(j=0;j<a;j++)
			{
				temp=ar[0];
				
				for(p=0;p<a-1;p++)
				{
					ar[p]=ar[p+1];
				}
				ar[a-1]=temp;
				
				num=0;
				
				for(p=0;p<a;p++)
				{
					num+=ar[p]*pow(10,a-p-1);
				}
								
				if(num<=B[i]&&num>temp2)
				{
					count++;
				}
			}
		}
				
		cout<<"Case #"<<i+1<<": "<<count<<endl;
	}
		
	return 0;
}
