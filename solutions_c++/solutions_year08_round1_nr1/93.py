#include<iostream>
#include<string>
#include<algorithm>
#include<map>
#include<memory>
#include<functional>

using namespace std;

int main() {
    int t, n;
    long long x[1000], y[1000];
    cin >> t;
    for(int c=1; c<=t; c++) {
        cin >> n;
        for(int i=0; i<n; i++) cin >> x[i];
        for(int i=0; i<n; i++) cin >> y[i];
        
        sort(x, x+n);
        sort(y, y+n, greater<long long>());
        
        long long s = 0;
        for(int i=0; i<n; i++) s += x[i]*y[i];
        cout << "Case #" << c << ": " << s << endl;
    }
}
