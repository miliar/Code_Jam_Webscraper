#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <cstdio>

#define REP(i,n) for (int i = 0; i < (int)n; ++i)
#define FOR(i,c) for (__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)

using namespace std;

int main(void)
{
    int nCase;
    int N, M;

    cin >> nCase;
    for (int c = 1; c <= nCase; ++c) {
        cin >> N >> M;

        string s;
        map<string, int> used;
        REP(i, N) {
            cin >> s;

            int pos = 0;
            while ((pos = s.find_first_of('/', pos+1)) != string::npos) {
                string part = s.substr(0, pos);
                used[part] = 1;
            }
            
            used[s] = 1;
        }

        int cnt = 0;
        REP(i, M) {
            cin >> s;

            int pos = 0;
            while ((pos = s.find_first_of('/', pos+1)) != string::npos) {
                string part = s.substr(0, pos);

                if (used[part] != 1) {
                    used[part] = 1;
                    cnt++;
                }
            }

            if (used[s] != 1) {
                used[s] = 1;
                cnt++;
            }
        }

        cout << "Case #" << c << ": " << cnt << endl;
    }
    return 0;
}
