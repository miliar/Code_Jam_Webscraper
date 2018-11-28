#include<stdio.h>
#include<string.h>
#include <iostream>
#include<stdlib.h>
using namespace std;
const int num=4;
char map[num][num];
int main()
{
	freopen("A-small-attempt1.in","rt",stdin);
	freopen("A-small-attempt1.out","wt",stdout);
	int T;
	scanf("%d",&T);
	int cas=0;
	while(T--)
	{
		int flag=1,flag2=0,flag3=0,flag4=0;
	    for(int i=0;i<num;i++)
		{
		   scanf("%s",map[i]);
		  for(int j=0;j<4;j++)
			  if(map[i][j]=='.')
				  flag=0;
		}
		for(int i=0;i<4;i++)
			{  
		      for(int j=0;j<4;j++)
			{ 
                  if(map[i][j]=='T')
				  {
				    if(j+3<4)
					{
					  if(map[i][j+1]==map[i][j+2]&&map[i][j+2]==map[i][j+3])
					  {
					    if(map[i][j+1]=='O')
						flag3=3;
						else 
							flag4=4;
						if(flag3==3||flag4==4)
						break;
					  }
					}
					if(j+3<4&&i+3<4)
					{
					  if(map[i+1][j+1]==map[i+2][j+2]&&map[i+2][j+2]==map[i+3][j+3])
					  {
					    if(map[i+1][j+1]=='O')
						flag3=3;
						else 
							flag4=4;
						if(flag3==3||flag4==4)
						break;
					  }
					}
					if(i+3<4)
					{
					  if(map[i+1][j]==map[i+2][j]&&map[i+2][j]==map[i+3][j])
					  {
					    if(map[i+1][j]=='O')
						flag3=3;
						else 
							flag4=4;
						if(flag3==3||flag4==4)
						break;
					  }
					}
					if(i+3<4&&j-3>=0)
					{
					  if(map[i+1][j-1]==map[i+2][j-2]&&map[i+2][j-2]==map[i+3][j-3])
					  {
					    if(map[i+1][j-1]=='O')
						flag3=3;
						else 
							flag4=4;
						if(flag3==3||flag4==4)
						break;
					  }
					}
				  }
				  else if(map[i][j]!='.')
				  {
				    if(j+3<4)
					{
					  if(map[i][j]==map[i][j+1]&&map[i][j+1]==map[i][j+2]&&map[i][j+2]==map[i][j+3])
					  {
					    if(map[i][j+1]=='O')
						flag3=3;
						else 
							flag4=4;
						if(flag3==3||flag4==4)
						break;
					  }
					  else 
					  {
						  char aa,bb;
						  int num1=1;
						  aa=map[i][j];
						  for(int k=1;k<4;k++)
						  {
						    if(aa!=map[i][j+k])
								bb=map[i][j+k];
							else num1++;
						  }
						  if(num1==3&&bb=='T')
						  {
						  if(map[i][j]=='O')
						flag3=3;
						else 
							flag4=4;
						if(flag3==3||flag4==4)
						break;
						  }
					  }
					}
					if(j+3<4&&i+3<4)
					{
					  if(map[i][j]==map[i+1][j+1]&&map[i+1][j+1]==map[i+2][j+2]&&map[i+2][j+2]==map[i+3][j+3])
					  {
					    if(map[i+1][j+1]=='O')
						flag3=3;
						else 
							flag4=4;
						if(flag3==3||flag4==4)
						break;
					  }
					  else
					  {
					     char aa,bb;
						  int num1=1;
						  aa=map[i][j];
						  for(int k=1;k<4;k++)
						  {
						    if(aa!=map[i+k][j+k])
								bb=map[i+k][j+k];
							else num1++;
						  }
						  if(num1==3&&bb=='T')
						  {
						  if(map[i][j]=='O')
						flag3=3;
						else 
							flag4=4;
						if(flag3==3||flag4==4)
						break;
						  }
					  }
					}
					if(i+3<4)
					{
					  if(map[i][j]==map[i+1][j]&&map[i+1][j]==map[i+2][j]&&map[i+2][j]==map[i+3][j])
					  {
					    if(map[i+1][j]=='O')
						flag3=3;
						else 
							flag4=4;
						if(flag3==3||flag4==4)
						break;
					  }
					  else
					  {
					      char aa,bb;
						  int num1=1;
						  aa=map[i][j];
						  for(int k=1;k<4;k++)
						  {
						    if(aa!=map[i+k][j])
								bb=map[i+k][j];
							else num1++;
						  }
						  if(num1==3&&bb=='T')
						  {
						  if(map[i][j]=='O')
						flag3=3;
						else 
							flag4=4;
						if(flag3==3||flag4==4)
						break;
						  }
					  }
					}
					if(i+3<4&&j-3>=0)
					{
					  if(map[i][j]==map[i+1][j-1]&&map[i+1][j-1]==map[i+2][j-2]&&map[i+2][j-2]==map[i+3][j-3])
					  {
					    if(map[i+1][j-1]=='O')
						flag3=3;
						else 
							flag4=4;
						if(flag3==3||flag4==4)
						break;
					  }
					  else
					  {
					      char aa,bb;
						  int num1=1;
						  aa=map[i][j];
						  for(int k=1;k<4;k++)
						  {
						    if(aa!=map[i+k][j-k])
								bb=map[i+k][j-k];
							else num1++;
						  }
						  if(num1==3&&bb=='T')
						  {
						  if(map[i][j]=='O')
						    flag3=3;
						    else 
							flag4=4;
						if(flag3==3||flag4==4)
						break;
						  }
					  }
					}
				  }
	 	    }
			  if(flag3==3||flag4==4)
				  break;
		}
		printf("Case #%d: ",++cas);
		if(flag3==3)
	    printf("O won\n");
		else if(flag4==4)
			printf("X won\n");
		else if(!flag)
		 printf("Game has not completed\n");
		else if(flag) 
			printf("Draw\n");

	}
return 0;
}