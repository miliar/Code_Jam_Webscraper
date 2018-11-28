#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int test;
    cin >> test;
    
    for(int cases = 1; cases <= test; ++cases) {
        int a[5000];
        int N;
        int possible = 0;
        cin >> N;
        for(int i = 0; i < N; ++i) {
            cin >> a[i];
            possible = possible ^ a[i];
        }
        
        if(possible != 0) {
            cout << "Case #" << cases << ": NO" << endl;
        }
        else {
            sort(a, a+N);
            int sum = 0;
            for(int i = 1; i < N; ++i) {
                sum += a[i];
            }
            
            cout << "Case #" << cases << ": " << sum << endl;
        }
    }
    
    return 0;
}
