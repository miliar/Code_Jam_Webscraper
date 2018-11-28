#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		char ch=' ';char input[4];
        int computation[10],val;
        for(int j=0;j<10;j++)
        computation[j]=1;
		for(int j=0;j<4;j++)
		{
			scanf("%s",input);
			for(int k=0;k<4;k++)
			{
				ch=input[k];
				if(ch=='X')
				val=2;
				else if(ch=='O')
				val=3;
				else if(ch=='T')
				val=1;
				else val=0;
				computation[j]*=val;
				computation[k+4]*=val;
				if(j==k)
				computation[8]*=val;
				if(j+k==3)
				computation[9]*=val;
			}

		}
	bool incomplete=false,checked=false;
	string s="Draw";
	for(int j=0;j<10;j++)
	{
		if(!incomplete && computation[j]==0)
			incomplete=true;
		if(computation[j]%6==0)
			continue;
		else if(computation[j]%2==0 && computation[j]>=8)
			{
				s="X won";
				checked=true;
				break;
			}
		else if(computation[j]%3==0 && computation[j]>=27)
			{
				s="O won";
				checked=true;
				break;
			}
		
	}
	if(incomplete && !checked)
		s="Game has not completed";
	cout<<"Case #"<<i<<": "<<s<<"\n";
	
	}
}
