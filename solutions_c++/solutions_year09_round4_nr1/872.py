#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Milkshakes {
    
public:
    
    int Solve(
            int N,
            vector<string> G) {
        vector<int> V(N);
        for(int i = 0; i < N; ++i)
            V[i] = G[i].find_last_of('1');
        int ans = 0;
        for(int i = 0, j; i < N; ++i) {
            for(j = i; j < N && V[j] > i; ++j);
            for(; j > i; --j) {
                swap(V[j], V[j-1]);
                ++ans;
            }
        }
        return ans;
    }
    
};

int main(int argc, char* argv[]) {
    //*
    if(argc == 1) return 0;
    string inpath = argv[1];
    string outpath = inpath.substr(0, inpath.find_last_of('.')) + ".out";
    freopen(inpath.c_str(), "r", stdin);
    freopen(outpath.c_str(), "w", stdout);
    //*/
    Milkshakes m;
    
    int T, N, M;
    cin >> T;
    for(int c = 1; c <= T; ++c) {
        cin >> M;
        vector<string> G(M);
        for(int i = 0; i < M; ++i) {
            cin >> G[i];
        }
        cout << "Case #" << c << ": ";
        cout << m.Solve(M, G) << endl;
    }
}

