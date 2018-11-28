#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

vector< pair <int, int> > com;

int sign(int v) {
    return v > 0 ? 1 : (v < 0) ? - 1 : 0;
}

int nextCom(int pos, int type) {
    int i;
    for (i = pos; i < com.size(); i++)
        if (com[i].second == type) break;
    return i;
}

int main()
{
    ifstream fin("in.dat");
    ofstream fout("out.dat");
    int i, test, T, N, p;
    string s;
    fin >> T;
    for (test = 1; test <= T; test++) {
        fin >> N;
        com.clear();
        for (i = 0; i < N; i++) {
            fin >> s >> p;
            com.push_back(make_pair(p, s == "O" ? 0 : 1));
        }

        int res = 0;
        int r[2], dx[2] = {0, 0};
        int pos[2] = {1, 1};
        r[0] = nextCom(0, 0), r[1] = nextCom(0, 1);

        while (r[0] < N || r[1] < N) {
            res++;
            for (i = 0; i < 2; i++) {
                if (r[i] == N) continue;
                dx[i] = sign(com[r[i]].first - pos[i]);
                pos[i] += dx[i];
            }

            if (r[0] < r[1]) {
                if (!dx[0]) r[0] = nextCom(r[0] + 1, 0);
            }
            else if (!dx[1]) r[1] = nextCom(r[1] + 1, 1);
        }

        fout << "Case #" << test << ": " << res << endl;
    }
    return 0;
}
