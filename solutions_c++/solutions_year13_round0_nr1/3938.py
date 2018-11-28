//Author :Faisal


#include<stdio.h>
#include<iostream>
using namespace std;
int main()
{
     int tcases,newt,i,j,k,AW,BW,cwr,count=1;
     char array[4][4],fc;
     scanf("%d\n",&tcases);


while(tcases--){
               AW=0;
               BW=0;

             
	for(i=0;i<4;i++)
	{	
	scanf("%c%c%c%c \n",&array[i][0],&array[i][1],&array[i][2],&array[i][3]);		
	}

		k=0;
	          for(i=0;i<4;i++)
                  {
                    if((array[i][k]=='X'||array[i][k]=='T')&&((array[i][k+1]=='X'||array[i][k+1]=='T'))&&((array[i][k+2]=='X'||array[i][k	+2]=='T'))&&(array[i][k+3]=='X'||array[i][k+3]=='T')) {AW=1;break;}
                                                         
                                
               if((array[i][k]=='O'||array[i][k]=='T')&&((array[i][k+1]=='O'||array[i][k+1]=='T'))&&((array[i][k+2]=='O'||array[i][k+2]=='T'))&&(array[i][k+3]=='O'||array[i][k+3]=='T'))   {BW=1;break;}                      
                                      
                               
                                            
               }

	
		k=0;
if (AW!=1&& BW!=1){

	          for(i=0;i<4;i++)//  column OPERATION
                  {
                    if(((array[k][i]=='X'||array[k][i]=='T')&&((array[k+1][i]=='X'||array[k+1][i]=='T'))&&((array[k+2][i]=='X'||array[k+2][i]=='T'))&&(array[k+3][i]=='X'||array[k+3][i]=='T')))
                                                         
                                {AW=1;break;}
                    if(((array[k][i]=='O'||array[k][i]=='T')&&((array[k+1][i]=='O'||array[k+1][i]=='T'))&&((array[k+2][i]=='O'||array[k+2][i]=='T'))&&(array[k+3][i]=='O'||array[k+3][i]=='T')))
                                       
                                {BW=1;break;}
               }}


			i=0;k=0;

if (AW!=1&& BW!=1){
                    if(((array[k][i]=='X'||array[k][i]=='T')&&((array[k+1][i+1]=='X'||array[k+1][i+1]=='T'))&&((array[k+2][i+2]=='X'||array[k+2][i+2]=='T'))&&(array[k+3][i+3]=='X'||array[k+3][i+3]=='T')))
                                                         
                                AW=1;
                    if(((array[k][i]=='O'||array[k][i]=='T')&&((array[k+1][i+1]=='O'||array[k+1][i+1]=='T'))&&((array[k+2][i+2]=='O'||array[k+2][i+2]=='T'))&&(array[k+3][i+3]=='O'||array[k+3][i+3]=='T')))
                                       
                                BW=1;}

i=0;k=3;
if (AW!=1&& BW!=1){
                    if(((array[i][k]=='X'||array[i][k]=='T')&&((array[i+1][k-1]=='X'||array[i+1][k-1]=='T'))&&((array[i+2][k-2]=='X'||array[i+2][k-2]=='T'))&&(array[i+3][k-3]=='X'||array[i+3][k-3]=='T')))
                                                         
                                AW=1;
               if(((array[i][k]=='O'||array[i][k]=='T')&&((array[i+1][k-1]=='O'||array[i+1][k-1]=='T'))&&((array[i+2][k-2]=='O'||array[i+2][k-2]=='T'))&&(array[i+3][k-3]=='O'||array[i+3][k-3]=='T')))                        
                                      
                                BW=1;
}
cwr=0;
if (AW!=1&& BW!=1){
for (i=0;i<4;i++){
for (j=0;j<4;j++){
if (array[i][j]=='.')
cwr=1;
}
}

if (cwr == 1){
printf("Case #%d: Game has not completed\n",count);
}

else{

printf("Case #%d: Draw\n",count);

}

}

if (AW==1)
printf("Case #%d: X won\n",count);
else if (BW==1)
printf("Case #%d: O won\n",count);


count++;
}



}
