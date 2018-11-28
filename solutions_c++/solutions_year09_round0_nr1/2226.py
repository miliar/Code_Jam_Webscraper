#include <string>
#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
#include <cstdlib>

using namespace std;

typedef vector<string> VS;
typedef vector<int> VI;



int contar(const int L, const string &line, const VS &words) {
    int cant = 0;
    size_t i = 0;
    VS vv;
    VI vi(line.size(), 0);

    while (i < line.size()) {
        while (i < line.size() && line[i] != '(') {
            vv.push_back(line.substr(i, 1));
            ++i;
        }

        ++i;

        size_t start = i;
        while (i < line.size() && line[i] != ')')
            ++i;

        if (i - start > 0) {
            vv.push_back(line.substr(start, i - start));
        }

        ++i;
    }

/*
    for (i = 0; i < vv.size(); ++i)
        cout << "[" << vv[i] << "]" << endl;
*/

    for (VS::const_iterator it = words.begin(); it != words.end(); ++it) {
        const string &w1 = *it;

        for (i = 0; i < w1.size(); ++i) {
            string &w2 = vv[i];
            bool f2 = false;

            for (size_t j = 0; j < w2.size(); ++j) {
                if (w1[i] == w2[j]) {
                    f2 = true;
                    break;
                }
            }

            if (!f2)
                break;
        }

        if (i == w1.size())
            ++cant;
    }

    return cant;
}

int main(int argc, char** argv) {
    int L, D, N;
    VS words;

    cin >> L;
    cin >> D;
    cin >> N;

    for (int i = 0; i < D; ++i) {
        string tmp;
        cin >> tmp;
        words.push_back(tmp);
    }

    for (int i = 0; i < N; ++i) {
        string tmp;
        cin >> tmp;
        cout << "Case #" << (i + 1) << ": " << contar(L, tmp, words) << endl;
    }
}
