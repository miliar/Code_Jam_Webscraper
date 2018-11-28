#include <iostream>
#include <vector>
#include <iterator>
#include <set>
#include <algorithm>
#include <map>

using namespace std;

int main(void)
{
    int cases = 0;
    cin >> cases;
    for (int c = 0; c < cases; ++c) {
        int p = 0;
        cin >> p;
        vector<int> can_miss(1 << p);
        vector<int> needed_matches(1 << p);        
        set<int> ok_teams;
        for (int t = 0; t < (1 << p); ++t) {
            cin >> can_miss[t];
            needed_matches[t] = p - can_miss[t];
            if (can_miss[t] >= p)
                ok_teams.insert(t);
        }
        int foo;
        for (int line = 1; line <= p; ++line) {
            for (int f = 0; f < 1 << (p - line); ++f)
                cin >> foo; // will be 1
        }
        // small input: go for the final, etc.
        vector<vector<int> > team_plays(1 << p);
        vector<vector<int> > match_has((1 << p) - 1);
        
        int i = 0;
        map<pair<int, int>, int> match_ids;
        for (int round = 1; round <= p; ++round) {
            int matches = (1 << (p - round));
            for (int match = 0; match < matches; ++match, ++i) {
                int size = (1 << p) / matches; 
                int start = match * size;
                //cerr << "in match " << i << " we got ";
                for (int plays = start ; plays < start + size; ++plays) {
                    //cerr << plays << " ";
                    team_plays[plays].push_back(i);
                    match_has[i].push_back(plays);
                }
                match_ids[make_pair(round, match)] = i;
            }
        }
        set<int> bought;
        for (int round = p; round >= 1; --round) {
            int matches = (1 << (p - round));

            for (int match = 0; match < matches; ++match, ++i) {
                i = match_ids[make_pair(round, match)];
                //cerr << "round " << round << " match" << match << endl;
                // do we need to take this match
                bool needed = false;
                for (int t = 0; t < match_has[i].size(); ++t) {
                    if (ok_teams.find(match_has[i][t]) == ok_teams.end()) {
                        //cerr << "taking cause of team" << match_has[i][t] << endl;
                        needed = true;
                        bought.insert(i);
                        break;
                    }
                }
                if (needed) {
                    for (int t = 0; t < match_has[i].size(); ++t) {
                        //cerr << "increasing mathes for" << match_has[i][t];
                        needed_matches[match_has[i][t]]--;
                        if (needed_matches[match_has[i][t]] <= 0) {
                            ok_teams.insert(match_has[i][t]);
                        }
                        //cerr << ", needs " << needed_matches[match_has[i][t]] << endl;
                    }
                }
                if (ok_teams.size() == (1 << p)) break;
            }
            if (ok_teams.size() == (1 << p)) break;
        }
        cout << "Case #" << (c + 1) << ": " << bought.size() << endl;
    }
    return 0;
}
