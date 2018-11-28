#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<string.h>
using namespace std;
int main()
{
	int t,A,B,n,m;
	char str[1000];
	scanf("%d",&t);
	char c,c1;
	int count=0;
	for(int i=0;i<t;i++)
	{
		count=0;
		scanf("%d %d",&A,&B);
		for(int j=A;j<B;j++)
		{
			n=sprintf(str,"%d",j);
			for(int k=0;k<strlen(str);k++)
			{
				c=str[strlen(str)-1];			
				for(int l=0;l<strlen(str);l++)
				{
					c1=str[l];
					str[l]=c;
					c=c1;
				}
				m=atoi(str);
				if(A <= j &&  j < m && m <= B) 		
					count++;
			}
		}
		cout << "Case #"<<i+1<<": "<<count << endl;
	}
}
