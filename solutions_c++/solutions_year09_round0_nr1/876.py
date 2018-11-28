#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXL 15
#define MAXD 5002
#define MAXP 10002

char dictionary[MAXD+1][MAXL+1];

bool match(char *str, char *pat)
{
     bool t=false;
     if(!(*str)&&!(*pat)) return true;
     if(*pat=='(')
     {       
          pat++;
          while(*pat!=')')
          {
              if(*str==*pat) t = true;
              pat++;
          }
          if(!t) return false;
          return match(str+1,pat+1);        
     }
     else
     {
         if(*str==*pat) return match(str+1,pat+1);
         else return false;
     }
}

main()
{
      FILE *in = fopen("A-large.in","r");
      FILE *out = fopen("a.out.txt","w");
      int L,D,N,total;
      char pattern[MAXP+1];
      fscanf(in,"%d %d %d",&L,&D,&N);
      for(int i=0;i<D;i++)
              fscanf(in,"%s",dictionary[i]);
      for(int i=0;i<N;i++)
      {
              fscanf(in,"%s",pattern);
              total=0;
              for(int j=0;j<D;j++)
                      total += match(dictionary[j],pattern);
              fprintf(out,"Case #%d: %d\n",i+1,total);
              fprintf(stdout,"Case #%d: %d\n",i+1,total);
      }
      fclose(out);
      system("PAUSE");
      return 0;
}
