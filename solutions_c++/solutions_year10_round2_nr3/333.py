#include <cstdio>
#include <cassert>
#include <vector>

using namespace std;

#define MOD (100003)

int get() { int x; scanf("%d",&x); return x;}

bool icncr[1000][1000];
int ncr[1000][1000];
int nCr(int n, int r) {
    if(r>n)return 0;
    if(n==0)return 1;
    if(r==0)return 1;
    if(icncr[n][r]) {
        return ncr[n][r];
    }
    icncr[n][r]=true;
    ncr[n][r]=(nCr(n-1,r)+nCr(n-1,r-1))%MOD;
    return ncr[n][r];
}

int ways(int lower,int upper,int numPlaces) {
    // k how many ways can we choose numbers between lower
    // and upper, inclusive, given that upper must be the last place?
    if(upper==lower)return numPlaces==1;
    upper--;
    numPlaces--;
    assert(upper>=lower);
    if(numPlaces<0) return 0;
    if(numPlaces==0) return 1;
    if(lower>upper)return 0;
    upper-=lower;
    lower-=lower;
    upper++;
    if(numPlaces>upper) {
        return 0;
    }
    // k, now fit [lower,upper) into numPlaces.
    // that's [0,upper) into numPlaces.
    // that's upper thinsg into numPlaces.
    // in other words, upper choose numPlaces.
    return nCr(upper,numPlaces);
}

bool icns[1000][1000];
int ca[1000][1000];
int nsets(int n, int size) {
    // n is the biggest element of a set of size size.
    // so... size must also be in the set.
    // but... where is it? is it the first one? the second?
    // all we know is that it is not the sizeth one.

    if(size==1) return 1;
    if(n<=size) return 0;

    if(icns[n][size]) {
        return ca[n][size];
    }
    icns[n][size]=true;
    int ans=0;
    for(int i=1;i<=size-1;i++) {
        // let's say that size will be the ith one
        int a= nsets(size,i);
        int b=ways(size+1,n,size-i);
        long temp=a;
        temp*=b;
        temp%=MOD;
        ans+=((int)temp);
        ans%=MOD;
    }
    ca[n][size]=ans;
    return ca[n][size];
}

int main() {
    int c = get();
    for(int i =0;i<c;i++) {
        int n=get();
        int ans=0;
        for(int j=1;j<=n;j++) {
            ans += nsets(n,j);
            ans %= MOD;
        }
        printf("Case #%d: %d\n",i+1,ans);
    }
    return 0;
}
