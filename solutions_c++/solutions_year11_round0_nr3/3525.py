#include <cstdio>
inline long add(long a,long b) {
    long s = ~ (a & b);
    return (s & a) | (s & b);
}
long work() {
    long n;
    scanf("%ld",&n);
    long i;
    long sum_p = 0;
    long sum_c = 0;
    long t;
    unsigned long little = -1;
    //printf("%lx\n",little);
    for (i = 0; i < n; ++i) {
        scanf("%ld",&t);
        sum_p += t;
        sum_c = add(sum_c,t);
        if (t < little) little = t;
    }
    if (sum_c) 
        return -1;
    else
        return sum_p - little;

}
int main() {
    long test;
    scanf("%ld",&test);
    //printf("test is %d\n",test);
    long i;
    for (i = 0; i < test; ++i) {
        long result = work();
        if (result < 0) 
            printf("Case #%ld: NO\n",i+1);
        else
            printf("Case #%ld: %ld\n",i+1,result);
    }
    return 0;
}
