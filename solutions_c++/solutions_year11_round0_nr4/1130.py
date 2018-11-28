#include<iostream>
using namespace std;
int T,n;
int a[100],b[100];
int main()
{
    freopen("d.in","r",stdin);
    freopen("d.out","w",stdout);
    int i,j;
    scanf("%d",&T);
    for(i=1;i<=T;i++){
                      memset(a,0,sizeof(a));
                      int x,y,s=0,w=0;
                      scanf("%d",&n);
                      for(j=1;j<=n;j++){scanf("%d",&a[j]);if(a[j]!=j)w++;}
                      printf("Case #%d: %d.000000\n",i,w);
                      }
    //while(1);
}
