#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
using namespace std;

map<string, int> tbl;

int solve() {
    int N, M, result = 0;
    cin >> N >> M;
    string tmp;
    tbl.clear();
    for (int i = 0; i < N; ++i) {
        cin >> tmp;
        int idx = 1;
        tmp += '/';
        while ((idx = tmp.find('/',idx+1)) != -1) {
            tbl[tmp.substr(0, idx+1)]++;
        }
    }
    
    for (int i = 0; i < M; ++i) {
        cin >> tmp;
        int idx = 1;
        tmp += '/';
        while ((idx = tmp.find('/',idx+1)) != -1) {
            string key = tmp.substr(0, idx+1);
            if (tbl[key] == 0) result++;
            tbl[key]++;
        }
    }
    return result;
}

int main() {
    int T;
    cin >> T;
    for (int times = 1; times <= T; ++times) {
        cout << "Case #" << times << ": " << solve() << '\r' << endl;
    }
    return 0;
}
