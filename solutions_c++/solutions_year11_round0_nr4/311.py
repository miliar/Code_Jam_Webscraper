#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>
#include <queue>
using namespace std;
//double p[1005];
//double d(int n,int m){//n=>m
//    if(m==1) return 0;
//    double tmp=1;
//    for(int i=0;i<m;i++){
//        tmp*=n-i;
//        tmp/=m-i;
//    }
//
//    double h=0;
//    double k=-1;
//    for(int i=2;i<=m;i++){
//        k*=-i;
//        h+=1.0/k;
//    }
//    tmp*=h;
//    for(int i=m+1;i<=n;i++)
//        tmp/=i;
//    return tmp;
//}
int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int ca;
//    p[0]=p[1]=0;
//    for(int i=2;i<1001;i++){
//        p[i]=1;
//        for(int j=2;j<i;j++)
//            p[i]+=p[j]*d(i,j);
//        p[i]/=1.0-d(i,i);
//        if(i<10) printf("%lf\n",p[i]);
//    }

    scanf("%d",&ca);
    for(int pp=1; pp<=ca; pp++)
    {
        printf("Case #%d: ",pp);
        int n,ans=0;
        scanf("%d",&n);
        for(int i=0;i<n;i++){
            int j;
            scanf("%d",&j);
            if(j!=i+1) ans++;
        }
        printf("%d.000000\n",ans);
    }
    return 0;
}
