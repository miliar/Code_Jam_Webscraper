#include<iostream>
using namespace std;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int tt,cases,i,n,s1,s2,m,x;
    for (scanf("%d",&cases),tt=0;tt<cases;tt++)
    {
         s1=0;
         s2=0;
         m=0;
         for (scanf("%d",&n);n;n--)
         {
             scanf("%d",&x);
             s1^=x;
             s2+=x;
             if (m==0) m=x;
             else m=min(m,x);
         }
         printf("Case #%d: ",tt+1);
         if (s1) puts("NO");
         else printf("%d\n",s2-m);
    }
    return 0;
}
