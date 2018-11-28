#include <iostream>
#include <algorithm>
#include <math.h>
#include <vector>

using namespace std;

int gcm(int a, int b) {
    while(1) {
        int c = a % b;
        if (c == 0) {
            return b;
        }
        a = b;
        b = c;
    }
}

int main() {
    int c;
    cin >> c;
    vector<int> ts;
    for (int i = 0; i < c; i ++) {
        int n;
        cin >> n;
        ts.clear();
        for (int j = 0; j < n; j ++) {
            int t;
            cin >> t;
            ts.push_back(t);
        }
        sort(ts.begin(), ts.end());
        int tmin = ts[0];

        // get the gcf for ts 1 and 2
        int cm;
        if (ts.size() == 2) {
            cm = ts[1] - tmin;
        } else { // ts.size() == 3
            cm = gcm(ts[1] - tmin, ts[2] - tmin);
        }
        double a = ((double)ts[0])/((double)cm);
        int aceil = ceil(a);
        int amul = aceil * cm;
        int answer = amul - ts[0];
        
        cout << "Case #" << (i+1) << ": " << answer << endl;
    }
}

