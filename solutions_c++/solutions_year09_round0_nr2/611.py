#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <list>
#include <set>
#include <ios>
#include <map>
#include <algorithm>

using namespace std;

struct cmp {
    vector<int>& m_ar;
    cmp(vector<int>& ar) : m_ar(ar) {}
    bool operator()(int el1, int el2) {return m_ar[el1] > m_ar[el2];}
};

int main(int argc, char* argv[])
{
	int N;

	cin >> N;

    for (int i = 1; i <= N; ++i) {
        int H, W;

        cin >> H >> W;

        int sz = H * W;

        vector<int> m(sz);
        for (int j = 0; j < sz; ++j)
            cin >> m[j];

        vector<int> sorted(sz);
        for (int j = 0; j < sz; ++j) sorted[j] = j;

        sort(sorted.begin(), sorted.end(), cmp(m));

        vector<list<int> > wf(sz); // for each cell = list of source cells
        for (int j = 0; j < sz; ++j) wf[j].push_back(j);

        for (int j = 0; j < sz; ++j) {
            int ind = sorted[j];
            int h = ind / W;
            int w = ind % W;
            int dest = ind;

            if (h - 1 >= 0 && m[ind - W] < m[dest]) dest = ind - W;
            if (w - 1 >= 0 && m[ind - 1] < m[dest]) dest = ind - 1;
            if (w + 1 < W && m[ind + 1] < m[dest]) dest = ind + 1;
            if (h + 1 < H && m[ind + W] < m[dest]) dest = ind + W;

            if (dest != ind) {
                for (list<int>::iterator it = wf[ind].begin(); it != wf[ind].end(); ++it) wf[dest].push_back(*it);
                wf[ind].clear();
            }
        }

        vector<int> wt(sz);

        for (int j = 0; j < sz; ++j)
            if (wf[j].size())
                for (list<int>::const_iterator it = wf[j].begin(); it != wf[j].end(); ++it)
                    wt[*it] = j;

        vector<vector<char> > res(H);
        for (int j = 0; j < H; ++j) res[j].resize(W);
        char l = 'a';
        map<int, char> ml;
        for (int j = 0; j < sz; ++j) {
            if (ml.find(wt[j]) == ml.end()) {
                ml[wt[j]] = l;
                ++l;
            }
            res[j / W][j % W] = ml[wt[j]];
        }

        cout << "Case #" << i << ":" << endl;
        for (int j = 0; j < H; ++j) {
            for (int k = 0; k < W; ++k)
                cout << (k ? " " : "") << res[j][k];
            cout << endl;
        }
    }

	return 0;
}
