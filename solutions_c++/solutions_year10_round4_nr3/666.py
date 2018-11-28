#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <iomanip>

using namespace std;

typedef long long ll;
typedef int ret_t;

class Solver {
public:
    void add(vector<pair<int, vector<int> > > & pos, int x, int y) {
        //cerr<<"add"<<endl;
        if (pos.empty() || pos.back().first != x)
            pos.push_back(make_pair(x, vector<int>(0)));
        if (pos.back().second.empty() || pos.back().second.back() != y)
            pos.back().second.push_back(y);
        //cerr<<"/add"<<endl;
    }
    ret_t solve(vector<pair<int, vector<int> > > & pos) {
        vector<pair<int, vector<int> > > pos2;
        int t = 0;
        while (!pos.empty()) {
            cerr<<"t = "<<t<<endl;
            for (int i = 0; i < pos.size(); ++i) {
                bool checkprev = true;
                if (i == 0)
                    checkprev = false;
                else if (pos[i-1].first != pos[i].first - 1)
                    checkprev = false;
                int prevj = 0;
                for (int j = 0; j < pos[i].second.size(); ++j) {
                    //cerr<<pos[i].first<<','<<pos[i].second[j]<<endl;//
                    // survives?
                    bool survives = false;
                    if (j > 0 && pos[i].second[j - 1] == pos[i].second[j] - 1)
                        survives = true;
                    else if (checkprev) {
                        //cerr<<"check prev for surv"<<endl;
                        while (prevj < pos[i-1].second.size()
                               && pos[i-1].second[prevj] < pos[i].second[j])
                            ++prevj;
                        if (prevj < pos[i-1].second.size()
                            && pos[i-1].second[prevj] == pos[i].second[j])
                            survives = true;
                    }
                    if (survives) {
                        add(pos2, pos[i].first, pos[i].second[j]);
                    }
                    // new one?
                    if (j + 1 < pos[i].second.size()
                        && pos[i].second[j+1] == pos[i].second[j] + 1) {
                        // already there
                    }
                    else if (checkprev) {
                        //cerr<<"check prev for new"<<endl;
                        while (prevj < pos[i-1].second.size()
                               && pos[i-1].second[prevj] < pos[i].second[j] + 1)
                            ++prevj;
                        if (prevj < pos[i-1].second.size()
                            && pos[i-1].second[prevj] == pos[i].second[j] + 1) {
                            add(pos2, pos[i].first, pos[i].second[j] + 1);
                        }
                    }
                }
            }
            pos.clear();
            swap(pos, pos2);
            ++t;
        }
        return t;
	}
};

int main(int argc, char ** argv) {
    string s;
    int N;
    getline(cin, s);
    {
        stringstream A(s);
        A >> N;
    }
    for (int no = 1; no <= N; ++no) {
        cerr << "Case " << no << " / " << N << endl;
        Solver solver;
        // *** get input ***
        getline(cin, s);
        int r;
        {
            stringstream A(s);
            A >> r;
        }
        vector<pair<int, int> > pos;
        vector<pair<int, vector<int> > >pos2;
        for (int i = 0; i < r; ++i) {
            getline(cin, s);
            stringstream A(s);
            int x1, y1, x2, y2;
            A >> x1 >> y1 >> x2 >> y2;
            for (int x = x1; x <= x2; ++x) {
                for (int y = y1; y <= y2; ++y) {
                    pos.push_back(make_pair(x, y));
                }
            }
        }
        sort(pos.begin(), pos.end());
        int curx = -1;
        int curi = -1;
        int cury = -1;
        for (int i = 0; i < pos.size(); ++i) {
            if (curx != pos[i].first) {
                curx = pos[i].first;
                curi = pos2.size();
                pos2.push_back(make_pair(curx, vector<int>(0)));
                cury = -1;
            }
            if (cury != pos[i].second) {
                cury = pos[i].second;
                pos2[curi].second.push_back(cury);
            }
        }
        ret_t ret = solver.solve(pos2);

        // *** give output ***
        cout << "Case #" << no << ": " << ret << endl; // one line
        //cout << "Case #" << no << ":\n" << ret; // multi-line
        //cout << "Case #" << no << ": " << fixed << setprecision(7) << ret << endl; // float
    }
    return 0;
}
