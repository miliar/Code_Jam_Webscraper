#include <iostream>
#include <vector>
#include <memory>
#include <queue>
#include <stack>

using namespace std;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int c;
    cin >> c;
    
    for(int p=0; p<c; ++p) {
        int n, k, b, t, res = 0;
        cin >> n >> k >> b >> t;
        vector <int> X(n);
        vector <int> V(n);
        vector <bool> came(n, false);
        for(int i=0; i<n; ++i) cin >> X[i];
        for(int i=0; i<n; ++i) cin >> V[i];
        
        for(int i=0; i<n; ++i)
            if(X[i] + V[i]*t >= b) 
                came[i] = true;
        
        for(int i=n-1; i>=0 && k>0; --i)
            if(came[i]) {
                for(int j=i+1; j<n; ++j)
                    if(!came[j]) 
                        res++;
                k--;
            }
        
        if(k>0) printf("Case #%d: IMPOSSIBLE\n", p+1);
        else printf("Case #%d: %d\n", p+1, res);
    }

    return 0;
}
