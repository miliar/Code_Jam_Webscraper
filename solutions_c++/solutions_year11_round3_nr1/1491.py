#include <iostream>
#include <fstream>
#include <string>
#include <cctype>
#include <stack>
using namespace std;
int main()
{
	freopen("D:\\codejam\\A-large.in","rt",stdin);
	freopen("D:\\codejam\\A-small.out","wt",stdout);
	int T;
	cin>>T;
	char arry[55][55],e;
	for (int i=1;i<=T;i++)
	{
		for(int w=0;w<50;w++)
			for(int q=0;q<50;q++)
				arry[w][q]=0;
		cout<<"Case #"<<i<<":"<<endl;
		int C,R,flag=1;
		cin>>R>>C;
		for (int j=1;j<=R;j++)
		{
			for( int k=1;k<=C;k++)
			{
				while(cin.get(e)&&e=='\n') {}
				arry[j][k]=e;
			}
		}
		for (int j=1;j<=R;j++)
		{
			for( int k=1;k<=C;k++)
			{
				if(arry[j][k]=='#'&&arry[j+1][k]=='#'&&arry[j][k+1]=='#'&&arry[j+1][k+1]=='#')
				{
					arry[j][k]='/';
					arry[j][k+1]='\\';
					arry[j+1][k]='\\';
					arry[j+1][k+1]='/';

				}
			}
		}
		for (int j=1;j<=R;j++)
		{
			for( int k=1;k<=C;k++)
			{
				if(arry[j][k]=='#') 
				{
					cout<<"Impossible"<<endl;
					flag=0;
					break;
				}
				if(!flag) break;
			}
			if(!flag) break;
		}
		if(flag)
		{
			for (int j=1;j<=R;j++)
			{
				for( int k=1;k<=C;k++)
				{
					cout<<arry[j][k];
				}
				cout<<endl;
			}
		}


	}

	return 0;
}