#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;

int main()
{
	int values[20];
	char pattern[20]="welcome to code jam";
	int n;
	cin>>n;
	cin.get();
	for(int i=0;i<n;i++)
	{
		char str[600];
		cin.getline(str,600);
		memset(values,0,20*sizeof(int));
		values[0]=1;
		int isize=strlen(str);
		for(int j=0;j<isize;j++)
		{
			for(int k=0;k<19;k++)
			{
				if(pattern[k]==str[j])
				{
					values[k+1]+=values[k];
					values[k+1]=values[k+1]%10000;
				}
			}
		}
		cout<<"Case #"<<i+1<<": ";
		printf("%04d\n",values[19]);
	}
}
