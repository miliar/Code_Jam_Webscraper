#include <iostream>
#include <gmpxx.h>
#include <cstdio>

//#define TESTING

// compile with file.cpp -lgmpxx
// download from http://gmplib.org/#DOWNLOAD

typedef mpz_class mint;

using namespace std;

const mint MOD = 100003;

mint memo[1000];
mint memo2[1000][1000];
mint mrec[1000][1000];

mint fact(int n) {
    if(n < 2) return 1;
    if(memo[n] != -1) return memo[n];
    return memo[n] = fact(n - 1) * n;
}

mint nCr(int n, int r) {
	if(memo2[n][r] != -1) return memo2[n][r];
    mint res = fact(n)/fact(r)/fact(n-r); 
    //cout<<"RES: "<<res<<endl;
    return memo2[n][r] = res % MOD;
}

mint rec(int N, int size) {
	if(mrec[N][size] != -1) return mrec[N][size];
    if(size == 1) return mrec[N][size] = 1;
    mint ret = 0;
    for(int i = 0; i < size - 1; ++i) {
        if(size - 2 - i <= N - size - 1) {
            ret += rec(size,i+1) * nCr(N-size - 1, size - 2 - i); 
            ret %= MOD;
            //cout<<"I: "<<i<<" N: "<<N<<" size: "<<size<<" ret: "<<ret<<endl;
        }
    }
    return mrec[N][size] = ret;
}

mint solve(int N) {
    mint sum = 0;
    for(int i = 1; i <= N - 1; ++i) {
        sum += rec(N,i);
        sum %= MOD;
    }
    return sum;
}

int main() {
	for(int i = 0; i < 1000; ++i) memo[i] = -1;

    for(int i = 0; i < 1000; ++i) {
        for(int j = 0; j < 1000; ++j) {
            memo2[i][j] = -1;
            mrec[i][j] = -1;
        }
    }

#ifndef TESTING
	int T;
    cin>>T;
    for(int Case = 1; Case <= T; ++Case) {
    	int N;
        cin>>N;
        cout<<"Case #"<<Case<<": "<<solve(N)<<endl;
    }

    /*
    cout<<nCr(4,2)<<endl;
    cout<<nCr(3,2)<<endl;
    cout<<nCr(8,4)<<endl;
    */
#else

    //cout<<rec(3,2)<<endl;
    //cout<<rec(5,2)<<endl;

    for(int i = 2; i < 500; ++i) cout<<solve(i)<<endl;

#endif
    return 0;
}
