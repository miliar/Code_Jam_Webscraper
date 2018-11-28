#include<iostream>
#include<stdlib.h>
#include<algo.h>
#include<math.h>
#include<stdio.h>
#include<string.h>
using namespace std;

int findChar(char *str,int len,char c)
{
	for(int i=0;i<len;i++)
		if(str[i]==c)
			return i+1;
		return 0;
}

int main()
{
	int T,C,D,N,i,j,x,y;
	char c[10][10],d[10][10];
	char n[15];
	char stack[10];
	int top=-1;
	cin>>T;
	for(int t=0;t<T;t++)
	{
		top=-1;
		cin>>C;
		for(i=0;i<C;i++)
			cin>>c[i];
		cin>>D;
		for(i=0;i<D;i++)
			cin>>d[i];
		cin>>N;
		for(i=0;i<N;i++)
			cin>>n[i];
			
		for(i=0;i<N;i++)
		{
			stack[++top]=n[i];
			if(top>0)
			{
				if(C==1)
				{
					
					if((stack[top]==c[0][0] && stack[top-1]==c[0][1]) || (stack[top]==c[0][1] && stack[top-1]==c[0][0]))
					{
						top-=2;
						stack[++top]=c[0][2];
					}
				}
				if(D==1)
				{
					x=findChar(stack,top+1,d[0][0]);
					y=findChar(stack,top+1,d[0][1]);
					if(x && y && x!=y)
						top=-1;
				}
			}
		}
		cout<<"Case #"<<t+1<<": [";
		if(top>-1)
		{
			for(i=0;i<top;i++)
				cout<<stack[i]<<", ";
			cout<<stack[top];
		}
		cout<<"]"<<endl;
		
	}
	return 0;
}