#include <fstream>
#include <queue>
using namespace std;

int t, r, k, n;
long long ans;
queue<int> g, in;

int main()
{
    ifstream fin("task.in");
    ofstream fout("task.out");
    int num, tak, i, j, l;
    fin >> t;
    for (i = 1; i <= t; i++) {
        fin >> r >> k >> n;
        ans = 0;
        for (j = 0; j < n; j++) {
            fin >> num;
            g.push(num);
        }
        for (j = 0; j < r; j++) {
            tak = 0;
            while (!g.empty() && tak + g.front() <= k) {
                  tak += g.front();
                  in.push(g.front()); g.pop();
            }
            ans += tak;
            while (!in.empty()) {
                  g.push(in.front()); in.pop();
            }
        }
        while (!g.empty()) g.pop();
        fout << "Case #" << i << ": " << ans << endl;
    }
    fin.close();
    fout.close();
    return 0;
}
