#include<iostream>
using namespace std;
long n,m,tst=1,tt;
long q[110],l,i,j;
long f[1000];
bool b[1000];
char s[110];
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    for (scanf("%ld",&tt);tst<=tt;tst++)
    {
        memset(f,-1,sizeof(f));
        memset(b,0,sizeof(b));
        for (scanf("%ld",&n);n>0;n--)
        {
            scanf("%s",s);
            f[(s[0]-65)*26+(s[1]-65)]=s[2];
            f[(s[1]-65)*26+(s[0]-65)]=s[2];
        }
        for (scanf("%ld",&n);n>0;n--)
        {
            scanf("%s",s);
            b[(s[0]-65)*26+(s[1]-65)]=1;
            b[(s[1]-65)*26+(s[0]-65)]=1;
        }
        scanf("%ld",&n);
        scanf("%s",s);
        l=0;
        for (i=0;i<n;i++)
        {
            q[l++]=s[i];
            if (l>1 && f[(q[l-2]-65)*26+(q[l-1]-65)]>=0)
            {
               q[l-2]=f[(q[l-2]-65)*26+(q[l-1]-65)];
               l--;
            }
            if (l>1)
            {
               for (j=0;j<l-1;j++) if (b[(q[j]-65)*26+(q[l-1]-65)])
               {
                   l=0;
                   break;
               }
            }
        }
        printf("Case #%ld: [",tst);
        if (l>0) printf("%c",q[0]);
        for (i=1;i<l;i++) printf(", %c",q[i]);
        printf("]\n");
    }
    return 0;
}
