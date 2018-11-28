#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int pow2(int a){
    int ans = 1;
    for(int i = 1; i <= a; ++i)
        ans*= 2;
    return ans;
}

void f(vector<int> &candies, int &sum1, int &xsum1, int &sum2, int &xsum2, int n){
    int l = candies.size();
    int mask = 1;
    
    for(int i = 0; i < l; ++i){
        if(n & mask){
            sum1 += candies[i];
            xsum1 = (xsum1 == 0)?candies[i]:xsum1^candies[i];
        }
        else{
            sum2 += candies[i];
            xsum2 = (xsum2 == 0)?candies[i]:xsum2^candies[i];
        }
        mask *= 2;
    }
}

int main(){
    int T, N, c;
    c = 1;
    cin >> T;
    while(T--){
        cin >> N;
        vector<int> candies(N);
        int tmp;
        for(int i = 0; i < N; ++i){
            cin >> tmp;
            candies[i] = tmp;
        }
        int n = pow2(N);
        int maxsum, xsum1, xsum2, sum1, sum2;
        maxsum = xsum1 = xsum2 = sum1 = sum2 = 0;
        for(int i = 1; i < n-1; ++i){
            xsum1 = xsum2 = sum1 = sum2 = 0;
            f(candies, sum1, xsum1, sum2, xsum2, i);
            if(xsum1 == xsum2){
                maxsum = max(maxsum, max(sum1,sum2));
            }
        }
        cout << "Case #" << c++ << ": ";
        if(maxsum > 0)
            cout << maxsum;
        else
            cout << "NO";
        cout << endl;
    }
    return 0;
}
