#include <iostream>
using namespace std;
bool isprime[1000001];
long long primes[1000000];
int pc = 0;
long long nums[10];
// gcd: ax+by=gcd(a,b)
long long inverse(long long a, long long b) {
    long long bb = b;
    long long x=1, y=0;
    long long x1=0, y1=1;
    while (b!=0) {
        long long t = b, tx = x1, ty = y1;
        long long div = a/b;
        x1 = ((x-div*x1)%bb+bb)%bb;
        y1 = ((y-div*y1)%bb+bb)%bb;
        x = tx;
        y = ty;
        b = a%b;
        a = t;
    }
    return x;
}
int main() {
    memset(isprime,1,sizeof(isprime));
    isprime[0]=isprime[1]=false;
    for (int i=2; i<=1000; i++) {
        if (isprime[i]) {
            for (int j=i*i; j<1000001; j+=i) isprime[j]=false;
            primes[pc++]=i;
        }
    }
    for (int i=1001; i<1000001; i+=2) if (isprime[i]) primes[pc++]=i;
    int T; scanf("%d",&T); for (int t=1; t<=T; t++) {
        printf("Case #%d: ",t);
        int D,K; scanf("%d %d",&D,&K);
        int limit = 1;
        for (int i=0; i<D; i++) limit*=10;
        bool allsame = true;
        int biggest = 0;
        for (int i=0; i<K; i++) {
            scanf("%I64d",&nums[i]);
            biggest>?=nums[i];
            if (nums[i]!=nums[0]) allsame=false;
        }
        if (allsame && K>1) {
            printf("%d\n",nums[0]);
            continue;
        }
        if (K<=2) {
            printf("I don't know.\n");
            continue;
        }
        long long possans = -1;
        for (int p=0; p<pc && primes[p]<limit; p++) {
            long long P = primes[p];
            if (P<=biggest) continue;
            long long two = ((nums[2]-nums[1])%P+P)%P;
            long long one = ((nums[1]-nums[0])%P+P)%P;
            long long A = (inverse(one,P)*two)%P;
            for (int k=2; k<K-1; k++) {
                long long onea = ((nums[k]-nums[k-1])%P+P)%P;
                long long twoa = ((nums[k+1]-nums[k])%P+P)%P;
                if ((onea*A)%P!=twoa) goto nope;
            }
            {
            long long B = ((nums[1]-A*nums[0])%P+P)%P;
            long long here = ((A*nums[K-1]+B)%P+P)%P;
            if (possans==-1) possans = here;
            else if (possans!=here) {
                printf("I don't know.\n");
                goto nope2;
            }
            }
            nope:;
        }
        printf("%I64d\n",possans);
        nope2:;
    }
}
