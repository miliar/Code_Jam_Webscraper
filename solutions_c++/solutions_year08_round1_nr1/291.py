#include <iostream>
#include <algorithm>
using namespace std;

int ans(){
    int n1[9], n2[9], n;
    cin >> n;
    int ret = 0;
    for(int i = 0; i < n; ++i) cin >> n1[i];
    sort(n1, n1 + n);
    for(int i = 0; i < n; ++i) {cin >> n2[i]; ret += n1[i] * n2[i];}
    
    while( next_permutation(n1, n1 + n) ){
        int tmp = 0;
        for(int i = 0; i < n; ++i) tmp += n1[i] * n2[i];
        if(tmp < ret) ret = tmp;
    }
    return ret;
    
}

int main(){
    int c; cin >> c;
    for(int i = 1; i <= c; i++){
        cout << "Case #" << i << ": " << ans() << endl;
    }
}
