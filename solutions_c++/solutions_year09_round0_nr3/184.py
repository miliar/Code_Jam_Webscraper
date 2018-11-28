/*
TASK: codejam
LANG: C++
*/

#include<stdio.h>
#include<stdlib.h>
#include<string.h>

FILE *fin,*fout;
int n;
char str[510];
char u[20] = "welcome to code jam";
int ans[2][20];

int main()
{
    fin = fopen("C-large.in","r");
    fout = fopen("codejam.out","w");
    
    fscanf(fin,"%d\n",&n);
    for(int nn=1;nn<=n;nn++)
    {
        int i,j;
        for(i=0;i<510;i++) str[i]=0;
        for(i=0;i<20;i++) {ans[0][i] = 0; ans[1][i] = 0;}
        fgets(str,510,fin);
        //printf("%s",str);
        int lenz;
        lenz = strlen(str);
        for(i=0;i<lenz;i++)
        {
            for(j=0;j<=18;j++)
            {
                ans[i&1][j] = ans[!(i&1)][j];
                if(str[i]==u[j]) 
                {
                    if(j>0) ans[i&1][j] += ans[!(i&1)][j-1];
                    else ans[i&1][j] += 1;
                    ans[i&1][j] = ans[i&1][j] % 10000;
                }
            }
        }
        fprintf(fout,"Case #%d: %04d\n",nn,ans[!(i&1)][18]);
    }
    
    system("PAUSE");
    return 0;
}
