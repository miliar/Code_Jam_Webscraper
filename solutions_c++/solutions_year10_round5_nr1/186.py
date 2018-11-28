#include <cstdio>
#include <cstring>
#include <cstdlib>

int T,N,D,P,p[1000000],ten[7]={1,10,100,1000,10000,100000,1000000};
long long n[10];

void Prime() {
    int i,x;

    p[P++] = 2;
    for(x=3; x<1000000; x++) {
        for(i=0; p[i]*p[i]<=x&&i<P; i++)
            if(x % p[i] == 0)
                break;
        if(p[i] * p[i] > x || i >= P)
            p[P++] = x;
    }
}
long long Exgcd(long long a, long long b, long long &x, long long &y) {
    long long d;
    if(b == 0) {
        x = 1;
        y = 0;
        return a;
    }
    d = Exgcd(b, a%b, x, y);
    int t=x;
    x = y;
    y = t - a/b*y;
    return d;
}

long long Solve(long long a, long long b, long long c) {
    long long x,y,gcd;

    gcd = Exgcd(a, b, x, y);
    return c/gcd*x;
}

int main() {
    int i,j,cas=1;
    long long A,B,a,b,c;

    Prime();
    scanf("%d", &T);
    while(T--) {
        scanf("%d%d", &D, &N);
        for(i=0; i<N; i++)
            scanf("%lld", &n[i]);
        printf("Case #%d: ", cas++);
        if(N == 1)
            printf("I don't know.\n");
        else if(N == 2) {
            if(n[0] == n[1])
                printf("%lld\n", n[0]);
            else
                printf("I don't know.\n");
        }
        else {
            if(n[0] == n[1])
                printf("%lld\n", n[0]);
            else {
                long long ans=-1;
                c = n[2] - n[1];
                a = n[1] - n[0];
                for(i=0; i<P&&p[i]<ten[D]; i++) {
                    b = p[i];
                    for(j=0; j<N; j++)
                        if(n[j] >= b)
                            break;
                    if(j < N)
                        continue;
                    A = Solve(a,b,c);
                    A = (A%b+b)%b;
                    B = ((n[1]-n[0]*A)%b+b)%b;
                    //printf("%lld %lld\n", A, B);
                    for(j=0; j<N-1; j++)
                        if(n[j+1] != (n[j]*A+B)%b)
                            break;
                    if(j >= N-1) {
                        long long tmp=((n[N-1]*A+B))%b;
                        if(ans != -1 && tmp != ans) {
                            ans = -1;
                            break;
                        }
                        else
                            ans = tmp;
                    }
                }
                if(ans == -1)
                    printf("I don't know.\n");
                else
                    printf("%lld\n", ans);
            }
        }
    }
    return 0;
}
