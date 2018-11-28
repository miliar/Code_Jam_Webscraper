#include<stdio.h>
#include<stdlib.h>

int main()
{
  int nTestCases;
  scanf("%d",&nTestCases);
  for(int i=0;i<nTestCases;i++)
	{
	  int r,c;
	  scanf("%d",&r);
	  scanf("%d",&c);
	  char Inpict[52][52];
	  //char Outpict[52][52];
	  int nBlue=0;
	  for(int j=0;j<r;j++)
		{
		  char str[52];
		  scanf("%s",str);
		  for(int k=0;k<c;k++)
			{
			  Inpict[j][k]=str[k];
			  if(str[k]=='#')
				{
				  nBlue++;
				}
			}
		}
	  if((nBlue % 4) != 0)
		{
		  printf("Case #%d:\nImpossible\n",i+1);
		  continue;
		}
	  bool br=false;
	  for(int j=0;j<r;j++)
		{
		  for(int k=0;k<c;k++)
			{
			  if(Inpict[j][k]=='#')
				{
				  if(Inpict[j][k+1] == '.' || Inpict[j+1][k]=='.' || Inpict[j+1][k+1]=='.')
					{
					  br=true;
					  break;
					}
				  Inpict[j][k]='/';
				  Inpict[j][k+1]='\\';
				  Inpict[j+1][k]='\\';
				  Inpict[j+1][k+1]='/';
				}
			}
		  if(br)
			{
			  break;
			}
		}
	  if(br)
		{
		  printf("Case #%d:\nImpossible\n",i+1);
		   continue;
		}
	  printf("Case #%d:\n",i+1);
	  for(int j=0;j<r;j++)
		{
		  for(int k=0;k<c;k++)
			{
			  printf("%c",Inpict[j][k]);
			}
		  printf("\n");
		}
	}
  return 0;
}
