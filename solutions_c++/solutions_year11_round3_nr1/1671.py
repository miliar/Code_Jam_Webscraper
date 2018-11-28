#include<stdio.h>
#include<string.h>
#include<math.h>
#include<ctype.h>

int main()
{

freopen("A-large.in","r",stdin);
freopen("A-large.out","w",stdout);
int t,k;
int i,j,red,r,c;
char a[100][100],ch;
scanf("%d",&t);



for(k=1;k<=t;k++)
{


    scanf("%d%d\n",&r,&c);

    red=0;
    for(i=0;i<r;i++)
     {for(j=0;j<c;j++)
     {
         scanf("%c",&a[i][j]);
         if(a[i][j]=='#') red++;
     }

         a[i][j]=0;

         scanf("%c",&ch);
     }

     for(i=0;i<r-1;i++)
       for(j=0;j<c-1;j++)
         if(a[i][j]=='#' && a[i+1][j]=='#' && a[i][j+1]=='#' && a[i+1][j+1]=='#')
        {
            a[i][j]='/' ;
            a[i+1][j]='\\';
            a[i][j+1]='\\';
            a[i+1][j+1]='/';
            red=red-4;
        }

    printf("Case #%d:\n",k);
    if(red==0)
     {
         for(i=0;i<r;i++)
          {for(j=0;j<c;j++)
           printf("%c",a[i][j]);

           printf("\n");
        }
     }
    else
       printf("Impossible\n");


}

return 0;
}
