#include<iostream>
#include<cstdio>
#include<math.h>
#include<string.h>
#include<stdlib.h>

using namespace std;

int sumsp(int num1,int num2)
{
	return ((num1&(~num2))|(num2&(~num1)));
}

int main()
{
	int ch;//cout<<sumsp(sumsp(4,5),3)<<" "<<sumsp(1,2);
	cin>>ch;
	for(int test=1;test<=ch;test++)
	{
		int N;
		cin>>N;
		int arr[100]={0};
		int comb=1;
		for(int i=1;i<=N;i++)
		{
			cin>>arr[i];
			comb*=2;
		}
		int max=0;
		for(int i=1;i<comb;i++)
		{
			int valpat=0,valsan=0,maxval=0;
			int ptr=0;
			int j=i;
			for(int k=1;k<=N;k++)
			{
				if((j&1)==1)
				{
					valpat=sumsp(valpat,arr[N-ptr]);
				}
				else
				{	
					valsan=sumsp(valsan,arr[N-ptr]);
					//cout<<valsan<<endl;
					maxval+=arr[N-ptr];
				}
				j=j>>1;
				ptr++;
			}
			if(valsan==valpat)
				if(maxval>max)
					max=maxval;
		}
		//cout<<max;
		if(max==0)
			cout<<"Case #"<<test<<": NO"<<endl;
		else
			cout<<"Case #"<<test<<": "<<max<<endl;
			
	}
	return 0;
}
				
		
