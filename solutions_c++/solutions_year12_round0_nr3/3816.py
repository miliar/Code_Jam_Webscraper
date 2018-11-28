#include <iostream>
#include <cstdio>
#include <cstring>
#include <map>
#include <set>

using namespace std;


__int64 a, b;

__int64 moveOneDigit(__int64 x, __int64 w) {
    return (x%10ll)*w+x/10ll;
}

int genPair(__int64 x) {
     __int64 key, tmp, w;
     int ans=0;
     tmp=x/10ll, w=1ll;
     while(tmp) tmp/=10ll, w*=10ll;
     tmp=x;
     do{
         tmp=moveOneDigit(tmp, w);
         if(tmp>x && tmp>=a && tmp<=b) ++ans;
     }while(tmp!=x);
     return ans;
}

int main() {
    
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    
    int t;
    __int64 res;
    scanf("%d", &t);
    
    for(int i=0; i<t; ++i) {
        res=0;
        scanf("%I64d %I64d", &a, &b);
        for(__int64 j=a; j<=b; ++j) res+=genPair(j);
        printf("Case #%d: ", i+1);
        printf("%I64d\n", res);
    }
}
