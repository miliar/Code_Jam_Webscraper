#include <iostream>
#define maxl 6000
#define ll 20
char a[maxl][ll],x;
int o[ll][26],b,c,d,e,n,m,l;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d %d %d\n",&l,&d,&n);
    for (b=1;b<=d;b++)
    {
        for (c=1;c<=l;c++)
          scanf("%c",&a[b][c]);
        scanf("\n");
    }
    for (b=1;b<=n;b++)
    {
        c=1;
        memset(o,0,sizeof(int)*ll*26);
        while (c<=l)
        {
              scanf("%c",&x);
              if (x!='(') o[c][x-'a']=1;
                else
              while (1)
              {
                    scanf("%c",&x);
                    if (x==')') break;
                    o[c][x-'a']=1;
              }
              c++;
        }
        scanf("\n");
        m=0;
        for (c=1;c<=d;c++)
        {
          for (e=1;e<=l;e++)
          if (o[e][a[c][e]-'a']==0) break;
          if (e==l+1) m++;
        }
        printf("Case #%d: %d\n",b,m);
    }
}
