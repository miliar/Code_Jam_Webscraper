#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<string.h>
#include<limits.h>
#include<map>
#include<queue>
#include<vector>
using namespace std;
int main()
{
     int TC,newt,i,j,k,awins,bwins,ch,count=1;
     char ar[4][4],fc;
     scanf("%d\n",&TC);


while(TC--){
               awins=0;
               bwins=0;

             
	for(i=0;i<4;i++)
	{	
	scanf("%c%c%c%c \n",&ar[i][0],&ar[i][1],&ar[i][2],&ar[i][3]);		
	}

		k=0;
	          for(i=0;i<4;i++)//// row
                  {
                    if((ar[i][k]=='X'||ar[i][k]=='T')&&((ar[i][k+1]=='X'||ar[i][k+1]=='T'))&&((ar[i][k+2]=='X'||ar[i][k	+2]=='T'))&&(ar[i][k+3]=='X'||ar[i][k+3]=='T')) {awins=1;break;}
                                                         
                                
               if((ar[i][k]=='O'||ar[i][k]=='T')&&((ar[i][k+1]=='O'||ar[i][k+1]=='T'))&&((ar[i][k+2]=='O'||ar[i][k+2]=='T'))&&(ar[i][k+3]=='O'||ar[i][k+3]=='T'))   {bwins=1;break;}                      
                                      
                               
                                            
               }

	
		k=0;
if (awins!=1&& bwins!=1){

	          for(i=0;i<4;i++)//  column
                  {
                    if(((ar[k][i]=='X'||ar[k][i]=='T')&&((ar[k+1][i]=='X'||ar[k+1][i]=='T'))&&((ar[k+2][i]=='X'||ar[k+2][i]=='T'))&&(ar[k+3][i]=='X'||ar[k+3][i]=='T')))
                                                         
                                {awins=1;break;}
                    if(((ar[k][i]=='O'||ar[k][i]=='T')&&((ar[k+1][i]=='O'||ar[k+1][i]=='T'))&&((ar[k+2][i]=='O'||ar[k+2][i]=='T'))&&(ar[k+3][i]=='O'||ar[k+3][i]=='T')))
                                       
                                {bwins=1;break;}
               }}

///////////////////////////////////////////////////diagonal

			i=0;k=0;//diagonal left to right

if (awins!=1&& bwins!=1){
                    if(((ar[k][i]=='X'||ar[k][i]=='T')&&((ar[k+1][i+1]=='X'||ar[k+1][i+1]=='T'))&&((ar[k+2][i+2]=='X'||ar[k+2][i+2]=='T'))&&(ar[k+3][i+3]=='X'||ar[k+3][i+3]=='T')))
                                                         
                                awins=1;
                    if(((ar[k][i]=='O'||ar[k][i]=='T')&&((ar[k+1][i+1]=='O'||ar[k+1][i+1]=='T'))&&((ar[k+2][i+2]=='O'||ar[k+2][i+2]=='T'))&&(ar[k+3][i+3]=='O'||ar[k+3][i+3]=='T')))
                                       
                                bwins=1;}

i=0;k=3;
if (awins!=1&& bwins!=1){
                    if(((ar[i][k]=='X'||ar[i][k]=='T')&&((ar[i+1][k-1]=='X'||ar[i+1][k-1]=='T'))&&((ar[i+2][k-2]=='X'||ar[i+2][k-2]=='T'))&&(ar[i+3][k-3]=='X'||ar[i+3][k-3]=='T')))
                                                         
                                awins=1;
               if(((ar[i][k]=='O'||ar[i][k]=='T')&&((ar[i+1][k-1]=='O'||ar[i+1][k-1]=='T'))&&((ar[i+2][k-2]=='O'||ar[i+2][k-2]=='T'))&&(ar[i+3][k-3]=='O'||ar[i+3][k-3]=='T')))                        
                                      
                                bwins=1;
}
ch=0;
if (awins!=1&& bwins!=1){
for (i=0;i<4;i++){
for (j=0;j<4;j++){
if (ar[i][j]=='.')
ch=1;
}
}

if (ch == 1){
printf("Case #%d: Game has not completed\n",count);
}

else{

printf("Case #%d: Draw\n",count);

}

}

if (awins==1)
printf("Case #%d: X won\n",count);
else if (bwins==1)
printf("Case #%d: O won\n",count);

/*
	for (i=0;i<4;i++){
		for (j=0;j<4;j++){
		printf("%c",ar[i][j]);		
		}
	}

*/
//printf("%d",TC);
//scanf("%c",&fc);
count++;
}



}
