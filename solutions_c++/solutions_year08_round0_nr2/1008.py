#include <iostream>
#include <vector>

using namespace std;

const int N = 24 * 60;

vector<int> depA[N];
vector<int> depB[N];
int readyA[N];
int readyB[N];

int get(const string& s) {
    int hh = (s[0]-'0') * 10 + (s[1]-'0');
    int mm = (s[3]-'0') * 10 + (s[4]-'0');
    return hh * 60 + mm;
}

int main() {
    int cases; cin >> cases;
    for (int t = 1; t <= cases; t++) {
        for (int i = 0; i < N; i++) {
            depA[i].clear(); depB[i].clear();
            readyA[i] = readyB[i] = 0;
        }

        int ta; cin >> ta;
        int na, nb; cin >> na >> nb;

        for (int i = 0; i < na; i++) {
            string dep, arr; cin >> dep >> arr;
            int nDep = get(dep);
            int nArr = get(arr);
            depA[nDep].push_back(nArr);
        }

        for (int i = 0; i < nb; i++) {
            string dep, arr; cin >> dep >> arr;
            int nDep = get(dep);
            int nArr = get(arr);
            depB[nDep].push_back(nArr);
        }

        int aa = 0, bb = 0;
        int currA = 0, currB = 0;
        for (int time = 0; time < N; time++) {
            currA += readyA[time];
            currB += readyB[time];
            for (int i = 0; i < depA[time].size(); i++) {
                int readyTime = depA[time][i] + ta;
                if (readyTime < N) readyB[readyTime]++;
                currA--; if (currA < 0) { currA++; aa++; }
            }
            for (int i = 0; i < depB[time].size(); i++) {
                int readyTime = depB[time][i] + ta;
                if (readyTime < N) readyA[readyTime]++;
                currB--; if (currB < 0) { currB++; bb++; }
            }
        }
        cout << "Case #" << t << ": " << aa << " " << bb << endl;
    }
    return 0;
}

