#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

struct Cir {
    double x, y, r;
    void get() { cin >> x >> y >> r; }
};

double calc(Cir c1, Cir c2) {
    return (sqrt(double((c1.x-c2.x)*(c1.x-c2.x)+(c1.y-c2.y)*(c1.y-c2.y)))+ c1.r+c2.r)/2;
}

class Milkshakes {
    
public:
    
    double Solve(
            int N,
            vector<Cir > G) {
            double ans = 1e99;
        if(N == 1) return G[0].r;
        else if(N == 2) return max(G[0].r, G[1].r);
        else {
            ans <?= max(G[0].r, calc(G[1], G[2]));
            ans <?= max(G[1].r, calc(G[0], G[2]));
            ans <?= max(G[2].r, calc(G[1], G[0]));
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
        vector<Cir> G(M);
        for(int i = 0; i < M; ++i) {
            G[i].get();
        }
        cout << "Case #" << c << ": ";
        printf("%.6lf\n",m.Solve(M, G)) ;
    }
}

