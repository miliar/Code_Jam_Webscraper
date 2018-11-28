#include <iostream>
#include <vector>
#include <map>

using namespace std;

int n, T = 0;
vector<string> engines;
map<string, int> table;

int main() {
    cin >> n;
    while(n--) {
        engines.clear();
        table.clear();
        int ans = 0;

        int s, q;
        cin >> s;
        cin.ignore();
        for(int i = 0; i < s; i++) {
            string engine;
            getline(cin, engine);
            table[engine] = 0;
            engines.push_back(engine);
        }

        cin >> q;
        cin.ignore();
        int last = s;
        for(int i = 0; i < q; i++) {
            string query;
            getline(cin, query);
            if(table[query] == 0)
                last--;
            if(last == 0) {
                for(int j = 0; j < engines.size(); j++)
                    table[engines[j]] = 0;
                ans++;
                last = s-1;
            }
            table[query]++;
        }

        cout << "Case #" << ++T << ": " << ans << endl;
    }
    return 0;
}
