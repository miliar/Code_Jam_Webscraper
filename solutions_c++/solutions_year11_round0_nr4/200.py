#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cstring>
#include<string>
#include<algorithm>
using namespace std;
int a[2000];
int b[2000];
int n;
int main(){
    freopen("D-large.in","r",stdin);
    freopen("D-large.out","w",stdout);
    int cas;
    scanf("%d",&cas);
    for(int ca=1;ca<=cas;ca++){
        scanf("%d",&n);
        for(int i=0;i<n;i++){
            scanf("%d",&a[i]);
            b[i]=a[i];
        }
        sort(a,a+n);
        double ans=0;
        for(int i=0;i<n;i++){
            if(a[i]!=b[i]) ans+=1.0;
        }
        printf("Case #%d: %lf\n",ca,ans);
    }
    return 0;
}
