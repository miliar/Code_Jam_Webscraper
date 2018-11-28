#include <iostream>
#include <vector>

using namespace std;

double go(vector<int> v, bool b);

bool done[1200];
double solve(int c) {
    if (c ==0 || c== 1) return 0;
    return c;
}

double go(vector<int> v, bool zeroOnCycle) {
    memset(done, 0, sizeof(done));

    vector<int> lens;
    for(int i=0; i<v.size(); i++) {
        int pt = i;
        int len = 0;
        while(!done[pt])
        {
            done[pt] = true;
            pt = v[pt];
            len++;
        }

        if (len == v.size() && zeroOnCycle) { return -1;}

        if (len > 0) lens.push_back(len);
    }

    double ans = 0;
    for(int i=0; i<lens.size(); i++) ans += solve(lens[i]);

    return ans;
}

int main() {
    int cases;
    cin >> cases;

    for(int c=0; c<cases; c++) {
        int N;
        cin >> N;
        vector<int> v;
        v.resize(N);
        for(int i=0; i<N; i++) { cin >> v[i]; v[i]--; }

        cout << "Case #" <<(c+1) << ": " << go(v, false) << endl;
    }
}
