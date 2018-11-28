#include<iostream>

using namespace std;

int main() {
    int T;
    cin >> T;
    for(int t=1; t<=T; t++) {
        int n, a[40];
        char buf[41];
        cin >> n;
        for(int i=0; i<n; i++) {
            cin >> buf;
            a[i] = -1;
            for(int j=n-1; j>=0; j--) {
                if(buf[j] == '1') {
                    a[i] = j;
                    break;
                }
            }
        }

        int y = 0;
        for(int i=0; i<n; i++) {
            int x = -1;
            for(int j=i; j<n; j++) {
                if(a[j] <= i) {
                    x = j;
                    break;
                }
            }
            y += x - i;
            for(int j=x; j>i; j--) {
                a[j] = a[j-1];
            }
        }

        cout << "Case #" << t << ": " << y << endl;
    }
}

