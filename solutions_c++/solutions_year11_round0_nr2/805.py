#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <fstream>
using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

int has[256];
char combine[256][256];
bool opposed[256][256];

void Solve(int testid, const vector<char>& seq) {
    vector<char> res;
    for (int i = 0; i < seq.size(); ++i) {
        char c = seq[i];
        res.push_back(c);
        has[c]++;
        if (res.size() >= 2 && combine[res[res.size() - 2]][res[res.size() - 1]])  {
            c = combine[res[res.size() - 2]][res[res.size() - 1]];
            has[res[res.size() - 1]]--;
            res.erase(res.begin() + res.size() - 1);
            has[res[res.size() - 1]]--;
            res.erase(res.begin() + res.size() - 1);
            res.push_back(c);
            has[c]++;
        }
        else if (res.size() > 0) {
            for (int j = 0; j < 256; ++j) {
                if (has[j] && opposed[res[res.size() - 1]][j]) {
                    res.clear();
                    for (int k = 0; k < 256; ++k)
                        has[k] = 0;
                    break;
                }
            }
        }
    }
    fout << "Case #" << testid + 1 << ": [";
    if (res.size() > 0)
        fout << res[0];
    for (int i = 1; i < res.size(); ++i)
        fout << ", " << res[i];
    fout << "]\n";
}

int main() {
    int T; fin >> T;
    for (int testid = 0; testid < T; ++testid) {
        for (int i = 0; i < 256; ++i) {
            has[i] = 0;
            for (int j = 0; j < 256; ++j) {
                combine[i][j] = 0;
                opposed[i][j] = false;
            }
        }
        int C; fin >> C;
        for (int i = 0; i < C; ++i) {
            string s;
            fin >> s;
            combine[s[0]][s[1]] = s[2];
            combine[s[1]][s[0]] = s[2];
        }
        int D; fin >> D;
        for (int i = 0; i < D; ++i) {
            string s;
            fin >> s;
            opposed[s[0]][s[1]] = true;
            opposed[s[1]][s[0]] = true;
        }
        int N; fin >> N;
        vector<char> seq(N);
        for (int i = 0; i < N; ++i)
            fin >> seq[i];
        Solve(testid, seq);
    }
    return 0;
}