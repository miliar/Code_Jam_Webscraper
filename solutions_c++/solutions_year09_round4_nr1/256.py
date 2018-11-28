#include <iostream>
using namespace std;

int ncase,i,j,k,n,m,t,sum;
int a[100]={0};
char s[100]={0};
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&ncase);
    for (t=1; t<=ncase; t++)
    {
        scanf("%d",&n);
        gets(s);
        for (i=1; i<=n; i++)
        {
            gets(s);
            for (j=strlen(s)-1; j>=0; j--)
                if (s[j]=='1')
                    break;
            a[i] = j+1;
//            printf("\t%d\n",a[i]);
        }
        sum = 0;
        for (i=1; i<=n; i++)
        {
            for (j=i; j<=n; j++)
                if (a[j]<=i)
                    break;
            sum+=j-i;
            while (j>i)
            {
                a[j] = a[j-1];
                j--;
            }
        }
        printf("Case #%d: %d\n",t,sum);
    }
    return 0;
}
