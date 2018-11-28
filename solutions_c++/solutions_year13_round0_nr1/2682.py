#include <iostream>
#include <vector>
#include <string>
#include <cstdio>
#include <algorithm>

using namespace std;

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int t;
	scanf("%d", &t);
	for( int p=0; p<t; p++)
	{
		bool flagx=false;
		bool flago=false;
		string temp[4];
		for( int j=0; j<4; j++)
			cin>>temp[j];
		for( int j=0; j<4; j++)
		{
			for( int k=0; k<4; k++)
			{
				if(temp[j][k]!='X' && temp[j][k]!='T')
				{
					break;
				}
				if(k==3)
				{
					flagx=true;
				}
			}
		}
		for( int j=0; j<4; j++)
		{
			for( int k=0; k<4; k++)
			{
				if(temp[j][k]!='O' && temp[j][k]!='T')
				{
					break;
				}
				if(k==3)
				{
					flago=true;
				}
			}
		}
		for( int j=0; j<4; j++)
		{
			for( int k=0; k<4; k++)
			{
				if(temp[k][j]!='O' && temp[k][j]!='T')
				{
					break;
				}
				if(k==3)
				{
					flago=true;
				}
			}
		}
		for( int j=0; j<4; j++)
		{
			for( int k=0; k<4; k++)
			{
				if(temp[k][j]!='X' && temp[k][j]!='T')
				{
					break;
				}
				if(k==3)
				{
					flagx=true;
				}
			}
		}
		for( int k=0; k<4; k++)
		{
			if(temp[k][k]!='X' && temp[k][k]!='T')
			{
				break;
			}
			if(k==3)
			{
				flagx=true;
			}
		}
		for( int k=0; k<4; k++)
		{
			if(temp[k][k]!='O' && temp[k][k]!='T')
			{
				break;
			}
			if(k==3)
			{
				flago=true;
			}
		}
		for( int k=0; k<4; k++)
		{
			if(temp[k][3-k]!='X' && temp[k][3-k]!='T')
			{
				break;
			}
			if(k==3)
			{
				flagx=true;
			}
		}
		for( int k=0; k<4; k++)
		{
			if(temp[k][3-k]!='O' && temp[k][3-k]!='T')
			{
				break;
			}
			if(k==3)
			{
				flago=true;
			}
		}
		bool flag=false;
		for( int i=0; i<4; i++)
		{
			for( int j=0; j<4; j++)
			{
				if(temp[i][j]=='.')
					flag=true;
			}
		}
		if(flago==true)
			printf("Case #%d: O won\n", p+1);
		else if(flagx==true)
			printf("Case #%d: X won\n", p+1);
		else if(flag==true)
			printf("Case #%d: Game has not completed\n", p+1);
		else
			printf("Case #%d: Draw\n", p+1);
	}
}
