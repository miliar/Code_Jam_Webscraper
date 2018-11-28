#include <iostream>
#include <string>

using namespace std;

long long int d[512][512];

long long pow2[512];


long long bin[512][512];

long long int B(int n, int k){
   long long res = 0;
   if (k == 0 || k == n)
       return 1;
   
   if (bin[n][k] != -1)
       return bin[n][k];
   
   res = (B(n-1, k-1) + B(n-1, k)) % 100003;
   bin[n][k] = res;
   return res;
}

long long int D(int n, int i){
   // cout << "(" << n << ", " << i << ")" << endl;
    if (i == 1)
        return 1;
    if (d[n][i] != -1)
        return d[n][i];
    
    int t;
    long long r = 0;
    
    
    for (t = 1; t < i; t++){
        //r = (r + (D(i, t) * pow2[i - t - 1])) % 100003;
        if (t < 2*i - n)
            continue;
        r = (r + (D(i, t) * B(n - i - 1, i - t - 1))) % 100003;
    }
    
    d[n][i] = r;
    return r;
}

int main(){
    int T;
    cin >> T;
    
    /*pow2[0] = 1;
    for (int i = 1; i < 512; i++)
        pow2[i] = (pow2[i-1] * 2 ) % 100003;*/
    
        for (int i = 0; i < 512; i++)
            for (int j = 0; j < 512; j++)
                bin[i][j] = -1;    
    
    for (int t = 0; t < T; t++){
        int n;
        cin >> n;
        for (int i = 0; i <= n; i++)
            for (int j = 0; j <= n; j++)
                d[i][j] = -1;
            
        
        long long int res = 0;
        
        for (int i = 1; i < n; i++)
            res = (res + D(n, i)) % 100003;
        cout << "Case #" << t+1 << ": " << res << endl;
    }
    return 0;
}
