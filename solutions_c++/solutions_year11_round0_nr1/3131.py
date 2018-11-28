#include <cstdio>
#include <cstdlib>
#define MAX 110
typedef struct
{
    char col;
    int bot;//el boton
}tiposec;
tiposec sec[MAX];
int t,n,blue,ora,pb,po,total;
void resuelve()
{
    for (int i=1; i<=n; i++)//revisar cada una de los movimientos
    {
        if (sec[i].col=='O')//Es naranja
        {
            ora+=(abs(sec[i].bot-po));
            po=sec[i].bot;
            if (ora>total)
                total=ora;
            else
                ora=total;
            ora++;//apretar el boton
            total++;
        }
        else
        {
            blue+=(abs(sec[i].bot-pb));
            pb=sec[i].bot;
            if (blue>total)
                total=blue;
            else
                blue=total;
            total++;
            blue++;
        }
    }
}
int main()
{
    scanf("%d",&t);
    for (int i=1; i<=t; i++)
    {
        blue=0;
        pb=po=1;
        ora=0;
        total=0;
        scanf("%d ",&n);
        for (int j=1; j<=n; j++)
            scanf("%c %d ",&sec[j].col,&sec[j].bot);
        resuelve();
        printf("Case #%d: %d\n",i,total);
    }
}
