#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<string.h>
using namespace std;
int main()
{
     int test_case,newt,I,J,K,AWINNER,BWINNER,charactyer,result=1;
     char AAR[4][4],fchar;
     scanf("%d\n",&test_case);


while(test_case--){
               AWINNER=0;
               BWINNER=0;

             
	for(I=0;I<4;I++)
	{	
	scanf("%c%c%c%c \n",&AAR[I][0],&AAR[I][1],&AAR[I][2],&AAR[I][3]);		
	}

		K=0;
	          for(I=0;I<4;I++)// ROW
                  {
                    if((AAR[I][K]=='X'||AAR[I][K]=='T')&&((AAR[I][K+1]=='X'||AAR[I][K+1]=='T'))&&((AAR[I][K+2]=='X'||AAR[I][K	+2]=='T'))&&(AAR[I][K+3]=='X'||AAR[I][K+3]=='T')) {AWINNER=1;break;}
                                                         
                                
               if((AAR[I][K]=='O'||AAR[I][K]=='T')&&((AAR[I][K+1]=='O'||AAR[I][K+1]=='T'))&&((AAR[I][K+2]=='O'||AAR[I][K+2]=='T'))&&(AAR[I][K+3]=='O'||AAR[I][K+3]=='T'))   {BWINNER=1;break;}                      
                                      
                               
                                            
               }

	
		K=0;
if (AWINNER!=1&& BWINNER!=1){

	          for(I=0;I<4;I++)
                  {
                    if(((AAR[K][I]=='X'||AAR[K][I]=='T')&&((AAR[K+1][I]=='X'||AAR[K+1][I]=='T'))&&((AAR[K+2][I]=='X'||AAR[K+2][I]=='T'))&&(AAR[K+3][I]=='X'||AAR[K+3][I]=='T')))
                                                         
                                {AWINNER=1;break;}
                    if(((AAR[K][I]=='O'||AAR[K][I]=='T')&&((AAR[K+1][I]=='O'||AAR[K+1][I]=='T'))&&((AAR[K+2][I]=='O'||AAR[K+2][I]=='T'))&&(AAR[K+3][I]=='O'||AAR[K+3][I]=='T')))
                                       
                                {BWINNER=1;break;}
               }}


			I=0;K=0;

if (AWINNER!=1&& BWINNER!=1){
                    if(((AAR[K][I]=='X'||AAR[K][I]=='T')&&((AAR[K+1][I+1]=='X'||AAR[K+1][I+1]=='T'))&&((AAR[K+2][I+2]=='X'||AAR[K+2][I+2]=='T'))&&(AAR[K+3][I+3]=='X'||AAR[K+3][I+3]=='T')))
                                                         
                                AWINNER=1;
                    if(((AAR[K][I]=='O'||AAR[K][I]=='T')&&((AAR[K+1][I+1]=='O'||AAR[K+1][I+1]=='T'))&&((AAR[K+2][I+2]=='O'||AAR[K+2][I+2]=='T'))&&(AAR[K+3][I+3]=='O'||AAR[K+3][I+3]=='T')))
                                       
                                BWINNER=1;}

I=0;K=3;
if (AWINNER!=1&& BWINNER!=1){
                    if(((AAR[I][K]=='X'||AAR[I][K]=='T')&&((AAR[I+1][K-1]=='X'||AAR[I+1][K-1]=='T'))&&((AAR[I+2][K-2]=='X'||AAR[I+2][K-2]=='T'))&&(AAR[I+3][K-3]=='X'||AAR[I+3][K-3]=='T')))
                                                         
                                AWINNER=1;
               if(((AAR[I][K]=='O'||AAR[I][K]=='T')&&((AAR[I+1][K-1]=='O'||AAR[I+1][K-1]=='T'))&&((AAR[I+2][K-2]=='O'||AAR[I+2][K-2]=='T'))&&(AAR[I+3][K-3]=='O'||AAR[I+3][K-3]=='T')))                        
                                      
                                BWINNER=1;
}
charactyer=0;
if (AWINNER!=1&& BWINNER!=1){
for (I=0;I<4;I++){
for (J=0;J<4;J++){
if (AAR[I][J]=='.')
charactyer=1;
}
}

if (charactyer == 1){
printf("Case #%d: Game has not completed\n",result);
}

else{

printf("Case #%d: Draw\n",result);

}

}

if (AWINNER==1)
printf("Case #%d: X won\n",result);
else if (BWINNER==1)
printf("Case #%d: O won\n",result);


result++;
}



}
