#include <cstdio>

int probCount;
long long a, b, p0;

int s[1000010];
int r[1000010];

int prime[100000];
int np = 1;

int sc(int a) {
    if(s[a] == a)
        return a;
    s[a] = sc(s[a]);
    return s[a];
}

void su(int a, int b) {
    a = sc(a);
    b = sc(b);
    if(a == b)
        return;
    if(r[b] > r[a]) {
        s[a] = b;
    } else {
        s[b] = a;
        if(r[a] == r[b]) {
            r[a]++;
        }
    }
}

int main() {
    scanf("%d", &probCount);
    prime[0] = 2;
    for(int i=3; i<1000010; i++) {
        bool newp = true;
        for(int j=0; prime[j]*prime[j] <= i; j++) {
            if(i%prime[j] == 0) {
                newp = false;
                break;
            }
        }
        if(newp) {
            prime[np++] = i;
        }
    }
    for(int probIndex=1; probIndex<=probCount; probIndex++) {
        scanf("%I64d%I64d%I64d", &a, &b, &p0);
        int n = b-a+1;
        for(int i=0; i<n; i++) {
            s[i] = i;
            r[i] = 0;
        }
        int i;
        for(i=0; i<np; i++) {
            if(prime[i]>=p0)
                break;
        }
        for(; i<np; i++) {
            if(prime[i] > n)
                break;
            int p = prime[i];
            for(int j = ((a-1) / p + 1) * p - a; j+p<n; j+=p) {
                su(j, j+p);
            }

        }
        int ans=0;
        for(int i=0; i<n; i++) {
            if(s[i] == i)
                ans++;
        }
        printf("Case #%d: %d\n", probIndex, ans);
    }
    return 0;
}
