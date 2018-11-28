#include<iostream>
#include<string.h>
using namespace std;
char stack[102];
int top=-1;
void push(char ch)
{
	top++;
	stack[top]=ch;
}
void pop()
{
	top--;
}
void empty()
{
	top=-1;
}
int main()
{
	int t,p=1,i,l;
	cin>>t;
	while(t)
	{
		t--;
		int c,d,n;
		cin>>c;
		int j;
		char combine[c][4];
		for(i=1;i<=c;i++)
			cin>>combine[i-1];
		//cout<<combine[0];
		cin>>d;
		char oppose[d][3];
		for(i=1;i<=d;i++)
			cin>>oppose[i-1];
		//cout<<oppose[0];
		cin>>n;
		char s[n+1];
		cin>>s;
		//cout<<s;
		for(l=0;l<n;l++)
		{
		//	cout<<s[l]<<"\n";
			push(s[l]);
			for(i=0;i<c;i++)
			{
				if((stack[top]==combine[i][0] && stack[top-1]==combine[i][1]) || (stack[top]==combine[i][1] && stack[top-1]==combine[i][0]))
				{
					pop();pop();
					push(combine[i][2]);
					break;
				}
			}
			for(i=0;i<d;i++)
			{
				if(stack[top]==oppose[i][0])
				{
					for(j=0;j<=top;j++)
					{
						if(stack[j]==oppose[i][1])
						{empty();break;}
					}
				}
				if(stack[top]==oppose[i][1])
				{
					for(j=0;j<=top;j++)
					{
						if(stack[j]==oppose[i][0])
						{empty();break;}
					}
				}
			}
		}
		cout<<"Case #"<<p<<": [";
		for(j=0;j<top;j++)
			cout<<stack[j]<<", ";
		if(top!=-1)
		cout<<stack[top]<<"]\n";
		else cout<<"]\n";
		p++;
 		empty();
	}
	return 0;
}