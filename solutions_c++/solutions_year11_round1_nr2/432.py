#include <iostream>
#include <string>
#include <vector>
using namespace std;
const int maxn = 10000 + 10, maxm = 100 + 10;
const int debug = 0;

string dict[maxn];
string list[maxm];
int n, m;

bool suitable(string w, string s)
{
    for (int i = 0; i < s.size(); i++)
        if (s[i] != ' ' && s[i] != w[i] || s[i] == ' ' && s.find(w[i]) < s.npos)
            return false;
    return true;
}

int tryit(string target, string alph)
{
    vector<string> dicts;
    string s = target;
    for (int i = 0; i < n; i++)
        if (dict[i].size() == target.size())
            dicts.push_back(dict[i]);
    for (int i = 0; i < s.size(); i++)
        s[i] = ' ';

    int cnt = 0;
    for (int i = 0; i < 26; i++) {
        bool tryit = false;
        for (int j = 0; j < dicts.size(); j++)
            if (dicts[j].find(alph[i]) < dicts[j].npos) {
                tryit = true;
                break;
            }

        if (tryit) {
            if (target.find(alph[i]) < target.npos) {
                int st = 0, k;
                while ((k = target.find(alph[i], st)) < target.npos) {
                    s[k] = alph[i];
                    st = k + 1;
                }

                for (vector<string>::iterator word = dicts.begin(); word != dicts.end();)
                    if (!suitable(*word, s))
                        word = dicts.erase(word);
                    else
                        ++word;
            } else {
                ++cnt;
                for (vector<string>::iterator word = dicts.begin(); word != dicts.end();)
                    if ((*word).find(alph[i]) < (*word).npos)
                        word = dicts.erase(word);
                    else
                        ++word;
            }
        }
    }
    return cnt;
}

int main(void)
{
    int T;
    cin >> T;

    for (int loop = 1; loop <= T; loop++) {
        cin >> n >> m;
        for (int i = 0; i < n; i++)
            cin >> dict[i];
        for (int i = 0; i < m; i++)
            cin >> list[i];

        cout << "Case #" << loop << ':';
        for (int perlist = 0; perlist < m; perlist++) {
            int answ, guess;
            if (debug)
                cout << endl << list[perlist];
            for (int word = 0; word < n; word++) {
                int t = tryit(dict[word], list[perlist]);
                if (debug)
                    cout << endl << dict[word] << ' ' << t;
                if (!word || guess < t) {
                    answ = word;
                    guess = t;
                }
            }
            if (!debug)
                cout << ' ' << dict[answ];
        }
        cout << endl;
    }
    return 0;
}
