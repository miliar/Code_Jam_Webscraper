#include <iostream>
#include <string>
#include <vector>
#include <set>

using namespace std;

int L, D, N;
vector<string> dic;
vector<string> lets;

void split(const string &pattern) {
}

int main() {
    cin >> L >> D >> N;
    dic.resize(D);
    set<int> temp;
    for (int i = 0; i < D; i++) {
        cin >> dic[i];
        temp.insert(i);
    }
    for (int i = 1; i <= N; i++) {
        set<int> matchs(temp);
        for (int j = 0; j < L; j++) {
            char ch; cin >> ch;
            string list;
            if (ch != '(') {
                list += ch;
            } else {
                while (cin >> ch, ch != ')')
                    list += ch;
            }
            set<int>::iterator it = matchs.begin();
            while (it != matchs.end()) {
                if (list.find(dic[*it][j]) == -1)
                    matchs.erase(it++);
                else
                    it++;
            }
        }
        cout << "Case #" << i << ": " << matchs.size() << '\n';
    }
    return 0;
}
