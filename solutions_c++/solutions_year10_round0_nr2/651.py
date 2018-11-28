#include <iostream>
#include <cmath>

using namespace std;

int nc;

int mcd(int a, int b){
    if (a == 0) return b;
    if (b == 0) return a;
    return mcd(b,a%b);
}

int main(){
    cin >> nc;
    for (int q = 1; q <= nc;q++){
        int N; cin >> N;
        int nums[N];
        for (int i=0;i<N;i++) cin >> nums[i];
        int curr = abs(nums[0] - nums[1]);
        for (int i=0;i<N;i++){
            for (int j=i+1;j<N;j++){
                curr = mcd(curr,abs(nums[i]-nums[j]));
            }
        }
        //cout << curr << endl;
        long long res = -1000000000;
        /*for (int i=0;i<N;i++){
            int x;
            if (nums[i] % curr == 0) x = nums[i]/curr;
            else x = nums[i]/curr + 1;
            res >?= curr*x;
        }
        cout << res << endl;*/
        if (nums[0] % curr == 0) res = 0;
        else res = curr - nums[0] % curr;
        cout << "Case #" << q << ": " << res << endl;
    }
    return 0;
}
