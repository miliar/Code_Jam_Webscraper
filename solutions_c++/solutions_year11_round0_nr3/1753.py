#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

int C[1000];

int main() {
    int T;
    cin>>T;
    for (int t=1;t<=T;t++) {
        int N;
        cin>>N;
        int a = 0;
        int b = 0;
        for (int i=0;i<N;i++) {
            cin >> C[i];
            a ^= C[i];
            b += C[i];
        }
        if (a != 0) {
            cout << "Case #" << t << ": NO" << endl;
            continue;
        }
        sort(C, C+N);
        b -= C[0];
        cout << "Case #" << t << ": " << b << endl;
    }
}
