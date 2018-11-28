#include <iostream>
#include <vector>

using namespace std;

int main(){
    int T;
    cin >> T;
    for(int ii = 1; ii <= T; ++ii){
        int n;
        cin >> n;
        int res = 0;
        for(int i = 0; i < 1<<(n-2); ++i){
            vector<int> a(n+1);
            int c = 1;
            for(int j = 0; j < n-2; ++j){
                if(i & 1<<j){
                    a[j+2] = c++;
                }
            }
            a[n] = c;
            while(c > 1){
                c = a[c];
            }
            if(c == 1){
                res++;
                res %= 100003;
            }
        }
        cout << "Case #" << ii << ": " << res << endl;
    }
    return 0;
}
