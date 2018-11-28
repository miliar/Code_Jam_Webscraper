#include <algorithm>
#include <vector>
#include <sstream>
#include <set>
#include <iostream>
#include <map>
#include <iomanip>
#include <fstream>
#include <locale>
#include <cmath>
#include <queue>
using namespace std;

int main() {
#ifndef ONLINE_JUDGE
    ifstream cin("A-large (1).in");
#endif
    ofstream cout("out.txt");
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        cout << "Case #" << t+1 << ": ";
        int N;
        cin >> N;
        vector<int> d(N), l(N);
        for (int i = 0; i < N; i++)
            cin >> d[i] >> l[i];
        int D;
        cin >> D;
        vector<int> mx(N);
        int pos = 0;
        mx[0] = d[0]*2;
        bool res = (mx[0] >= D);
        for (int i = 0; i < N; i++) {
            int dist = mx[i];
            for (int j = i+1; j < N; j++) {
                if (d[j] > dist)
                    break;
                mx[j] = max(mx[j], d[j] + min(d[j] - d[i], l[j]));
                if (mx[j] >= D)
                    res = true;
            }
        }
        //cout << mx[N-1] << endl;
        cout << (res ? "YES" : "NO");
        cout << endl;
    }
}
