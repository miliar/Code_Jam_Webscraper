#include <iostream>
#include <string>
#include <vector>
using namespace std;

char f[256][256];
bool g[256][256];
string st;

int main()
{
    freopen("b2.in", "r", stdin);
    freopen("b2.out", "w", stdout);
    
    int t1;
    cin >> t1;
    for (int t2 = 1; t2 <= t1; ++t2) {
        memset(f, 0, sizeof(f));
        memset(g, 0, sizeof(g));
        int x;
        cin >> x;
        while (x--) {
            cin >> st;
            f[st[0]][st[1]] = f[st[1]][st[0]] = st[2];
        }
        cin >> x;
        while (x--) {
            cin >> st;
            g[st[0]][st[1]] = g[st[1]][st[0]] = true;
        }
        cin >> x >> st;
        vector<char> ret;
        for (int i = 0; i < st.size(); ++i) {
            if (!ret.empty() && f[ret.back()][st[i]])
                ret.back() = f[ret.back()][st[i]];
            else
                ret.push_back(st[i]);
            for (int j = 0; j < ret.size(); ++j)
                if (g[ret.back()][ret[j]]) ret.clear();
        }
        cout << "Case #" << t2 << ": [";
        if (ret.size()) {
            cout << ret[0];
            for (int i = 1; i < ret.size(); ++i)
                cout << ", " << ret[i];
        }
        cout << "]" << endl;
    }
    
    return 0;
}
