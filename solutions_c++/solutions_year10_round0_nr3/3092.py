#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main() {
    int t, cas = 1; cin >> t;
    while(t--) {
        long long r,k,n; cin >> r >> k >> n;
        queue<long long> c, c2;
        while(n--) {
            long long aux; cin >> aux;
            c.push(aux);
        }
        long long earn = 0, cap = 0;
        while(r--) {
            while(not c.empty() and cap + c.front() <= k) {earn += c.front(); cap += c.front(); c2.push(c.front()); c.pop();}
            while(not c2.empty()) {c.push(c2.front()); c2.pop();}
            cap = 0;
        }
        cout << "Case #" << cas++ << ": " << earn << endl;
    }
}