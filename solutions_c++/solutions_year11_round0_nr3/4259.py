#include<iostream>
#include<cstdio>
#include<math.h>
using namespace std;
void insertion_sort(int n, int *a);
int main()
{
	int T;
	cin>>T;
	//int a;
	//int b;
	//cin>>a;
	//cin>>b;
	//printf("a ^ b = %d\n", a^b);
	
	for(int i=0;i<T;i++)
	{
		int numbers;
		cin>>numbers;
		int array_numbers[1001];
		int sum;
		sum=0;
		for(int j=0;j<numbers;j++)
		{
			cin>>array_numbers[j];
			sum=sum+array_numbers[j];
		}
		//if((sum%2)==0)
		int solution_found=0;
			insertion_sort(numbers,array_numbers);
			for(int k=0;k<numbers-1;k++)
			{
				int xor1=0;
				for(int k1=0;k1<=k;k1++)
				{
					xor1=xor1^array_numbers[k1];
				}
				int xor2=0;
				for(int k2=k+1;k2<numbers;k2++)
				{
					xor2=xor2^array_numbers[k2];
				}
				if(xor1==xor2)
				{
					int max_val=0;
					for(int k3=k+1;k3<numbers;k3++)
						{max_val=max_val+array_numbers[k3];}
					cout<<"Case #"<<i+1<<": "<<max_val<<"\n";
					solution_found=1;
					break;
				}
			}
		
		if(solution_found!=1)
		{
			cout<<"Case #"<<i+1<<": "<<"NO\n";
			solution_found=0;
		}
	
	}
	
	
	
	return 0;
}

void insertion_sort(int n, int *a)
{
	for(int i=1;i<n;i++)
	{	
		int j=i;
		int current=a[i];
		while(a[j-1]>current && j>0)
		{
		j--;
		a[j+1]=a[j];
		}
		a[j]=current;
	}
}
