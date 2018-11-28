#include <iostream>
#include <vector>
#include <utility>
#include <fstream>
using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

void Solve(int id, const vector<pair<int, int> > plan[2]) {
    int pos0 = 1;
    int pos1 = 1;
    int planid0 = 0;
    int planid1 = 0;
    int time = 0;
    for (; planid0 < plan[0].size() || planid1 < plan[1].size(); ++time) {
        bool push0 = false;
        bool push1 = false;

        if (planid0 < plan[0].size()) {
            if (pos0 < plan[0][planid0].first) pos0++;
            else if (pos0 > plan[0][planid0].first) pos0--;
            else push0 = true;
        }

        if (planid1 < plan[1].size()) {
            if (pos1 < plan[1][planid1].first) pos1++;
            else if (pos1 > plan[1][planid1].first) pos1--;
            else push1 = true;
        }

        if (push0 && !push1 && (planid1 >= plan[1].size() || plan[0][planid0].second < plan[1][planid1].second))
            planid0++;
        else if (!push0 && push1 && (planid0 >= plan[0].size() || plan[0][planid0].second > plan[1][planid1].second))
            planid1++;
        else if (push0 && push1) {
            if (plan[0][planid0].second < plan[1][planid1].second)
                planid0++;
            else 
                planid1++;
        }
    }
    fout << "Case #" << id + 1 << ": " << time << endl;
}

int main() {
    int n; fin >> n;
    for (int i = 0; i < n; ++i) {
        int len; fin >> len;
        vector<pair<int, int> > plan[2];
        for (int j = 0; j < len; ++j) {
            char botch; fin >> botch;
            int pos; fin >> pos;
            plan[botch == 'O' ? 0 : 1].push_back(make_pair(pos, j));
        }
        Solve(i, plan);
    }
    return 0;
}