#include <iostream>
#include <vector>
#include <queue>
#include <memory>
#include <stack>

using namespace std;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt","w", stdout);
    int T;
    cin >> T;
    
    for(int p=0; p<T; ++p) {
        int n, res = 0;
        cin >> n;
        vector <int> A(n), B(n);
        for(int i=0; i<n; ++i)
            cin >> A[i] >> B[i];
        for(int i=0; i<n; ++i)
           for(int j=0; j<n; ++j)
               if((A[i]>A[j] && B[i]<B[j]) ||(A[i]<A[j] && B[i]>B[j]))
                   res++;
        
        res /= 2;
        
        printf("Case #%d: %d\n", p+1, res);
    }
    
    return 0;
}
