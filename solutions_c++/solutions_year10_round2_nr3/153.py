#include <iostream>
#include <vector>

using namespace std;

long long cache[510][510];
long long cache2[510][510];
long long MO = 100003;

int nCm(int n, int m) {
    if (m == 0) return 1;
    if (n == 0) return 0;
    
    long long &ans=cache2[n][m];
    if (ans >= 0) return ans;

    return ans=(nCm(n-1, m) + nCm(n-1,m-1)) % MO;
}

// Number of sequences of length len that start with n
int f(int n, int len) {
    if (len == 1) return 1;
    long long &ans=cache[n][len];
    if(ans>=0) return ans;

    ans=0;
    // The sequence must contain element 'len'
    for(int pos=len-1; pos >= 1; pos--) {
        long long cur = f(len, pos);
        cur *= nCm(n-len-1, len-pos-1);
        ans += cur;
        ans %= MO;
    }

    return ans;
}


int main() {
    int cases;
    cin >> cases;

    memset(cache,-1,sizeof(cache));
    memset(cache2,-1,sizeof(cache2));
    //for(int i=1; i<10; i++) for(int j=1; j<=i; j++) cout << j << " " << i << " " <<  nCm(i,j)<<endl;

    for(int c=0; c<cases; c++) {
        int x;
        cin >> x;

        long long ans=0;
        for(int len=1; len<x; len++) {
            int cur = f(x,len);
            //cout << "f("<<x<<","<<len<<")="<<cur<<endl;
            ans += cur;
            ans %= MO;
        }

        cout << "Case #" <<(c+1) << ": " << ans << endl;
    }
}
