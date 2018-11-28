#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

char *InpFilename = "C:\\VINOD\\B-large.in"; 
char *OutFilename = "C:\\VINOD\\B-large-1.txt"; 
#define LINE_MAX 100


int main()
{
 FILE *fpr, *fpw; 
 fpr=fopen(InpFilename,"r");
 fpw=fopen(OutFilename,"w"); 
 char G[LINE_MAX];
  
 int T = 0, i = 1;
 fscanf(fpr,"%s", G);
 T = atoi(G);
 int N, S, p, totalPoints[LINE_MAX][3], dP = 0, tpValues[LINE_MAX][2][3];
 
 
 while((fscanf(fpr,"%s", G) == 1) && i <= T)
 {
     N = atoi(G);
     fscanf(fpr,"%s", G);
     S = atoi(G);
     fscanf(fpr,"%s", G);
     p = atoi(G);
     
     dP = 0; 
     
     for(int j=0; j < N; j++)
     {
        fscanf(fpr,"%s", G);       
        totalPoints[j][0] = atoi(G);
        totalPoints[j][1] = totalPoints[j][0]/3;
        totalPoints[j][2] = totalPoints[j][0]%3;
       
        
        /** increase the number of count who have value > p by default **/
        if(totalPoints[j][1] >= p )
        {
             dP++;
        }
        
        if(totalPoints[j][2] == 0)
        {
            /** add (x,x,x) n (x-1, x, x+1) **/
            tpValues[j][0][0] = tpValues[j][0][1] = tpValues[j][0][2] = totalPoints[j][1];
            
            if(totalPoints[j][1] != 0 )
            { 
             tpValues[j][1][0] = totalPoints[j][1] - 1;
             tpValues[j][1][1] = totalPoints[j][1];
             tpValues[j][1][2] = totalPoints[j][1] + 1;
            }
            else
            {
              tpValues[j][1][0] = tpValues[j][1][1] = tpValues[j][1][2] = totalPoints[j][1];
            }
           
               
        }
        else if(totalPoints[j][2] == 1)
        {
            /** add (x,x,x+1) n (x-1, x+1, x+1) **/
            tpValues[j][0][0] = totalPoints[j][1];
            tpValues[j][0][1] = totalPoints[j][1];
            tpValues[j][0][2] = totalPoints[j][1] + 1;
            
            tpValues[j][1][0] = totalPoints[j][1] - 1;
            tpValues[j][1][1] = totalPoints[j][1] + 1;
            tpValues[j][1][2] = totalPoints[j][1] + 1;
        }
        else
        {
            /** add (x,x+1,x+1) n (x, x, x+2) **/
            tpValues[j][0][0] = totalPoints[j][1];
            tpValues[j][0][1] = totalPoints[j][1] + 1;
            tpValues[j][0][2] = totalPoints[j][1] + 1;
            
            if(totalPoints[j][1] != 9)
            {
              tpValues[j][1][0] = totalPoints[j][1];
              tpValues[j][1][1] = totalPoints[j][1];
              tpValues[j][1][2] = totalPoints[j][1] + 2;
            }
            else
            {
               tpValues[j][1][0] = totalPoints[j][1];
               tpValues[j][1][1] = totalPoints[j][1] + 1;
               tpValues[j][1][2] = totalPoints[j][1] + 1; 
            }
        }
        
     } //end of int = j forloop, getting all points and reading them
    
     
     /** Now we have N, S, p, TP[0][j] **/
     //If non-dP values are greater than given 'S', then find S values in non-dP 
     int S22 = 0, S10 = 0, cP1 = 0, cP1s = 0, tdP = 0, nP = 0, flg = 0, cpIn = 0;
     for(int j =0; j<N ; j++)
     {
        if(p - totalPoints[j][1] == 2 && totalPoints[j][2] == 2 && tpValues[j][1][2] >= p) 
        {
            S22++; 
        }
        else if(p - totalPoints[j][1] == 1 )
        {
           // printf("  tpv: %d", tpValues[j][1][2]);
            if(totalPoints[j][2] == 0 && tpValues[j][1][2] >= p) { S10++; }
            else if(tpValues[j][1][2] >= p && tpValues[j][0][2] < p) { cP1s++; }
            if(tpValues[j][0][2] >= p && tpValues[j][1][2] < p) cP1++;
            
        }
        else if(p - totalPoints[j][1] > 2) 
        { 
             //nothing 
             nP++;
        }
        else if(p - totalPoints[j][1] <= 0)
        {
            tdP++;
            //printf("\ntdp loop: p: %d, d: %d, r: %d, val: %d", p, totalPoints[j][1], totalPoints[j][2], totalPoints[j][0]);
        }
        
        if(p - totalPoints[j][1] == 2 || p - totalPoints[j][1] == 1)
        if(tpValues[j][0][2] >= p && tpValues[j][1][2] >= p) cpIn++;
        
     }
     
         
     if( (N - tdP) > S) 
     {
                 
         int Sx = S22 + S10 + cP1s;
         if( Sx >= S) 
         {
             fprintf(fpw,"Case #%d: %d\n", i, tdP + cP1 + S + cpIn);
         }
         else if( Sx + cpIn >= S)
         {
             fprintf(fpw,"Case #%d: %d\n", i, tdP + cP1 + Sx + cpIn);
         }
         else
         {
             fprintf(fpw,"Case #%d: %d\n", i, tdP + cP1 + Sx + cpIn );
         }
     }
     else fprintf(fpw,"Case #%d: %d\n",i , tdP + cP1 + S22 + S10 + cP1s + cpIn );
    // printf("\n\nS22 = %d, S10 = %d, cP1 = %d, cP1s = %d, tdP = %d, nP = %d, cpIn = %d, dP = %d\n\n-----------------------------------------------\n\n", S22, S10, cP1, cP1s, tdP, nP, cpIn, dP);
    
    i++;
 }
 
 fclose(fpr);
 fclose(fpw);

 
 return 1;
}


