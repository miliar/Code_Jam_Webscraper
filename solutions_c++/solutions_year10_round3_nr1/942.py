/*
  Rope Intranet
*/
#include <iostream>
#include <fstream>
#include <set>
#include <vector>
#include <map>
#include <algorithm>
#include <cstring>

#define print(x) cout << #x" = " << x << endl

using namespace std;

int N, ret;
vector<pair<int, int> > w;

int main(void) {
    int t = 1, n;

    cin >> n;

    while(n--) {
        cin >> N;
        
        w.clear();
        ret = 0;

        for (int i = 0; i < N; i++) {
            int a, b;
            cin >> a >> b;
            w.push_back(make_pair(a, b));
        }

        sort(w.begin(), w.end());

        for (int i = 0; i < N; i++) {
            for (int j = i + 1; j < N; j++) {
                if (w[i].second > w[j].second) {
                    ret++;
                }
            }
        }

        cout << "Case #" << t++ << ": " << ret << endl;
    }

    return 0;
}
