#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;


int tt;
long long int N;
int Pd,Pg;
int main( )
{
	freopen( "d:/A-large.in", "r", stdin );
	freopen( "d:/solution4a.out", "w", stdout );

	cin>>tt;
	for(int i = 0;i < tt;i ++)
	{
		cin>>N>>Pd>>Pg;
		if(Pg == 0 && Pd == 0)
		{
			cout<<"Case #"<<(i+1)<<": Possible"<<endl;
			continue;
		}
		else if(Pg == 100 && Pd  == 100)
		{
			cout<<"Case #"<<(i+1)<<": Possible"<<endl;
			continue;
		}
		else if(Pg == 0 || Pg == 100)
		{
			cout<<"Case #"<<(i+1)<<": Broken"<<endl;
			continue;
		}
		else
		{
			int flag = 0;
			if(N < 100)
			{
				for(int j = 1; j <= N;j ++)
				{
					if(j*Pd%100 == 0)
					{
						flag = 1;
						break;
					}
				}
				if(flag)
				{
					cout<<"Case #"<<(i+1)<<": Possible"<<endl;
					continue;
				}
				else
					cout<<"Case #"<<(i+1)<<": Broken"<<endl;
			}
			else
			{
				cout<<"Case #"<<(i+1)<<": Possible"<<endl;
			}
		}
	}
	return 0;
}