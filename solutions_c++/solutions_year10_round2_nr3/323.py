#include <iostream>

using namespace std;

#define PRIME 100003

long long memo[600][600];
long long inv[700];

long long power(long long x,long long y){
     if (y == 0) return 1;
     long long res = power(x,y/2);
     res = res*res;
     res%= PRIME;
     if (y%2 == 1) res*=x;
     res%= PRIME;
     return res;
}

long long comb(long long x,long long y){
     long long res =1;
     for (int i=1;i<=y;i++){
         res*=x-i+1;
         res*=inv[i];
         res%= PRIME;
     }
     return res;
}

long long f(long long x,long long y){
     //cerr << "entro con " << x << " " << y << endl;
     if (memo[x][y] != -1) return memo[x][y];
     long long res = 0;
     for (int npos = 1;npos<=y-1;npos++){
         res+=comb(y-npos-1,x-y-1)*f(y,npos);
     }
     memo[x][y] = res;
     return res;
}

int main(){
    for (int i=0;i<600;i++) for (int j=0;j<600;j++) memo[i][j] = -1;
    for (int i=1;i<600;i++) memo[i][1] = 1;
    for (int i=1;i<700;i++) inv[i] = power(i,PRIME-2);
    int nc; cin >> nc;
    for (int i=1;i<=nc;i++){
        int x; cin >> x;
        long long res =0;
        for (int y=1;y<=x-1;y++) res+=f(x,y);
        cout << "Case #" << i << ": " << res%PRIME << endl;
    }
    return 0;
}
