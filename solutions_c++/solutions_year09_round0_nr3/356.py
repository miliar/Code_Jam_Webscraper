#include <iostream>

using namespace std;

char s[30] = "welcome to code jam";
char a[600];

int d[600][30];

int main()
{
    int i, j, k, ca;
    freopen("C-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&ca);
    getchar();
    
    for(int cs=1;cs<=ca;cs++)
    {
        
        gets(a);
        //puts(a);
        int m = strlen(a);
        memset(d, 0, sizeof(d));
        for(i=0;i<=m;i++)d[i][0]=1;
        for(i=1;i<=m;i++)
            for(j=1;j<=19;j++)
            {
                d[i][j]=d[i-1][j];
                if(a[i-1]==s[j-1])
                    d[i][j] = (d[i][j] + d[i-1][j-1])%10000;
            }
        
        printf("Case #%d: ",cs);
        int n = 19;
        if(d[m][n]>=1000) printf("%d\n",d[m][n]);
        else if(d[m][n]>=100) printf("0%d\n",d[m][n]);
        else if(d[m][n]>=10) printf("00%d\n",d[m][n]);
        else printf("000%d\n",d[m][n]);
    }
    return 0;
}
    
                
    
