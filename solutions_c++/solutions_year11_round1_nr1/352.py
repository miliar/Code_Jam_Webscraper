#include <cstdio>
#include <algorithm>
using namespace std;

int CN = 1;
bool scase() {
    int pg,pd;
    long long n;
    scanf("%lld%d%d",&n,&pd,&pg);
    if (pg==100 && pd!=100) return false;
    if (pg==0 && pd!=0) return false;
    if (n>=100) return true;
    for(int i=1;i<=n;i++) if ((pd*i)%100==0) return true;
    return false;
}

int main() {
    int j; scanf("%d",&j);
    while(j--) printf("Case #%d: %s\n",CN++,scase()?"Possible":"Broken");
    return 0;
}

