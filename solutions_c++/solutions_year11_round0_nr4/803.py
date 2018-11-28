#include <iostream>
#include <vector>
#include <queue>
#include <iomanip>
#include <fstream>
using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

vector<vector<int> > edges;

void Solve(int testid, const vector<int>& p) {
    edges.assign(p.size(), vector<int>());
    for (int i = 0; i < p.size(); ++i) {
        edges[i].push_back(p[i]);
        edges[p[i]].push_back(i);
    }

    double E = p.size();
    vector<bool> was(p.size(), false);
    for (int i = 0; i < p.size(); ++i) {
        if (was[i])
            continue;
        vector<int> comp;
        queue<int> vertices;
        vertices.push(i);
        was[i] = true;
        while (!vertices.empty()) {
            int v = vertices.front();
            vertices.pop();
            comp.push_back(v);
            for (vector<int>::const_iterator it = edges[v].begin(); it != edges[v].end(); ++it) {
                int adjv = *it;
                if (!was[adjv]) {
                    was[adjv] = true;
                    vertices.push(adjv);
                }
            }
        }
        if (comp.size() == 1)
            E -= 1.0;
    }

    fout << "Case #" << testid + 1 << ": " << setprecision(6) << E << endl;
}

int main() {
    int T; fin >> T;
    for (int testid = 0; testid < T; ++testid) {
        int N; fin >> N;
        vector<int> p(N);
        for (int i = 0; i < N; ++i) {
            int a;
            fin >> a;
            p[i] = a - 1;
        }
        Solve(testid, p);
    }
    return 0;
}