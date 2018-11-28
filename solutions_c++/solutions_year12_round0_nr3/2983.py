#include <iostream>
#include <vector>

using namespace std;

int calc(int a, int b){
    int cnt = 0;
    for(int i = a; i <= b; ++i){
        int d = 0;
        int t = i;
        if(t == 0) d = 1;
        else{
            while(t > 0){
                t /= 10;
                d++;
            }
        }
        int exp = 1;
        int num = i;
        vector<bool> used(10001);
        for(int j = 1; j < d; ++j) exp *= 10;
        for(int j = 1; j < d; ++j){
            t = (num / exp);
            num -= t * exp;
            num *= 10;
            num += t;
            if(used[num]) continue;
            used[num] = true;
            
            if(i < num && num <= b) cnt++;
        }
    }
    return cnt;
}

int main(){
    int n, a, b;
    cin >> n;
    for(int i = 1; i <= n; ++i){
        cin >> a >> b;
        cout << "Case #" << i << ": " << calc(a, b) << endl;
    }
    return 0;
}
