#include<iostream>
#include<stdlib.h>
#include<math.h>
using namespace std;

int isPresent(char str[],int len,char x)
{
	int i;
	for(i=0;i<=len;i++)
		if(str[i]==x)
			return i+1;
		return 0;
}

int main()
{
	int T,C,D,N,i,j,k;
	char c[40][4],d[40][4];
	char n[101];
	char stack[108]={0};
	int top=-1;
	int x,y;
	cin>>T;
	for(k=0;k<T;k++)
	{
		for(i=0;i<108;i++)
			stack[i]=0;
		//Read inputs
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
				for(j=0;j<C;j++)
				{
					if((stack[top]==c[j][0] && stack[top-1]==c[j][1]) || (stack[top]==c[j][1] && stack[top-1]==c[j][0]))
					{
						top-=2;
						stack[++top]=c[0][2];
					}
				}
				for(j=0;j<D;j++)
				{
					x=isPresent(stack,top,d[0][0]);
					y=isPresent(stack,top,d[0][1]);
					if(x && y && x!=y)
					{
						top=-1;
						break;
					}
				}
			}
		}
		cout<<"Case #"<<k+1<<": [";
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
