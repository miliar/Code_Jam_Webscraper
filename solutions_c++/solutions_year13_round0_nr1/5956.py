#include<stdlib.h>
#include<stdio.h>

char arr[4][4];
bool isWin(int x,int y);

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	
	
	int T;
	scanf("%d\n",&T);
	for(int t=0;t<T;t++)
	{
		for(int i=0;i<4;i++)
		{
			scanf("%s",arr[i]);
		}
		
		bool win = false;
		char winC;
		for(int i=0;i<4;i++)
		{
			if(win==true)
				break;
			for(int j=0;j<4;j++)
			{
				if(isWin(i,j))
				{
					win = true;
					winC = arr[i][j];
					break;
				}

			}
		}
		
		bool hasEmpty = false;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(arr[i][j]=='.')
				{
					hasEmpty = true;
				}
			}
		}
		
		if(win)
		{
			printf("Case #%d: %c won\n",t+1,winC);
		}
		else
		{
			if(hasEmpty)
			{
				printf("Case #%d: Game has not completed\n",t+1);
			}
			else
			{
				printf("Case #%d: Draw\n",t+1);
			}
		}
/*
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				printf("%c ",arr[i][j]);
			}
			printf("\n");
		}
*/
	}

	return 0;
}

bool isWin(int x,int y)
{
	bool ret = false;
	char w = arr[x][y];
	if(w=='X'||w=='O')
	{
		int len = 1;
		int xx = x;
		int yy = y;
		while(1)
		{
			
			if(--yy>=0)
			{
				if(arr[xx][yy]==w||arr[xx][yy]=='T')
				{
					len++;
				}
				else
				{
					break;
				}
			}
			else
			{
				break;
			}
		}

		xx = x;
		yy = y;
		while(1)
		{
			
			if(++yy<=3)
			{
				if(arr[xx][yy]==w||arr[xx][yy]=='T')
				{
					len++;
				}
				else
				{
					break;
				}
			}
			else
			{
				break;
			}
		}

		if(len==4)
		{
			ret = true;
		}

		len = 1;
		xx = x;
		yy = y;
		while(1)
		{
			
			if(--xx>=0)
			{
				if(arr[xx][yy]==w||arr[xx][yy]=='T')
				{
					len++;
				}
				else
				{
					break;
				}
			}
			else
			{
				break;
			}
		}
		xx = x;
		yy = y;
		while(1)
		{
			
			if(++xx<=3)
			{
				if(arr[xx][yy]==w||arr[xx][yy]=='T')
				{
					len++;
				}
				else
				{
					break;
				}
			}
			else
			{
				break;
			}
		}

		if(len==4)
		{
			ret = true;
		}

		len = 1;
		xx = x;
		yy = y;
		while(1)
		{
			
			if(--yy>=0 && --xx>=0)
			{
				if(arr[xx][yy]==w||arr[xx][yy]=='T')
				{
					len++;
				}
				else
				{
					break;
				}
			}
			else
			{
				break;
			}
		}
		xx = x;
		yy = y;
		while(1)
		{
			
			if(++yy<=3 && ++xx<=3)
			{
				if(arr[xx][yy]==w||arr[xx][yy]=='T')
				{
					len++;
				}
				else
				{
					break;
				}
			}
			else
			{
				break;
			}
		}

		if(len==4)
		{
			ret = true;
		}

		len = 1;
		xx = x;
		yy = y;
		while(1)
		{
			
			if(--yy>=0 && ++xx<=3)
			{
				if(arr[xx][yy]==w||arr[xx][yy]=='T')
				{
					len++;
				}
				else
				{
					break;
				}
			}
			else
			{
				break;
			}
		}
		xx = x;
		yy = y;
		while(1)
		{
			
			if(++yy<=3 && --xx>=0)
			{
				if(arr[xx][yy]==w||arr[xx][yy]=='T')
				{
					len++;
				}
				else
				{
					break;
				}
			}
			else
			{
				break;
			}
		}

		if(len==4)
		{
			ret = true;
		}
	}//end of if
	
	return ret;
}