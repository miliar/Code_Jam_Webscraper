#include<cstdio>
#include<cstring>
#include<algorithm>
#include<utility>
#include<vector>
#include<queue>
#include<map>
using namespace std;

typedef long long foo;

foo gcd(foo a,foo b){
    return b?gcd(b,a%b):a;
}

class Frac {
public:
    foo num, den;
    Frac(foo n=0,foo d=1):num(n),den(d){spf();}
    void spf(){
        if(foo t=gcd(num,den)){
            int k=den/t<0?-1:1;
            num/=k*t;
            den/=k*t;
        }
    }
    const Frac operator+(const Frac &rhs) const {
        return Frac(num*rhs.den+den*rhs.num,den*rhs.den);
    }
    const Frac operator-(const Frac &rhs) const {
        return Frac(num*rhs.den-den*rhs.num,den*rhs.den);
    }
    const Frac operator*(const Frac &rhs) const {
        return Frac(num*rhs.num,den*rhs.den);
    }
    const Frac operator/(const Frac &rhs) const {
        return Frac(num*rhs.den,den*rhs.num);
    }
    const bool operator==(const Frac &rhs) const {
        return num*rhs.den==den*rhs.num;
    }
    const bool operator<(const Frac &rhs) const {
        return num*rhs.den<den*rhs.num;
    }
};

void gao(){
    int n, pd, pg;
    scanf("%d%d%d",&n,&pd,&pg);
    Frac fd(pd,100);
    if(fd.den<=n){
        if(pg>=fd.num && pg<=(pd==100?100:99)){
            puts("Possible");
            return ;
        }
    }
    puts("Broken");
}
int main(){
    freopen("A-small-attempt2.in","r",stdin);
    freopen("A-small.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int tt=1;tt<=T;tt++){
        printf("Case #%d: ",tt);
        gao();
    }
}
