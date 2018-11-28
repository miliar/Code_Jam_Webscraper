/*
 * Author :Krishna Kumar Tiwari
 * Problem Code:  Tic-Tac-Toe 
 * Programming Language : C++
*/

#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <map>
#include <set>
#include <stack>
#include <list>
#include <vector>
#include <queue>
using namespace std;
int main()
{
     int test,newt,i,j,k,A,B,chr,COUNT=1;
     char array[4][4],fc;
     scanf("%d\n",&test);


while(test--){
               A=0;
               B=0;

             
	for(i=0;i<4;i++)
	{	
	scanf("%c%c%c%c \n",&array[i][0],&array[i][1],&array[i][2],&array[i][3]);		
	}

		k=0;
	          for(i=0;i<4;i++)
                  {
                    if((array[i][k]=='X'||array[i][k]=='T')&&((array[i][k+1]=='X'||array[i][k+1]=='T'))&&((array[i][k+2]=='X'||array[i][k	+2]=='T'))&&(array[i][k+3]=='X'||array[i][k+3]=='T')) {A=1;break;}
                                                         
                                
               if((array[i][k]=='O'||array[i][k]=='T')&&((array[i][k+1]=='O'||array[i][k+1]=='T'))&&((array[i][k+2]=='O'||array[i][k+2]=='T'))&&(array[i][k+3]=='O'||array[i][k+3]=='T'))   {B=1;break;}                      
                                      
                               
                                            
               }

	
		k=0;
if (A!=1&& B!=1){

	          for(i=0;i<4;i++)
                  {
                    if(((array[k][i]=='X'||array[k][i]=='T')&&((array[k+1][i]=='X'||array[k+1][i]=='T'))&&((array[k+2][i]=='X'||array[k+2][i]=='T'))&&(array[k+3][i]=='X'||array[k+3][i]=='T')))
                                                         
                                {A=1;break;}
                    if(((array[k][i]=='O'||array[k][i]=='T')&&((array[k+1][i]=='O'||array[k+1][i]=='T'))&&((array[k+2][i]=='O'||array[k+2][i]=='T'))&&(array[k+3][i]=='O'||array[k+3][i]=='T')))
                                       
                                {B=1;break;}
               }}


			i=0;k=0;
if (A!=1&& B!=1){
                    if(((array[k][i]=='X'||array[k][i]=='T')&&((array[k+1][i+1]=='X'||array[k+1][i+1]=='T'))&&((array[k+2][i+2]=='X'||array[k+2][i+2]=='T'))&&(array[k+3][i+3]=='X'||array[k+3][i+3]=='T')))
                                                         
                                A=1;
                    if(((array[k][i]=='O'||array[k][i]=='T')&&((array[k+1][i+1]=='O'||array[k+1][i+1]=='T'))&&((array[k+2][i+2]=='O'||array[k+2][i+2]=='T'))&&(array[k+3][i+3]=='O'||array[k+3][i+3]=='T')))
                                       
                                B=1;}

i=0;k=3;
if (A!=1&& B!=1){
                    if(((array[i][k]=='X'||array[i][k]=='T')&&((array[i+1][k-1]=='X'||array[i+1][k-1]=='T'))&&((array[i+2][k-2]=='X'||array[i+2][k-2]=='T'))&&(array[i+3][k-3]=='X'||array[i+3][k-3]=='T')))
                                                         
                                A=1;
               if(((array[i][k]=='O'||array[i][k]=='T')&&((array[i+1][k-1]=='O'||array[i+1][k-1]=='T'))&&((array[i+2][k-2]=='O'||array[i+2][k-2]=='T'))&&(array[i+3][k-3]=='O'||array[i+3][k-3]=='T')))                        
                                      
                                B=1;
}
chr=0;
if (A!=1&& B!=1){
for (i=0;i<4;i++){
for (j=0;j<4;j++){
if (array[i][j]=='.')
chr=1;
}
}

if (chr == 1){
printf("Case #%d: Game has not completed\n",COUNT);
}

else{

printf("Case #%d: Draw\n",COUNT);

}

}

if (A==1)
printf("Case #%d: X won\n",COUNT);
else if (B==1)
printf("Case #%d: O won\n",COUNT);
COUNT++;
}
}
