#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>

using namespace std;

void solve(int caseN) {
    int ans = 0;
    vector<int> inQ;

    int N = 0;
    cin >> N;
    while(N--) {
        int v;
        cin >> v;
        inQ.push_back(v);
    }

    vector<int> sortedQ(inQ);

    sort(sortedQ.begin(), sortedQ.end());

    for(int i=0; i<inQ.size(); i++) {
        if(inQ[i] != sortedQ[i])
            ans++;
    }

    cout << "Case #" << caseN << ": " << ans << endl;
}

int main(int argc, void **argv) {
    int N;
    cin >> N;
    for(int i=0;i<N;i++) {
        solve(i+1);
    }
}

