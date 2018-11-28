#include <cstdio>
#include <vector>
#include <algorithm>
#include <string>
#include <cstring>
#include <map>
#include <set>
#include <iostream>
#include <cassert>

using namespace std;

struct state {
    int cur_letter;
    string pattern;

    state() { }
    state(int cur_letter, string pattern) : cur_letter(cur_letter), pattern(pattern) { }

    bool operator<(const state& s) const {
        if(cur_letter != s.cur_letter) return cur_letter < s.cur_letter;
        return pattern < s.pattern;
    }
};

map<state, set<state> > sons;
map<state, int> masks;
map<state, set<int> > buckets;
vector<string> words;

map<state, pair<int, int> > memo;
pair<int, int> doit(state s) {
    if(s.cur_letter == 26) return make_pair(0, *buckets[s].begin());

    map<state, pair<int, int> >::iterator it = memo.find(s);
    if(it != memo.end()) return it->second;

    if(!(masks[s] & (1<<s.cur_letter)))
        return memo[s] = doit(state(s.cur_letter + 1, s.pattern));

    pair<int, int> ret(999999999, 999999999);
    assert(sons.find(s) != sons.end());

    for(set<state>::iterator it2 = sons[s].begin(); it2 != sons[s].end(); it2++) {
        int wrong = !(masks[*it2] & (1<<s.cur_letter));
        pair<int, int> rec = doit(*it2);
        assert(rec.first != 999999999);
        rec.first -= wrong;
        ret = min(ret, rec);
    }

    return memo[s] = ret;
}

int main() {
    int T;
    scanf("%d", &T);

    for(int z = 1; z <= T; z++) {
        printf("Case #%d:", z);

        char c[15];
        int n, m;
        scanf("%d %d", &n, &m);

        words.clear();
        for(int i = 0; i < n; i++) {
            scanf("%s", c);
            words.push_back(string(c));
        }

        for(int i = 0; i < m; i++) {
            char list[30];
            scanf("%s", list);

            int ord[255];
            for(int j = 0; j < 26; j++)
                ord[(int)list[j]] = j+1;

            memo.clear();
            sons.clear();
            masks.clear();
            buckets.clear();

            for(unsigned int i = 0; i < words.size(); i++) {
                vector<pair<int, int> > s;

                int mask = 0;
                for(unsigned int j = 0; j < words[i].size(); j++) {
                    s.push_back(make_pair(ord[(int)words[i][j]], j));
                    mask |= 1<<(ord[(int)words[i][j]]-1);
                }
                sort(s.begin(), s.end());

                unsigned int ptr = 0;
                string cur = string(words[i].size(), 'X');

                for(int j = 0; j <= 26; j++) {
                    string oldcur = cur;
                    while(ptr < s.size() && s[ptr].first == j) {
                        cur[s[ptr].second] = words[i][s[ptr].second];
                        ptr++;
                    }

                    state newstate(j, cur);
                    if(j) sons[state(j-1, oldcur)].insert(newstate);
                    buckets[newstate].insert(i);
                    masks[newstate] |= mask;
                }
            }

            pair<int, int> ans(999999999, 999999999);
            for(int i = 1; i <= 10; i++) {
                if(buckets.find(state(0, string(i, 'X'))) == buckets.end()) continue;
                pair<int, int> cur = doit(state(0, string(i, 'X')));
                ans = min(ans, cur);
            }
            printf(" %s", words[ans.second].c_str());
        }

        printf("\n");
    }
}
