#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cstdio>
using namespace std;
int main()
{
	int i,l,d,n,j,k,m;
	cin>>l>>d>>n;
	getchar();
	char dict[d+5][l+5];
	for(i=0;i<d;i++)
	{
		gets(dict[i]);
	}

	string f;
	int index=0,found=0;
	for(i=0;i<n;i++)
	{
		cin>>f;
		int len=f.length();
		
		int ct=0;
		for(j=0;j<d;j++)
		{
			int useful=1;
			index=0;
			
			
			for(k=0;k<l;k++)
			{
				found=1;
				char ch=dict[j][k];
				char temp=f[index];
				if(temp!=')' && temp!='(')
				{
					if(temp!=ch)
					{
					found=0;
					}
				}	
			
				else if(temp=='(')
				{
					found=0;
					while(f[index]!=')')
					{
						index++;
						char tt=f[index];
						if(tt==ch)found=1;
					}
				}
				if(found==0)
				{
					useful=0;
					break;
				}
				
				
				
				index++;
			}
		if(useful==1)ct++;
		}
		cout<<"Case #"<<i+1<<": "<<ct<<"\n";
		
	}
}
