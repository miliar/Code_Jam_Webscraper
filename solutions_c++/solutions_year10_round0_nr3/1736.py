#include <iostream>
#include <cstdlib>
#include <cstdio>

using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int r,k,n,t,jj;
    int q[1000],p[1000],kol[1000];
    long long col;
    scanf("%d",&t);
    for (int i=0;i<t;i++) {
     scanf("%d%d%d",&r,&k,&n);
     for (int j=0;j<n;j++) scanf("%d",&q[j]);
     for (int j=0;j<n;j++) {
      kol[j]=q[j];jj=(j+1)%n;
      while (kol[j]<k&&jj!=j) {kol[j]+=q[jj];jj=(jj+1)%n;}
      if (kol[j]>k) {kol[j]-=q[(jj+n-1)%n];jj=(jj+n-1)%n;}
      p[j]=jj;
     }
     col=0;jj=0;
     for (int j=0;j<r;j++) {col+=kol[jj];jj=p[jj];}
     printf("Case #%d: %lld\n",i+1,col);
    }

    return 0;
}
