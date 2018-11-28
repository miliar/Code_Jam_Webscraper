#include <stdio.h>
#include <string>
#include <set>
#include <iostream>

using namespace std;

int T, t;
int sol;
int N, M;
int i, j, cnt;
string s, sub;
set <string> dirs;
set <string>::iterator iter;

int main() {

    cin >> T;

    for (t = 1; t <= T; t++) {

        dirs.clear();
        sol = 0;

        cin >> N >> M;

        for (i = 0; i < N; i++) {
            cin >> s;
            for (j = 1; j < s.size(); j++) {
                if (s[j] == '/') {
                    //cout << "found " << s.substr(0, j) << endl;
                    dirs.insert(s.substr(0, j));
                }
            }
            //cout << "found " << s << endl;
            dirs.insert(s);

        }
/*
        iter = dirs.begin();
        while (iter != dirs.end()) {
            cout << *iter << endl;
            iter++;
        }
*/
        for (i = 0; i < M; i++) {
            cin >> s;
            //cout << "check " << s << endl;
            iter = dirs.find(s);
            if (iter != dirs.end()) {
                //cout << "found\n";
                continue;
            }
            dirs.insert(s);

            cnt = 0;
            for (j = s.size() - 1; j >= 0; j--) {
                if (s[j] == '/') {
                    sub = s.substr(0, j);
                    //cout << "check " << sub << endl;
                    iter = dirs.find(sub);
                    cnt++;
                    //cout << "cnt = " << cnt << endl;
                    if (iter != dirs.end()) {
                        //cout << "found\n";
                        break;
                    }
                    dirs.insert(sub);
                }
            }
            sol += cnt;
            //cout << "sol = " << sol << endl;
        }

        cout << "Case #" << t << ": " << sol << "\n";
    }

    return 0;
}