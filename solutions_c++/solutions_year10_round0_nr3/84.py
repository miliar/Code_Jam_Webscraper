#include <cstdio>
#include <vector>

using namespace std;

int get() { int x; scanf("%d",&x); return x;}

long long go() {
    int r = get();
    int k = get();
    int n = get();

    vector<int> g(n);
    for(int i=0;i<n;i++) {
        g[i]=get();
    }

    vector<int> whosNext(n);
    vector<int> rideSize(n);

    long long rs=g[0];
    int j=1;
    for(int i=0;i<n;i++) {
        if(i!=0){
            rs-=g[i-1];
        }
        while(!(rs&&i==j) && rs+g[j]<=k) {
            rs+=g[j];
            j = (j+1)%n;
        }
        whosNext[i]=j;
        rideSize[i]=rs;
        //printf("next %d is %d, rs = %lld\n",i,j,rs);
    }

    long long ret=0;

    {
        int j=0;
        for(int i=0;i<r;i++) {
            ret+=rideSize[j];
            j = whosNext[j];
        }
    }
    return ret;
}

int main() {
    int t = get();
    for(int i=0;i<t;i++) {
        printf("Case #%d: %lld\n",i+1,go());
    }
}
