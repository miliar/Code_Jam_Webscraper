#include<stdio.h>
#include<string.h>

int min(int a,int b)
{
    if(a<b)
     return a;
    else
     return b;
    }

int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("A-small-attempt1.out","w",stdout);
    char  in[102][102],a[102],ch;
    int n,m,l,ma,count,i,j,k,start,p,t,s=0,cas;

    scanf("%d",&cas);

    while(cas--)
    {
    scanf("%d%d\n",&n,&m);



    count=0;

    for(i=0;i<n;i++)
     {
     gets(in[i]);
     l=strlen(in[i]);
     in[i][l]='/';
     in[i][l+1]=0;
     }

    for(k=0;k<m;k++)
    {
        gets(a);
        l=strlen(a);
        a[l]='/';
        a[++l]=0;

        ma=1;


         for(j=0;j<n;j++)
          {

              start=1;
              p=min(l,strlen(in[j]));
              for(i=1;i<=p;i++)
               if(a[i]!=in[j][i])
                {
                    start=i;
                    goto level;

                }
            start=p+1;

         level:
          if(start>ma)
              ma=start;
       }
        for(i=ma;i<=l;i++)
         if(a[i]=='/')
          count++;

      strcpy(in[n++],a);

    }
printf("Case #%d: ",++s);
    printf("%d\n",count);
    }
    return 0;
}
