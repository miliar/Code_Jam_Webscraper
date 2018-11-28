#include <iostream>
using namespace std;
long long gcd(long long a,long long b){
    if(a) return gcd(b%a,a);
    return b;
}
int main(){
    int T,pd,pg;
    long long n;
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    cin >> T;
    for(int I = 1;I <= T;++I){
        printf("Case #%d: ",I);
        cin >> n >> pd >> pg;
        if(pd > 0 && pg == 0){
            printf("Broken\n");
            continue;
        }
        if(pd < 100 && pg == 100){
            printf("Broken\n");
            continue;
        }
        long long gg = gcd(pd,100);
        if(gg == 0){
            printf("Possible1\n");
        }
        else if(100 / gg <= n)
            printf("Possible\n");
        else printf("Broken\n");
    }
}
