#include <iostream>
#include<sstream>
#include <cmath>
using namespace std;
char str[55][55];
int main ()
{

	    int t;
	    int sum;
		bool flag=true;
		int r,c;
		freopen("C:\\Users\\NAZI\\Desktop\\A-large.in", "rt", stdin);
		freopen("C:\\Users\\NAZI\\Desktop\\A-large.out", "wt", stdout);
	cin>>t;
	for(int i=0;i<t;i++)
	{//样例个数
	    cin>>r>>c;
		sum=0;
		for(int j=0;j<r;j++)
		{
			for(int k=0;k<c;k++)
			{
				cin>>str[j][k];
				if(str[j][k]=='#')
				{
					sum++;
				}
			}
		}

		if(sum%4!=0)
		{
			cout<<"Case #"<<i+1<<":"<<endl;
			cout<<"Impossible"<<endl;
		}
		else
		{
			flag=true;
			for(int j=0;j<r;j++)
			{//
				for(int k=0;k<c;k++)
				{
					if(str[j][k]=='#')
					{///
						if(str[j][k+1]=='#'&&str[j+1][k]=='#' && str[j+1][k+1]=='#')
						{
							str[j][k]='/';
							str[j][k+1]='\\';
							str[j+1][k]='\\';
							str[j+1][k+1]='/';
						}
						else
						{	
							flag=false;
							break;

						}
					}
				}///
					if(!flag)
					{
						break;
					}
			}//
			if(!flag)
			{
				cout<<"Case #"<<i+1<<":"<<endl;
				cout<<"Impossible"<<endl;
			}
			else if(flag)
			{
				cout<<"Case #"<<i+1<<":"<<endl;
				for(int j=0;j<r;j++)
				{
					for(int k=0;k<c;k++)
					{
						cout<<str[j][k];
					}
					cout<<endl;
				}
			}
		}


	}//样例个数

	
	return 0;
}

