#include<iostream>
#include<cstdio>
#include<math.h>
#include<string.h>
#include<stdlib.h>

using namespace std;

int main()
{
	int ch;
	cin>>ch;
	for(int z=1;z<=ch;z++)
	{
		char combine[300][3];
		char oppose[300][2];
		char str[500];
		int num_combine;
		cin>>num_combine;
		num_combine*=2;
		for(int i=1;i<=num_combine;i+=2)
		{
			getchar();
			scanf("%s",combine[i]);
			combine[i+1][0]=combine[i][1];
			combine[i+1][1]=combine[i][0];
			combine[i+1][2]=combine[i][2];
		}
		int num_opp;
		cin>>num_opp;
		num_opp*=2;
		for(int i=1;i<num_opp;i+=2)
		{
			getchar();
			scanf("%s",oppose[i]);
			oppose[i+1][0]=oppose[i][1];
			oppose[i+1][1]=oppose[i][0];
		}
		int num_string;
		cin>>num_string;
		getchar();
		scanf("%s",str);
		char stack[500];
		int top=-1;
		for(int i=0;i<num_string;i++)
		{
			if(top==-1)
			{
				top++;
				stack[top]=str[i];
				continue;
			}
			else
			{
				top++;
				stack[top]=str[i];
				int flag=1;
				for(int i=1;i<=num_combine;i++)
				{
					if(stack[top]==combine[i][1] && stack[top-1]==combine[i][0])
					{
						top--;
						stack[top]=combine[i][2];
						flag=2;
						break;
					}
				}
				if(flag==1)
				{
					//for oppose
					for(int i=1;i<=num_opp;i++)
					{
						if(stack[top]==oppose[i][1])
						{
							for(int j=0;j<top;j++)
							{
								if(stack[j]==oppose[i][0])
								{
									top=-1;
									break;
								}
							}
						}
					}
				}
			}
			
			
		}
		cout<<"Case #"<<z<<": [";
		for(int i=0;i<=top;i++)
		{
			cout<<stack[i];
			if(i<top)
				cout<<", ";
		}
		cout<<"]"<<endl;
	}
	return 0;
}
