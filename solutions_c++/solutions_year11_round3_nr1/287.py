#include<iostream>
using namespace std;
int main()
{
	long long int ttt;
	cin>>ttt;
	for(long long int tt=1;tt<=ttt;tt++)
	{
		cout<<"Case #"<<tt<<":\n";
		int row,col;
		cin>>row>>col;
		char d[100][100];
		for(int i=0;i<row;i++)
			cin>>d[i];
		int flag=1;
		for(int i=0;i<row;i++)
		{
			for(int j=0;j<col;j++)
			{
				if(d[i][j]=='#')
				{
					if(i==row-1 || j==col-1 || d[i][j+1]!='#' || d[i+1][j]!='#' || d[i+1][j+1]!='#')
					{
						flag=0;
						break;
					}
					else
					{
						d[i][j]=d[i+1][j+1]='/';
						d[i][j+1]=d[i+1][j]='\\';
					}
				}
			}
			if(flag==0)break;
		}
		if(flag==0)cout<<"Impossible\n";
		else
		{
			for(int i=0;i<row;i++)
			{for(int j=0;j<col;j++)
				cout<<d[i][j];
				cout<<endl;
			}
		}

	}


}
