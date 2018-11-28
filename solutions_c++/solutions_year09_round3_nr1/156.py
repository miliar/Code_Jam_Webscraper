#include <algorithm>
#include <vector>
#include <cstring>
#include <cstdlib>
#include <sstream>
#include <cstdio>

using namespace std;

int numUnique(char *s) {
    char foo[300];
    memset(foo,0,sizeof(foo));
    while(*s) {
        foo[*(s++)]=1;
    }
    return count(foo,foo+300,1);
}

long long go() {
    char buf[100];
    scanf("%s",buf);
    if(strlen(buf)==1) return 1LL;
    int ndiff=0;
    char foo[300];
    int nn=0;
    memset(foo,0xFF,sizeof(foo));
    for(int i=0;buf[i];i++) {
        if(foo[buf[i]]==-1) {
            foo[buf[i]]=nn++;
        }
    }
    for(int i=0;i<300;i++)if(foo[i]==0)foo[i]=1;else if(foo[i]==1)foo[i]=0;
    int base = max(numUnique(buf), 2);
    long long ans=0;
    for(int i=0;buf[i];i++) {
        ans=(ans*base+foo[buf[i]]);
    }
    return ans;
}

int main() {
    int n;
    scanf("%d",&n);
    for(int i=1;i<=n;i++) {
        printf("Case #%d: %lld\n",i,go());
    }
    return 0;
}
