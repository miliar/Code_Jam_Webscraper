#include <iostream>
#include <cstdio>
using namespace std;
int main()
{
	int T;
	scanf("%i", &T);
	for(int k=1; k<=T; k++)
	{
		char m[4][4];
		for(int j=0; j<4; j++)
		scanf("%s", m[j]);
		
		int dot=0;
		int flag=0;
		int xc[4]={0,0,0,0};
		int oc[4]={0,0,0,0};
		int xr[4]={0,0,0,0};
		int orr[4]={0,0,0,0};
		int xd[2]={0,0};
		int od[2]={0,0};
		
		for(int i=0; i<4; i++)
		{
			for(int j=0; j<4; j++)
			{
				if(m[i][j]=='X')
				{
					xc[j]++;
					xr[i]++;
					if(i==j)
					xd[0]++;
					if(i+j==3)
					xd[1]++;
				}
				else if(m[i][j]=='O')
				{
					oc[j]++;
					orr[i]++;
					if(i==j)
					od[0]++;
					if(i+j==3)
					od[1]++;
				}
				else if(m[i][j]=='.')
				dot++;
				else if(m[i][j]=='T')
				{
					xc[j]++;
					xr[i]++;
					oc[j]++;
					orr[i]++;
					if(i==j)
					{
						xd[0]++;
						od[0]++;
					}
					if(i+j==3)
					{
						xd[1]++;
						od[1]++;
					}
				}
			}
		}
		for(int p=0; p<4; p++)
		{
			if(xr[p]==4 || xc[p]==4)
			{
				printf("%s", "Case #");
				printf("%i", k);
				printf("%s\n", ": X won");
				flag=1;
				break;
			}
			else if(orr[p]==4 || oc[p]==4)
			{
				printf("%s", "Case #");
				printf("%i", k);
				printf("%s\n", ": O won");
				flag=1;
				break;
			}
			
			if(p<2)
			{
				if(xd[p]==4)
				{
					printf("%s", "Case #");
					printf("%i", k);
					printf("%s\n", ": X won");
					flag=1;
					break;
				}
				else if(od[p]==4)
				{
					printf("%s", "Case #");
					printf("%i", k);
					printf("%s\n", ": O won");
					flag=1;
					break;
				}
			}
		}
		if(flag==0)
		{
		if(dot==0)
		{
			printf("%s", "Case #");
			printf("%i", k);
			printf("%s\n", ": Draw");
			
		}
		else
		{
			printf("%s", "Case #");
			printf("%i", k);
			printf("%s\n", ": Game has not completed");
			
		}
		}
	}
			
	return 0;
}
