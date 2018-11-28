#include<cstdio>
#include<iostream>

#define lint long long int

using namespace std;

lint N;
int pd,pg;

bool rozwiaz(){
    if(pg==100 && pd!=100) return false;
    if(pg==0 && pd!=0) return false;
    if(N>=100) return true;
    for(int i=1;i<=N;i++){
        int k = i*pd/100;
        if(k * 100 == i * pd) return true;
    }
    return false;
}

int main(){
    int Z;
    scanf("%d",&Z);
    for(int z=1;z<=Z;z++){
        printf("Case #%d: ",z);
        scanf("%lld%d%d",&N,&pd,&pg);
        if(rozwiaz())
            printf("Possible\n");
        else printf("Broken\n");
    }

}
