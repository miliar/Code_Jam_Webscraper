#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
#include <set>
using namespace std;
typedef pair<int, int> P;
const int X = 2000000;
vector<P> v;
int pow10[10];

int numLen(int n) {
    for(int i = 1; i < 10; i ++) {
        if(pow10[i] > n) {
            return i;
        }
    }
    return 1;
}

int main() {
    pow10[0] = 1;
    for(int i = 1; i < 10; i ++) pow10[i] = 10 * pow10[i - 1];
    for(int A = 1; A <= X; A ++) {
        int len = numLen(A);
        set<int> st;
        for(int j = 1; j < len; j ++) {
            int B = A / pow10[len - j] + pow10[j] * (A % pow10[len - j]);
            if(A < B && st.count(B) == 0) {
                v.push_back(P(A, B));
                st.insert(B);
            }
        }
    }
    int t, a, b;
    cin >> t;
    for(int i = 0; i < t; i ++) {
        cin >> a >> b;
        int result = 0;
        for(int j = 0; j < v.size(); j ++) {
            if(v[j].first >= a && v[j].second <= b) {
                result ++;
            }
        }
        cout << "Case #" << i + 1 << ": " << result << endl;
    }
    return 0;
}
