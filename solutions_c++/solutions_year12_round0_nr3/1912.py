#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
using namespace std;
int t,t1,n,s,p,ans,fl,fr,iii;
int a[10001];
int f[21];
int main(){
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    scanf("%d",&t);
    t1=t;
    getchar();
    while (t--){
        printf("Case #%d: ",t1-t);
        scanf("%d%d",&fl,&fr);
        ans=0;
        for (int i2=fl;i2<=fr;i2++){
            int i1=i2;
            int l=0;int mm=1;
            memset(a,0,sizeof 0);
            while (i1){
                  a[++l]=i1%10;
                  i1=i1/10;
                  mm=mm*10;
            }i1=i2;mm=mm/10;
            for (int i=1;i<=l/2;i++) swap(a[i],a[l-i+1]);     
            for (int i=1;i<l;i++) a[i+l]=a[i];
            int l1=l;
            l+=l-1;
            iii=0;
            memset(f,0,sizeof f);
            for (int i=l1+1;i<=l;i++){
                i1=i1%mm;
                i1=i1*10+a[i];
                int check=0;
                for (int j=l1+1;j<i;j++)
                    if (i1==f[j]) check=1;
                if (i1>i2 && i1<=fr && !check){
                          f[i]=i1;
                          ans++;
                }
            }
        }
        printf("%d\n",ans);
    }
}
