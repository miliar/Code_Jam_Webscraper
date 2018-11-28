#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<iostream>
using namespace std;

int gcd(int a,int b){
    if(b==0) return a;
    else return gcd(b,a%b);
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    cin>>T;
    long long N;
    int PD,PG;
    int tt=1;
    while(T--){
        cin>>N>>PD>>PG;
        printf("Case #%d: ",tt++);

        if(PG==100){
            if(PD<100) {
                 printf("Broken\n");
            }else{
                printf("Possible\n");
            }
            continue;
        }
        if(PG==0){
            if(PD>0){
                printf("Broken\n");
            }else{
                printf("Possible\n");
            }
            continue;
        }
        int g = gcd(100,PD);
        int t = 100/g;
        if(t<=N){
            printf("Possible\n");
        }else{
            printf("Broken\n");
        }
    }
    return 0;
}
