#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;
int main()
{
	freopen("D://A-large.in","r",stdin);
	freopen("D://output.txt","w",stdout);
	int i, j, k, l;
	string str[4];
	cin >> k;
	bool x, o;
	for(j=1;j<=k;j++)
	{
		x=o=0;
		printf("Case #%d: ",j);
		for(i=0;i<4;i++)
		{
			cin >> str[i];
		}
		for(i=0;i<4;i++)
		{
			if(!x)
			{
				for(l=0;l<4;l++)
				{
					if(str[i][l]=='O' || str[i][l]=='.')
					{
						break;
					}
				}
				if(l==4)
				{
					x=1;
				}
			}
			if(!x)
			{
				for(l=0;l<4;l++)
				{
					if(str[l][i]=='O' || str[l][i]=='.')
					{
						break;
					}
				}
				if(l==4)
				{
					x=1;
				}
			}
			if(!o)
			{
				for(l=0;l<4;l++)
				{
					if(str[i][l]=='X' || str[i][l]=='.')
					{
						break;
					}
				}
				if(l==4)
				{
					o=1;
				}
			}
			if(!o)
			{
				for(l=0;l<4;l++)
				{
					if(str[l][i]=='X' || str[l][i]=='.')
					{
						break;
					}
				}
				if(l==4)
				{
					o=1;
				}
			}
		}
		if(!o)
		{
			for(i=0;i<4;i++)
			{
				if(str[i][i]=='X' || str[i][i]=='.')
				{
					break;
				}
			}
			if(i==4)
			{
				o=1;
			}
		}
		if(!o)
		{
			for(i=0;i<4;i++)
			{
				if(str[i][3-i]=='X' || str[i][3-i]=='.')
				{
					break;
				}
			}
			if(i==4)
			{
				o=1;
			}
		}
		if(!x)
		{
			for(i=0;i<4;i++)
			{
				if(str[i][i]=='O' || str[i][i]=='.')
				{
					break;
				}
			}
			if(i==4)
			{
				x=1;
			}
		}
		if(!x)
		{
			for(i=0;i<4;i++)
			{
				if(str[i][3-i]=='O' || str[i][3-i]=='.')
				{
					break;
				}
			}
			if(i==4)
			{
				x=1;
			}
		}
		if(o && x)
		{
			printf("Draw\n");
		}
		else if(o && !x)
		{
			printf("O won\n");
		}
		else if(!o && x)
		{
			printf("X won\n");
		}
		else if(!o && !x)
		{
			for(i=0;i<4;i++)
			{
				for(l=0;l<4;l++)
				{
					if(str[i][l]=='.')
					{
						break;
					}
				}
				if(l!=4)
				{
					break;
				}
			}
			if(i==4)
			{
				printf("Draw\n");
			}
			else
			{
				printf("Game has not completed\n");
			}
		}
	}
	return 0;
}