#include<iostream>
using namespace std;

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("output11.txt","w",stdout);
    char str[1000];
    char cj[]="welcome to code jam";
    int lcj=strlen(cj);
    int M[30][1000]={0};
    int t,i,j,k,l;
    scanf("%d\n",&t);
    
    for (k=1;k<=t;k++)
    {
        gets(str);
        l=strlen(str);
        for (j=0;j<l;j++)
        {
            if (cj[0]==str[j-1])
               M[1][j]=M[1][j-1]+1;
            else
                M[1][j]=M[1][j-1];
            //printf("%d ",M[1][j]);
        }
        //printf("\n");
        for (i=2;i<=lcj;i++)
        {
            M[i-1][0]=0;
            for (j=1;j<=l;j++)
                if (cj[i-1]==str[j-1])
                   M[i][j]=(M[i-1][j]+M[i][j-1])%10000;
                else
                    M[i][j]= M[i][j-1];
        }
        /*for (i=2;i<=lcj;i++)
        {
            for (j=0;j<=l;j++)
                printf("%d ",M[i][j]);
            printf("\n");
        }*/
        printf("Case #%d: %04d\n",k,M[lcj][l]);
    }
}
