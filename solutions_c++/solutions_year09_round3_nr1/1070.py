#include<stdio.h>
#include<iostream.h>
#include<string.h>
#include<math.h>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>

bool isUpperCase(char c){return c>='A' && c<='Z';}
bool isLowerCase(char c){return c>='a' && c<='z';}
bool isLetter(char c){return c>='A' && c<='Z' || c>='a' && c<='z';}
bool isDigit(char c){return c>='0' && c<='9';}
char toLowerCase(char c){return (isUpperCase(c))?(c+32):c;}
char toUpperCase(char c){return (isLowerCase(c))?(c-32):c;}

FILE *fin, *fout;

int D,L,N, H, W;






int n;

int c[250];
char digit[65];

main(int argc, char *argv[])
{
  
   int i,j,k,l,td, num=1 ;
   
   unsigned long long sum,temp;
	//freopen(argv[1],"r",stdin);freopen(argv[2],"w",stdout);
	int testcase;
   for(j=0;j<249;++j)
      c[j] = -1;
   //for(j=0;j<65;++j)
      digit[0] = '\0';

   fin = fopen(argv[1], "r");
   fout = fopen(argv[2], "w");

   fscanf(fin,"%d\n",&N);
   
   printf("\ntest case - %d\n",N); 
   
   
   for(k=1; k<=N;k++)
   {
       char str[100];

    for(j=0;j<249;++j)
      c[j] = -1;
   for(j=0;j<65;++j)
      digit[j] = '\0';

		fscanf(fin,"%s",str);
      td = 0;
      num = 1;
      td = 0;
printf("\nstr = %s\n",str);

     
        
      c[str[0]] = num;

      digit[0] = num-- + '0';
      
      for(i=1;str[i];i++)
      {
                    
        
   
        if(c[str[i]] == -1)
        {
           c[str[i]] = num;
           digit[i] = num + '0';
           
           if(num == 0)
             num = 2;
           else
             num++;
        }
        else
           digit[i] = c[str[i]] + '0';
       
        
      
      }
     printf("\ndigit - %s (num = %d)\n",digit,num);
      
      sum = -1;
      temp = 0;
      unsigned long long loop,len,p;
      if(num <= 2) loop = 2;
        else loop = num;
      len = strlen(digit);
      j=loop;
      //for(j = loop; j>=2;j--)
      {
         n=len-1;
         temp = 0;
         printf("\ntest n = %d\n",n);
         p=0;
         while(n != -1)
         {
           temp += (digit[n] - '0')* pow(j, p++);
//printf("\ndigits = %d, pow = %d\n", (digit[n] - '0'),pow(j, p-1));
           n--;
         }
         
         if(sum == -1)
           sum = temp;
         else
         {
           if(sum > temp)
             sum = temp;
         }         
      }
      printf("\nAns = %d\n",sum);
      fprintf(fout,"Case #%d: %d\n",k, sum);
   }
      
}


