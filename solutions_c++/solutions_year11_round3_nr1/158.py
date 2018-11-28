#include<stdio.h>
using namespace std;
char ch,tabel[55][55];
int a,b,c,d,e,f;
int main()
{
    //freopen("square.in","r",stdin);
    //freopen("square.out","w",stdout);
    scanf("%d",&a);
    for(b=1;b<=a;b++)
    {
        scanf("%d %d",&c,&d);
        for (e=1;e<=c;e++)
        {
            scanf("%c",&ch);
            for (f=1;f<=d;f++)
            {
                scanf("%c",&tabel[e][f]);
            }
        }
        for (e=1;e<=c;e++)
        {
            for (f=1;f<=d;f++)
            {
                if (tabel[e][f]=='#')
                {
                    if (tabel[e][f+1]=='#' && tabel[e+1][f]=='#' && tabel[e+1][f+1]=='#')
                    {
                       tabel[e][f]='/';
                       tabel[e][f+1]=(char)92;
                       tabel[e+1][f]=(char)92;
                       tabel[e+1][f+1]='/';
                       //printf("%c",tabel[e][f+1]);                       
                    }                     
                }    
            }    
        }
        bool bole=0;
        for (e=1;e<=c;e++)
        {
            for (f=1;f<=d;f++)
            {
                if (tabel[e][f]=='#')
                   bole=1;
               // printf("%c",tabel[e][f]);
            }
            //printf("\n");
        }
        printf("Case #%d:\n",b);
        if (bole)
           printf("Impossible\n");
        else
        {
            for (e=1;e<=c;e++)
            {
                for (f=1;f<=d;f++)
                    printf("%c",tabel[e][f]);
                printf("\n");    
            }    
        }          
    }
}
