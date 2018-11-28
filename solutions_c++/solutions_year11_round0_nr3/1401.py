#include<cstdio>
#include<conio.h>
using namespace std;
int main()
{
    int n,i,j,c[1000],tot=0,x,min,f;
    freopen("C-large.in","r",stdin);
    freopen("FFF.in","w",stdout);
    scanf("%d\n",&n);
    for(i=0;i<n;i++)
    {
                    scanf("%d\n",&f);
                    for(j=0,tot=0,x=0,min=10000000;j<f;j++)
                    {
                        scanf("%d",&c[j]);
                        tot+=c[j];
                        x^=c[j];
                        if(min>c[j])
                        min=c[j];
                        }
                   printf("Case #%d: ", (i+1));            
                   if(x)
                   printf("NO\n");
                   else
                   printf("%d\n",tot-min);
                   }
                   }
