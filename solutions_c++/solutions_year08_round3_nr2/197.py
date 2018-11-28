#include<iostream>
#include<vector>
#include<string>
#include<algorithm>

using namespace std;

void convert(char *s,int *a)
{
	int l=strlen(s);
	for(int i=0;i<l;i++)
	{
		a[i*2]=s[i]-48;
		a[i*2+1]=0;
	}
}

int check(int *a,int j)
{
	for(int i=1,k=1;k<=j;i+=2,k++)
	{	
		if(a[i]!=2)
			return 0;
	}
	return 1;
}
int eva(int *a,int j)
{
	long long int sum=0,num=a[0];
	int op1=1,oper;
	for(int i=2;i<=j*2;i+=2)
	{
		if(a[i-1]==1 || a[i-1]==2)
		{
			switch(op1)
			{
				case 1: sum+=num; break;
				case 2: sum-=num; break;
			}
			num=0;
			op1=a[i-1];
		}
		num=num*10+a[i];	
	}
	switch(op1)
	{
		case 1: sum+=num; break;
		case 2: sum-=num; break;
	}
	if(sum%2==0 || sum%3==0 || sum%5==0 || sum%7==0)
		return 1;
	else
		return 0;
}	

int main()
{
	long long int n;
	cin>>n;

	for(int i=1;i<=n;i++)
	{
		int arr[82];
		char ch,str[41];;
		int j;
		
		cin>>str;
		convert(str,arr);
		j=strlen(str)-1;

		long long int ugly=0;
		ugly+=eva(arr,j);
				
		while(check(arr,j)==0)		
		{
			int k=1;		
			arr[k]++;
			do
			{
				if(arr[k]==3)
				{
					arr[k]=0;
					arr[k+2]++;	
					k+=2;
				}
				else 
					break;
			}while(1);
			
			ugly+=eva(arr,j);
		}
		cout<<"Case #"<<i<<": "<<ugly<<endl;			
	}
}
