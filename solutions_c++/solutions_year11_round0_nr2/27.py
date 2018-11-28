
#include <iostream>
#include <vector>

using namespace std;

int C, D, N;
char change[26][26];
bool destroy[26][26];

string solve() {
    memset(change, 0, sizeof(change));
    cin >> C;
    for(int i = 0; i < C; i++) {
        string s;
        cin >> s;
        change[s[0]-'A'][s[1]-'A'] = s[2];
        change[s[1]-'A'][s[0]-'A'] = s[2];
    }

    memset(destroy, 0, sizeof(destroy));
    cin >> D;
    for(int i = 0; i < D; i++) {
        string s;
        cin >> s;
        destroy[s[0]-'A'][s[1]-'A'] = true;
        destroy[s[1]-'A'][s[0]-'A'] = true;
    }

    cin >> N;
    string s;
    cin >> s;
    vector <char> res;
    for(int i = 0; i < N; i++) {
        res.push_back(s[i]);

        int n = res.size();
        while(n > 1 && change[res[n-1]-'A'][res[n-2]-'A']) {
            char next = change[res[n-1]-'A'][res[n-2]-'A'];
            res.pop_back();
            res.pop_back();
            res.push_back(next);
            n = res.size();
        }
        for(int i = 0; i < n-1; i++) {
            if(destroy[res[i]-'A'][res[n-1]-'A']) {
                res.clear();
                break;
            }
        }
    }

    string r = "[";
    for(int i = 0; i < res.size(); i++) {
        r += res[i];
        if(i + 1 < res.size())
            r += ", ";
    }
    return r + "]";
}

int main() {
    int T;
    cin >> T;
    for(int i = 0; i < T; i++)
        cout << "Case #" << i+1 << ": " << solve() << endl;

    return 0;
}
