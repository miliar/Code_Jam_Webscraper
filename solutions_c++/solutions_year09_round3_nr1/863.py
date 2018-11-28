#include <stdio.h>
#include <string.h>

bool f[255];
int d[255];

long long solve(char s[]) {
    memset(f,0,sizeof(f));
    int n = 0;
    int cnt = 0;
    for(int i=0;s[i];i++) {
        n++;
        f[s[i]] = true;
    }
    for(int i=0;i<255;i++) {
        if(f[i]) cnt++;
    }
    if(cnt==1) cnt++;

    memset(d,-1,sizeof(d));
    d[s[0]] = 1;
    long long res = 1ll;
    int v = 0;
    for(int i=1;i<n;i++) {
        if(d[s[i]]<0) {
            if(v==1) ++v;
            d[s[i]] = v;
            v++;
        }
        res = res * cnt;
        res = res + d[s[i]];
    }

    return res;
}

int main() {
    int cases;
    scanf("%d",&cases);
    for(int cs=1;cs<=cases;cs++) {
        char s[100];
        scanf("%s",s);
        printf("Case #%d: %lld\n", cs, solve(s));
    }
    return 0;
}

