#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;

int a[10001];

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int dol,i,ability,add,j,somoy,test,dd,group,m,n,c,kase=1;
   scanf("%d",&test);
   while(test--)
   {
       scanf("%d %d %d",&somoy,&ability,&dol);
       for(i=0;i<dol;i++)
        scanf("%d",&a[i]);

        group=dol;
        dd=m=n=0;

        for(;m<somoy;m++)
        {
            c=1;
            for(j=n,add=0;j<group;j++,c++)
              {
                 if(add+a[j]<=ability)
                 {
                    dd+=a[j];
                    add+=a[j];
                    a[group++]=a[j];
                 }
                 else
                 {
                   n=j;
                   break;
                 }
                  if(c==dol) break;
               }
        }
        printf("Case #%d: %d\n",kase++,dd);

   }

    return 0;
}


