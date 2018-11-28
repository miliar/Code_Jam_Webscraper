#include <iostream>
#include <vector>

using namespace std;

int main(){
    int t;
    cin >> t;
    for(int k = 0; k < t; k++){
        long long n, l, h;
        cin >> n >> l >> h;

        vector<long long> freq(n);
        for(long long i = 0; i < n; i++){
            long long x;
            cin >> x;
            freq[i] = x;
        }

        bool yes = false;
        long long sol = -1;
        for(long long i = l; i <= h; i++){
            yes = true;
            for(long long j = 0; j < n; j++){
                long long f = freq[j];
                if(i % f != 0 && f % i != 0){
                    yes = false;
                    break;
                }
            }
            if(yes) {
                sol = i;
                break;
            }
        }

        cout << "Case #" << k+1 << ": ";
        if(sol != -1) cout << sol << endl;
        else cout << "NO" << endl;
    }
}
