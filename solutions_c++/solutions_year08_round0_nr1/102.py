#include <iostream>
#include <string>
#include <map>
using namespace std;
map<string, int> mp;
bool color[101];
int mark;
void Process(const int &cas)
{
    int n, m;
    int cnt, code;
    string name;
    cin >> n;
    cin.ignore(10, '\n');
    mp.clear();
    for (int i = 0; i < n; i++) {
        getline(cin, name);
        mp[name] = i;
    }
    cin >> m;
    cin.ignore(10, '\n');
    cnt = 0;
    memset(color, false, sizeof(color));
    mark = n;
    while (m--) {
        getline(cin, name);
        code = mp[name];
        if (!color[code]) {
            color[code] = true;
            if ((--mark) == 0) {
                cnt++;
                memset(color, false, sizeof(color));
                color[code] = true;
                mark = n-1;
            }
        }
    }
    cout << "Case #" << cas << ": " << cnt << endl;
}
int main()
{
    int cas;
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    cin >> cas;
    for (int t = 1; t <= cas; t++)
        Process(t);
    return 0;
}
