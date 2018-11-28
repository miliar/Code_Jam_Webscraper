#include <iostream>
#include <string>
#include <set>

using namespace std;

string engine[101];
string query;

int main () {
    int i, j, N, cse=0;
    cin >> N;
    while (N--) {
        int cnt = 0;
        int S, Q;
        cin >> S;
        getline(cin, query);
        for (i=0; i<S; i++) getline(cin, engine[i]);
        cin >> Q;
        getline(cin, query);
        set<string> se;
        for (i=0; i<S; i++) se.insert(engine[i]);
        int cur = 0;
        while (cur < Q) {
            while (se.size() > 0 && cur < Q) {
                getline(cin, query);
                se.erase(query);
                cur++;
            }
            if (se.size() == 0) {
                cnt++;
                for (i=0; i<S; i++) {
                    if (query != engine[i]) se.insert(engine[i]);
                }
            }
        }
        cout << "Case #" << ++cse << ": " << cnt << endl;
    }
    return 0;
}
