#include<iostream>
#include<string.h>
#include<stdio.h>
using namespace std;
int main()
{
	int l,d,n,i,j,k,z,count=0,len,flag=0,count2=0,cpy;
	char a[5000][15];
	char b[500][1000];
	
	cin>>l>>d>>n;

	for(i=0;i<d;i++)//input library
	{
		scanf("%s",&a[i]);
	//gets(a[i]);
	}
	//cout<<"ENTER THE TEST CASES"<<endl;
	for(i=0;i<n;i++)//input test cases
	{
			    scanf("%s",&b[i]);
		//gets(b[i]);
	}
	for(i=0;i<n;i++)//loop for test cases
	{
		count2=0;
		for(z=0;z<d;z++)//loop for checkin all library
		{
			j=0;
			count=0;
			flag=0;
			while(count<l && flag!=1)
			{
				if(b[i][j]=='(')
				{
					j++;
					cpy=count;
					if(b[i][j]!=' ')
					{
						while(b[i][j]!=')')
						{
							if(a[z][cpy]==b[i][j])
							{
								count++;
							}
							j++;
						}
						if(cpy==count)
						{
							flag=1;
						}
					}
					j++;
				}
				else
				{
					if(b[i][j]!=' ')
					{
						if(a[z][count]==b[i][j])
						{
							count++;
						}
						else
						{
						    flag=1;
						}
					}
					j++;
				}

			}
			if(count==l && flag!=1)
			{
				count2++;
			}
		}
		cout<<"Case #"<<i+1<<": "<<count2<<endl;
	}
return 0;
}
