#include<iostream>
#include<cstdio>

using namespace std;

char a[5][5];

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	
	int T;
	int Case = 1;
	scanf("%d",&T);
	while(T--)
	{		
		for(int i=0;i<4;i++)
		{
			scanf("%s", &a[i]);
		}
		
		bool xwon=false,owon=false,draw=false,dotpresent=false;
		
		for(int i=0;i<4;i++)
		{
			bool xpresent = false;
			bool opresent = false;
			for(int j=0;j<4;j++)
			{
				if(a[i][j]=='.')
				{
					dotpresent =true;
					xpresent = false;
					opresent = false;
					break;
				}
				else if(a[i][j]=='X')
				xpresent = true;
				else if(a[i][j]=='O')
				opresent = true;
			}
			if(xpresent && opresent)
			continue;
			else if(xpresent)
			{
				xwon = true;
				break;
			}
			else if(opresent)
			{
				owon = true;
				break;
			}
		}
		//printf("Case#%d: xwon %d owon%d draw%d dotpresent%d\n",Case,xwon,owon,draw,dotpresent);
		for(int j=0;j<4;j++)
		{
			bool xpresent = false;
			bool opresent = false;
			for(int i=0;i<4;i++)
			{
				if(a[i][j]=='.')
				{
					dotpresent =true;
					xpresent = false;
					opresent = false;
					break;
				}
				else if(a[i][j]=='X')
				xpresent = true;
				else if(a[i][j]=='O')
				opresent = true;
			}
			if(xpresent && opresent)
			continue;
			else if(xpresent)
			{
				xwon = true;
				break;
			}
			else if(opresent)
			{
				owon = true;
				break;
			}
		}
		//printf("Case#%d: xwon %d owon%d draw%d dotpresent%d\n",Case,xwon,owon,draw,dotpresent);
			bool xpresent = false;
			bool opresent = false;
			for(int i=0;i<4;i++)
			{
				if(a[i][i]=='.')
				{
					dotpresent =true;
					xpresent = false;
					opresent = false;
					break;
				}
				else if(a[i][i]=='X')
				xpresent = true;
				else if(a[i][i]=='O')
				opresent = true;
			}
			if(xpresent && opresent)
			{
			
			}
			else if(xpresent)
			{
				xwon = true;
				
			}
			else if(opresent)
			{
				owon = true;
				
			}
		//printf("Case#%d: xwon %d owon%d draw%d dotpresent%d\n",Case,xwon,owon,draw,dotpresent);
			xpresent = false;
			opresent = false;
			for(int i=0,j=3;i<4;i++,j--)
			{
				if(a[i][j]=='.')
				{
					dotpresent =true;
					xpresent = false;
					opresent = false;
					break;
				}
				else if(a[i][j]=='X')
				xpresent = true;
				else if(a[i][j]=='O')
				opresent = true;
			}
			if(xpresent && opresent)
			{
			
			}
			else if(xpresent)
			{
				xwon = true;
				
			}
			else if(opresent)
			{
				owon = true;
				
			}
			
			//printf("Case#%d: xwon %d owon%d draw%d dotpresent%d\n",Case,xwon,owon,draw,dotpresent);
			
		if(xwon==false && owon==false && dotpresent==false)
		draw=true;
		
		if(xwon)
		printf("Case #%d: X won\n",Case);
		else if(owon)
		printf("Case #%d: O won\n",Case);
		else if(draw)
		printf("Case #%d: Draw\n",Case);
		else
		printf("Case #%d: Game has not completed\n",Case);
		
		
		Case++;
	}
	return 0;
}
