#include <iostream>
#include <vector>

using namespace std;

int calc(){
    int n, s, p;
    cin >> n >> s >> p;
    vector<int> A(n);
    for(int i = 0; i < n; ++i) cin >> A[i];
    // sort(A.begin(), A.end()); ?
    int ans = 0;
    for(int i = n - 1; i >= 0; --i){
        if(A[i] % 3 == 0){
            if(A[i] / 3 >= p){
                ans++;
            }else{
                if((A[i] / 3) + 1 >= p && s > 0 && A[i] != 0){
                    ans++;
                    s--;
                }
            }
        }else if(A[i] % 3 == 1){
            if((A[i] / 3) + 1 >= p){
                ans++;
            }
        }else{
            if((A[i] / 3) + 1 >= p){
                ans++;
            }else{
                if((A[i] / 3) + 2 >= p && s > 0){
                    ans++;
                    s--;
                }
            }
        }
    }
    return ans;
}

int main(){
    int t;
    cin >> t;
    for(int i = 1; i <= t; ++i)
        cout << "Case #" << i << ": " << calc() << endl;
    return 0;
}
