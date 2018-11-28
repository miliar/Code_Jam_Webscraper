#include<cstdio>
#include<algorithm>
#include<iostream>

using namespace std;

int T,n,d,g,i;
int I=0;

int main(){
    scanf("%d",&T);
    while (T--){
        cin >>  n  >> d >> g;
        if (n>100) n=100;
        bool bt=false;
        for (i=1;i<=n;++i)
            if (i*d%100==0){
                bt=true;
                break;
            }
        if (g==0 && d!=0 || g==100 && d!=100)
            bt=false;
        printf("Case #%d: ",++I);
        if (bt) puts("Possible");
        else puts("Broken");
    }
}
