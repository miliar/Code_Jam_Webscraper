#include<iostream>

using namespace std;

int main() {
    int t;
    cin >> t;
    for(int i = 0; i < t; i++) {
        int R, k, N;
        cin >> R >> k >> N;
        int* groups = new int[N];
        int sum = 0;
        for(int j = 0; j < N; j++) {
            cin >> groups[j];
            sum += groups[j];
        }
        if(sum <= k) {
            cout << "Case #" << (i+1) << ": " << (R*sum) << endl;
        } else {
            int s = 0, c, p = -1;
            for(int _i = 0; _i < R; _i++) {
                c = 0;
                while((c + groups[(p+1)%N]) <= k) {
                    p = (p+1)%N;
                    c += groups[p];
                }
                s += c;
            }
            cout << "Case #" << (i+1) << ": " << s << endl;
        }
        delete [] groups;
    }
}
