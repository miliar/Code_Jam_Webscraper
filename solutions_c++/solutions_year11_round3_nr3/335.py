#include<iostream>
using namespace std;
int T,n,L,H;
int a[10000];
int main()
{
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
    int i,j,k;
    scanf("%d",&T);
    for(i=1;i<=T;i++){
                      scanf("%d%d%d",&n,&L,&H);
                      for(j=1;j<=n;j++)scanf("%d",&a[j]);
                      for(j=L;j<=H;j++){
                      for(k=1;k<=n;k++){
                                        //printf("%d %d\n",j,a[k]);
                                        if(j%a[k]==0||a[k]%j==0)continue;
                                        else break;
                                        }
                      if(k>n)break;
                      }
                      if(j<=H)
                      printf("Case #%d: %d\n",i,j);
                      else printf("Case #%d: NO\n",i);
                      }
    //while(1);
}
