#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int p[25][505];

int main()
{   int n,k,i,j,ii,jj;
    char c[505],a[505],b[25]=" welcome to code jam";
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    scanf("%d\n",&n);
    for(k=0;k<n;k++)
    {   gets(&a[1]);
        a[0]=' ';
        //printf("%s",a);
        jj=strlen(a)-1;
        ii=19;
        for(j=0;j<=jj;j++)
            p[0][j]=1;
        for(i=1;i<=ii;i++)
            for(j=1;j<=jj;j++)
            {   p[i][j]=p[i][j-1];
                if(a[j]==b[i])
                    p[i][j]=(p[i][j]+p[i-1][j-1])%10000;
            }
        printf("Case #%d: ",k+1);
        printf("%d",p[ii][jj]/1000);
        p[ii][jj]%=1000;
        printf("%d",p[ii][jj]/100);
        p[ii][jj]%=100;
        printf("%d",p[ii][jj]/10);
        p[ii][jj]%=10;
        printf("%d\n",p[ii][jj]);
    }
    //system("pause");
    return 0;
}
