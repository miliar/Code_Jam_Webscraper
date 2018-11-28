/*
TASK: B-triangle
LANG: C++
*/

#include<stdio.h>
#include<stdlib.h>

int n,m,a,ss;
FILE *fin,*fout;

void Doit()
{
    int nn,mm,xx,yy;
    for(nn=0;nn<=n;nn++) for(mm=0;mm<=m;mm++)
    for(xx=0;xx<=n;xx++) for(yy=0;yy<=m;yy++)
    {
        if(xx*mm+nn*yy==nn*mm+a || xx*mm+nn*yy==nn*mm-a)
        {
            fprintf(fout,"Case #%d: %d %d %d %d %d %d\n",ss,xx,yy,nn,0,0,mm);
            return;
        }
    }
    fprintf(fout,"Case #%d: IMPOSSIBLE\n",ss,xx,yy,nn,0,0,mm);
}

int main()
{
    int sss;
    int i;
    fin = fopen("B-small-attempt0.in","r");
    fout = fopen("B-small.out","w");
    fscanf(fin,"%d",&sss);
    for(ss=1;ss<=sss;ss++)
    {
        printf("--%d--\n",ss);
        fscanf(fin,"%d %d %d",&n,&m,&a);
        Doit();
        
    }
    system("PAUSE");
    return 0;
}
