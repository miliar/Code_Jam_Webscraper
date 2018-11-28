
#include <cstdio>
#include <fstream>
#include <string>
#include <vector>
#define MOD 10000

using namespace std;

const string p = "welcome to code jam";

int solve(const string& w) {
    int count[500][20];
    for(int i = 0; i < w.size(); ++i)
        count[i][0] = (w[i] == p[0]) ? 1 : 0;
    
    for(int j = 1; j < p.size(); ++j) {
        for(int i = 0; i < w.size(); ++i) {
            count[i][j] = 0;
            if(w[i] != p[j]) continue;
            for(int k = 0; k < i; ++k)
                count[i][j] = (count[i][j] + count[k][j-1]) % MOD;
        }
    }
    
    int ans = 0;
    for(int i = 0; i < w.size(); ++i)
        ans = (ans + count[i][p.size()-1]) % MOD;
    
    return ans;
}

int main() {
    ifstream fin("C-large.in");
    FILE *fout = fopen("C-large.out", "w");
    
    string w;
    getline(fin, w);
    int N = atoi(w.c_str());
    for(int i = 0; i < N; ++i) {
        getline(fin, w);
        fprintf(fout, "Case #%d: %04d\n", i+1, solve(w));
    }
    
    return 0;
}
