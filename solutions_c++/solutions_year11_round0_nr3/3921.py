#include<cstdio>
#include<vector>
#include<iostream>
using namespace std;

int getsum(vector<int> &arr, int flag, int& realsum) {
    int n = arr.size();
    int sum = 0;
    realsum = 0;
    for(int i = 0; i < n ;i++) {
        if(flag%2) {sum ^= arr[i];realsum += arr[i]; }
        flag /= 2;
    }
    return sum;
}
int main() {
    int t, n;
    cin >> t;
    for(int i = 1; i <= t; i++ ) {
        vector<int> arr;
        cin >> n;
        for(int j = 0; j < n ;j++) {
            int num;
            cin >> num;
            arr.push_back(num);
        }
        int res = -1;
        for(int k = 0; k < (1<<n); k++) {
            int k1 = (1<<n) -k-1;
            if(k == 0 || k1 == 0) {
                continue;
            }
            int realsum1, realsum2;
            int sum1 = getsum(arr, k, realsum1);
            int sum2 = getsum(arr, k1, realsum2);
            if(sum1 == sum2) {
                if(realsum1 > res) res = realsum1;
                if(realsum2 > res) res = realsum2;
            }
        }
        cout<< "Case #"<< i<<": ";
        if(res == -1) cout<< "NO";
        else cout <<res;
        cout << "\n";
    }
}

