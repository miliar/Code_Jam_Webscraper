#include <cstdio>
#include <cstring>
#include <utility>
#include <algorithm>
using namespace std;

typedef pair<int,int> PII;

int gcd(int a, int b){
    if(b) return gcd(b,a%b); else return a;
}

bool gao(){
    long long n;
    int pd,pg;
    scanf("%I64d%d%d",&n,&pd,&pg);
    if(pd==0) return pg!=100;
    if(n*gcd(100,pd)<100) return false;
    if(pg==0) return pd==0;
    if(pg==100) return pd==100;
    return true;
}

int main(){
    int cs;
    scanf("%d",&cs);
    for(int t=1;t<=cs;t++)
        printf("Case #%d: %s\n",t,gao()?"Possible":"Broken");
}
