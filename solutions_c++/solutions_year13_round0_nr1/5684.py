#if 1

#include<stdio.h>
#include<conio.h>
#include<math.h>
#include <string.h>
#include<iostream>

int main(){     
	int t;

	int ans[10];
	
	scanf("%d ",&t);
		 
		   for(int i=0;i<t;i++)
		   {
                 char in[4][4];
				 int dot=0;
				 for(int i=0;i<4;i++)
					 for(int j=0;j<4;j++)
						{
							scanf("%c ",&in[i][j]);
							if(in[i][j]=='.') dot++;
					    }

				 ans[i]=0;

				 if((in[0][0]=='X'||in[0][0]=='T')&&(in[0][1]=='X'||in[0][1]=='T')&&(in[0][2]=='X'||in[0][2]=='T')&&(in[0][3]=='X'||in[0][3]=='T'))
					 ans[i]=1;
				 if((in[1][0]=='X'||in[1][0]=='T')&&(in[1][1]=='X'||in[1][1]=='T')&&(in[1][2]=='X'||in[1][2]=='T')&&(in[1][3]=='X'||in[1][3]=='T'))
					 ans[i]=1;
				 if((in[2][0]=='X'||in[2][0]=='T')&&(in[2][1]=='X'||in[2][1]=='T')&&(in[2][2]=='X'||in[2][2]=='T')&&(in[2][3]=='X'||in[2][3]=='T'))
					 ans[i]=1;
				 if((in[3][0]=='X'||in[3][0]=='T')&&(in[3][1]=='X'||in[3][1]=='T')&&(in[3][2]=='X'||in[3][2]=='T')&&(in[3][3]=='X'||in[3][3]=='T'))
					 ans[i]=1;

				 if((in[0][0]=='X'||in[0][0]=='T')&&(in[1][0]=='X'||in[1][0]=='T')&&(in[2][0]=='X'||in[2][0]=='T')&&(in[3][0]=='X'||in[3][0]=='T'))
					 ans[i]=1;
				 if((in[0][1]=='X'||in[0][1]=='T')&&(in[1][1]=='X'||in[1][1]=='T')&&(in[2][1]=='X'||in[2][1]=='T')&&(in[3][1]=='X'||in[3][1]=='T'))
					 ans[i]=1;
				 if((in[0][2]=='X'||in[0][2]=='T')&&(in[1][2]=='X'||in[1][2]=='T')&&(in[2][2]=='X'||in[2][2]=='T')&&(in[3][2]=='X'||in[3][2]=='T'))
					 ans[i]=1;
				 if((in[0][3]=='X'||in[0][3]=='T')&&(in[1][3]=='X'||in[1][3]=='T')&&(in[2][3]=='X'||in[2][3]=='T')&&(in[3][3]=='X'||in[3][3]=='T'))
					 ans[i]=1;
				 if((in[0][0]=='X'||in[0][0]=='T')&&(in[1][1]=='X'||in[1][1]=='T')&&(in[2][2]=='X'||in[2][2]=='T')&&(in[3][3]=='X'||in[3][3]=='T'))
					 ans[i]=1;
				 if((in[0][3]=='X'||in[0][3]=='T')&&(in[1][2]=='X'||in[1][2]=='T')&&(in[2][1]=='X'||in[2][1]=='T')&&(in[3][0]=='X'||in[3][0]=='T'))
					 ans[i]=1;


				  if((in[0][0]=='O'||in[0][0]=='T')&&(in[0][1]=='O'||in[0][1]=='T')&&(in[0][2]=='O'||in[0][2]=='T')&&(in[0][3]=='O'||in[0][3]=='T'))
					 ans[i]=2;
				 if((in[1][0]=='O'||in[1][0]=='T')&&(in[1][1]=='O'||in[1][1]=='T')&&(in[1][2]=='O'||in[1][2]=='T')&&(in[1][3]=='O'||in[1][3]=='T'))
					 ans[i]=2;
				 if((in[2][0]=='O'||in[2][0]=='T')&&(in[2][1]=='O'||in[2][1]=='T')&&(in[2][2]=='O'||in[2][2]=='T')&&(in[2][3]=='O'||in[2][3]=='T'))
					 ans[i]=2;
				 if((in[3][0]=='O'||in[3][0]=='T')&&(in[3][1]=='O'||in[3][1]=='T')&&(in[3][2]=='O'||in[3][2]=='T')&&(in[3][3]=='O'||in[3][3]=='T'))
					 ans[i]=2;

				 if((in[0][0]=='O'||in[0][0]=='T')&&(in[1][0]=='O'||in[1][0]=='T')&&(in[2][0]=='O'||in[2][0]=='T')&&(in[3][0]=='O'||in[3][0]=='T'))
					 ans[i]=2;
				 if((in[0][1]=='O'||in[0][1]=='T')&&(in[1][1]=='O'||in[1][1]=='T')&&(in[2][1]=='O'||in[2][1]=='T')&&(in[3][1]=='O'||in[3][1]=='T'))
					 ans[i]=2;
				 if((in[0][2]=='O'||in[0][2]=='T')&&(in[1][2]=='O'||in[1][2]=='T')&&(in[2][2]=='O'||in[2][2]=='T')&&(in[3][2]=='O'||in[3][2]=='T'))
					 ans[i]=2;
				 if((in[0][3]=='O'||in[0][3]=='T')&&(in[1][3]=='O'||in[1][3]=='T')&&(in[2][3]=='O'||in[2][3]=='T')&&(in[3][3]=='O'||in[3][3]=='T'))
					 ans[i]=2;
				 if((in[0][0]=='O'||in[0][0]=='T')&&(in[1][1]=='O'||in[1][1]=='T')&&(in[2][2]=='O'||in[2][2]=='T')&&(in[3][3]=='O'||in[3][3]=='T'))
					 ans[i]=2;
				 if((in[0][3]=='O'||in[0][3]=='T')&&(in[1][2]=='O'||in[1][2]=='T')&&(in[2][1]=='O'||in[2][1]=='T')&&(in[3][0]=='O'||in[3][0]=='T'))
					 ans[i]=2;

				 if(ans[i]!=1&&ans[i]!=2&&dot) ans[i]=4;
				 if(ans[i]!=1&&ans[i]!=2&&!dot) ans[i]=3;

				 //printf("Case #%d:",i+1);     
/*Case #1: X won
Case #2: Draw
Case #3: Game has not completed
Case #4: O won
Case #5: O won
Case #6: O won*/
					//	if(ans[i]==1) printf(" X won\n");
					//	if(ans[i]==2) printf(" O won\n");
					//	if(ans[i]==3) printf(" Draw\n");
						//if(ans[i]==4) printf(" Game has not completed\n");
					//	if(ans[i]==4) printf(" Game has not completed\n");

				// printf("%d\n",ans[i]);
						//char dum;
						//scanf("%c",&dum);
		   }
		        for(int i=0;i<t;i++)
					{
						printf("Case #%d:",i+1);     
/*Case #1: X won
Case #2: Draw
Case #3: Game has not completed
Case #4: O won
Case #5: O won
Case #6: O won*/
						if(ans[i]==1) printf(" X won\n");
						if(ans[i]==2) printf(" O won\n");
						if(ans[i]==3) printf(" Draw\n");
						//if(ans[i]==4) printf(" Game has not completed\n");
						if(ans[i]==4) printf(" Game has not completed\n");
				    
				    }
		   
		   getch();
           return 0;
}

#endif