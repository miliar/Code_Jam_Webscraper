#include <math.h>
#include <stdlib.h>
#include <iostream>

using namespace std;

struct person {
    int loc, time;
}p[2];

struct node {
    int k, loc;
}task[105];

string ch;
int T, n, last;

int main() {

    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    cin >> T;
    for (int ca = 1; ca <= T; ca++) {
        cin >> n;
        for (int i = 1; i <= n; i++) {
            cin >> ch;
            if (ch == "B") task[i].k = 0;
            else task[i].k = 1;
            cin >> task[i].loc;
        }
        for (int i = 0; i <= 1; i++) {
            p[i].loc = 1;
            p[i].time = 0;
        }
        last = 0;
        for (int i = 1; i <= n; i++) {
            int k = task[i].k;
            int loc = task[i].loc;
            int d = abs(p[k].loc - loc);
            last = max(last, p[k].time + d);
            p[k].loc = loc;
            last += 1;
            p[k].time = last;
        }
        cout << "Case #" << ca << ": " << last << endl;
    }

    return 0;
}
