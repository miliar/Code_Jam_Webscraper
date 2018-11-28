#include <iostream>
#include <string>
#include <vector>
#include<cstdio>
#include<math.h>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int o=1;o<=t;o++)
	{
	int n;
	cin>>n;
	int *a=new int[n];
	int *b=new int[n];
	int total=0;
	total=0;
	for(int i=0;i<n;i++)
	{
		
		cin>>a[i];
		cin>>b[i];
		if(i!=0)
		{
			for(int j=1;j<=i;j++)
			{
				if((a[i]<a[i-j] && b[i]>b[i-j]) || (a[i]>a[i-j] && b[i]<b[i-j]))
				{
					total++;
				}
			}
		}
	
	}
	cout<<"Case #"<<o<<": "<<total<<"\n";
	}
}
