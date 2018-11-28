#include<iostream>
#include<stdio.h>
#include<math.h>
using namespace std;

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
     freopen("out.txt","w",stdout);
    int t,r,k,n,i,j,pos,ans,tmp,a[1010],tmp1;
    scanf("%d",&t);
    for(i=1;i<=t;i++){
        scanf("%d%d%d",&r,&k,&n);
        for(j=0;j<n;j++) scanf("%d",&a[j]);
        ans=pos=0;
        for(j=0;j<r;j++) {
            tmp=a[pos]; tmp1=pos; pos=(pos+1)%n;
            while((tmp+a[pos])<=k&&pos!=tmp1) {
                tmp+=a[pos];
                pos=(pos+1)%n;
            }
            ans+=tmp;
        }
        printf("Case #%d: %d\n",i,ans);
    }
   // system("pause");
    return 0;
}
