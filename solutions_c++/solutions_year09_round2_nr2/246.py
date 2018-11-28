#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <algorithm>
using namespace std;



main()
{
      int T,nc=1, res;
      char s[1000], temp[1000], temp2[1000];
      
      //FILE *in = fopen("b.txt","r");
      //FILE *in = stdin;
      //FILE *in = fopen("B-small-attempt1.in","r");
      //FILE *out = fopen("B-small.out","w");
      
      FILE *in = fopen("B-large.in","r");
      FILE *out = fopen("B-large.out","w");
      
      fscanf(in,"%d",&T);
      while(T--)
      {
             fscanf(in,"%s",s); 
             if(!next_permutation(s,s+strlen(s)))
             {                              
                  strcpy(temp,s+1);
                  s[1]='0';
                  s[2]=0;
                  strcat(s,temp);
                  int ceros=0;
                  while(s[ceros]=='0') ceros++;
                  strcpy(temp,s);
                  temp[ceros]=0;
                  strcpy(temp2,s+ceros+1);
                  //printf("-%s-%s-%s-",s,temp,temp2);
                  strcat(temp,temp2);
                  s[0] = s[ceros];
                  strcpy(s+1,temp);
             }
             fprintf(out,"Case #%d: %s\n",nc, s);
             fprintf(stdout,"Case #%d: %s\n",nc++,s);
             
             //Algorithm-begins
             //Algorithm-ends             
             
             fprintf(out,"\n");
      }
      system("PAUSE");
      fclose(out);
      return 0;
}
