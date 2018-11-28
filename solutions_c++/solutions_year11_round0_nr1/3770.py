#include<iostream>

using namespace std;

int N;
int o, b;
pair<int, int> O[101];
pair<int, int> B[101];

int solve() {
    int t=0;
    int startO=0, startB=0;
    int currO = 1, currB = 1;
    while(startO < o && startB < b) {
        int next = 0;
        if (O[startO].second > B[startB].second) next = 1;
        int diffO = O[startO].first - currO;
        int diffB = B[startB].first - currB;
        int minDiff = min(abs(diffO), abs(diffB));
        if (next == 0) {
            if ( abs(B[startB].first - currB) > minDiff) minDiff++;
            t+= abs(diffO) + 1;
            if (diffB < 0) currB -= minDiff;
            else if (diffB > 0) currB += minDiff;
            currO = O[startO++].first;
        } else {
            if (abs(O[startO].first - currO) > minDiff) minDiff++;
            t+= abs(diffB) + 1;
            if (diffO < 0) currO -= minDiff;
            else if (diffO > 0) currO += minDiff;
            currB = B[startB++].first;
        }
    }
    while(startO < o) {
        int diff = O[startO++].first - currO;
        t += abs(diff) + 1;
        currO += diff;
    }
    while(startB < b) {
        int diff = B[startB++].first - currB;
        t += abs(diff) + 1;
        currB += diff;
    }
    return t;
}

int main() {
    int T;
    cin>>T;
    for(int t=1;t<=T;t++) {
        cin>>N;
        o=0, b=0;
        for(int i=0;i<N;i++) {
            char c;
            int n;
            cin>>c>>n;
            if (c == 'O') {
                O[o++] = make_pair(n, i);
            } else {
                B[b++] = make_pair(n, i);
            }
        }
        printf("Case #%d: %d\n", t, solve());
    }
}
