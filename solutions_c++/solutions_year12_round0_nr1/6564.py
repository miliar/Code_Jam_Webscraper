/*
   PROGRAM MADE USING BORLAND C++ 3.0
   GOOGLE CODE JAM QUALIFICATION ROUND 2012
   Date: April 14, 2012
   Programmer: JORGE HUGO RUIZ CARDONA
   Country: COLOMBIA
   E-mail: ruizgeorgeh@gmail.com

   Solution for Problem A - SPEAKING IN TONGUES
*/

#include <conio.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <ctype.h>

FILE *input, *output;

int main(void)
{
 int T=0,testC,n,i,l;
 char G[105],S[105],lineT[5],CODE[26];
 strcpy(CODE,"yhesocvxduiglbkrztnwjpfmaq");
 input=fopen("c:\\codejam\\problema\\small.in","r");
 output=fopen("c:\\codejam\\problema\\small.out","w");
 fseek(input, 0, SEEK_SET);
 fgets(lineT,5,input);
 n=strlen(lineT)-1;
 for(i=0;i<n;i++)
 {
   T+=(lineT[i]-48)*pow10(n-i-1);
 }
 for(i=0;i<T;i++)
 {
   fgets(G,105,input);
   n=strlen(G);
   for(l=0;l<n;l++)
   {
     if(G[l]=='\n')
       S[l]=NULL;
     else
     if(isalnum(G[l]))
     {
       S[l]=CODE[G[l]-97];
     }
     else
     {
       if(G[l]==32)
	 S[l]=G[l];
     }
   }

   S[l]=NULL;
   fprintf(output,"Case #%d: %s\n",i+1,S);

 }
 fclose(input);
 fclose(output);

 return 0;
}