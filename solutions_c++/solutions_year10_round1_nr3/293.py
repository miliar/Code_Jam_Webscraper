#include<iostream>
#include<algorithm>

using namespace std;

bool f(int a, int b) {
    if(b > a) return f(b, a);
    if(a == 0 or b == 0) return true;
    if(a == b) return false;
    if(a <= 2 * b) return not f(b, a - b);
    else return true;
}

int main() {
    int T, A1, A2, B1, B2;
    cin >> T;
    for(int t = 1; t <= T; t++) {
        cin >> A1 >> A2 >> B1 >> B2;
        int n = 0;
        for(int i = A1; i <= A2; i++) {
            for(int j = B1; j <= B2; j++) {
                n += f(i, j);
            }
        }
        cout << "Case #" << t << ": " << n << endl;
    }
}

