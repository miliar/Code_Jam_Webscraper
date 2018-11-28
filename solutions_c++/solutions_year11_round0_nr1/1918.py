#include <iostream>
#include <cstdio>
#include <queue>
using namespace std;

int t, n;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> t;
    for (int tc = 1; tc <= t; tc++) {
          queue <int> but[2], who;
          cin >> n;
          while (n--) {
                char r;
                int p;
                cin >> r >> p;
                if (r == 'O') {
                      who.push(0);
                      but[0].push(p);
                } else {
                       who.push(1);
                       but[1].push(p);
                }
          }
          int pos[2];
          pos[0] = pos[1] = 1;
          int tim = 0;
          while (!who.empty()) {
                tim++;
                bool pushed = false;
                for (int i = 0; i < 2; i++) if (!but[i].empty())
                   if (pos[i] < but[i].front()) pos[i]++;
                   else if (pos[i] > but[i].front()) pos[i]--;
                   else if (pos[i] == but[i].front() && who.front() == i && !pushed) {
                        pushed = true;
                        but[i].pop(); who.pop();
                   }
          }
          cout << "Case #" << tc << ": " << tim << endl;
    }
    return 0;
}
