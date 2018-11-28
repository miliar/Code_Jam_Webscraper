#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 10000

char s[MAX+1];
char p[20];
int T[MAX+1][20];
int tb;

int pos(int a, int b)
{
    if(b==tb) return 1;
    if(s[a]==0) return 0;
    if(T[a][b]!=-1) return T[a][b];
    return T[a][b] = ((pos(a+1,b) % 10000) + (((s[a]==p[b])?pos(a+1,b+1):0) % 10000)) % 10000;
}

main()
{
      strcpy(p,"welcome to code jam");
      tb = strlen(p);
      int N,r=0,nc=1;
      FILE *in = fopen("C-large.in","r");
      FILE *out = fopen("c.out.txt","w");
      fgets(s,MAX-1,in);
      N = atoi(s);
      while(N--)
      {
                fgets(s,MAX-1,in);
                memset(T,-1,sizeof(T));
                r = pos(0,0)%10000;
                fprintf(out,"Case #%d: %04d\n",nc,r);
                fprintf(stdout,"Case #%d: %04d\n",nc,r);
                nc++;
      }
      fclose(out);
      system("PAUSE");
}
