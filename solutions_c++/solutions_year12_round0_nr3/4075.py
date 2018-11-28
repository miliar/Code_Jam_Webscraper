// dance.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
using namespace std;
int _tmain(int argc, _TCHAR* argv[])
{
	freopen("C-small-attempt1.in","r",stdin);
	freopen("b.txt","w",stdout);
	int T;
	cin>>T;
	int casess[100];
	int a,b;
	int y=0;
	int temp;
	int temp_o;
	for(int i=1;i<=T;i++)
	{
		y=0;
		cin>>a;
		cin>>b;
		for(int k=a;k<=b;k++)
		{
			temp=k;
			int j=10;
			while(k/j!=0)
			{
				j=j*10;
			}
			j=j/10;
			for(int q=10;q<=j;q=q*10)
			{
				
				temp=k/q+(k%q)*(j/q*10);
				if(temp<=b&&temp>k)
				{
					y++;
					
				
				}
			}
			
		}
		casess[i]=y;
		
	}
	for(int i=1;i<=T;i++)
	cout<<"Case #"<<i<<": "<<casess[i]<<endl;

	return 0;
}

