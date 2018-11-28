#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

int Tc;

int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin >> Tc;
    for (int k=1;k<=Tc;k++){
        long long n,Pg,Pd;
        cin >> n >> Pd >> Pg;
/*
        bool check=false;
        for (int i=1;i<=n;i++){
            if (Pd*i%100==0){
                long long Wd=Pd*i/100;
                if (Wd!=0 && Pg==0) continue;
                if (Pg==100 && Pd!=100) continue;
                check=true;
                break;
            }
        }
*/
        bool check=true;
        if (Pg==0 && Pd!=0) check=false;
        if (Pg==100 && Pd!=100) check=false;
        if (Pd!=0){
            int cnt2=0,cnt5=0;
            int tmp=Pd;
            while (tmp%2==0){
                tmp/=2;
                cnt2++;
            }
            while (tmp%5==0){
                tmp/=5;
                cnt5++;
            }
            long long ret=1;
            for (int i=cnt2+1;i<=2;i++) ret*=2;
            for (int i=cnt5+1;i<=2;i++) ret*=5;
            if (ret>n) check=false;
        }
        printf("Case #%d: ",k);
        if (check) printf("Possible\n");
             else  printf("Broken\n");
    }
}
