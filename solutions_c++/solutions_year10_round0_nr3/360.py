#include <cstdlib>
#include <cstdio>
#include <iostream>
using namespace std;

int m, n, r, k, g[1001];
int lastTime[1001], pos;
long long lastMoney[1001], money;
int doubleg[2002];

int putIn() {
    int sitIn = 0;
    for (int i=pos; i<pos+n;  ++i) {
        if (sitIn + doubleg[i] <= k) {
            sitIn += doubleg[i];
            money += doubleg[i];
        }
        else
            return (i>=n)?(i-n):i;
    }
    return pos;
}

int main(void)
{
    cin >> m;
    for (int test=0; test<m; ++test) {
        cin >> r >> k >> n;
        for (int i=0; i<n; ++i) {
            cin >> g[i];
            doubleg[i] = g[i];
            doubleg[i+n] = g[i];
        }
        for (int i=0; i<n;  ++i)
            lastTime[i] = -1;
        lastTime[0] = 0;
        lastMoney[0] = 0;
        pos = 0;
        money = 0;
        int times = 0;
        while (r > 0) {
            int newPos = putIn();
            //cout << newPos << ' ' << money << endl;
            --r;
            ++times;
            pos = newPos;
            if (lastTime[newPos] != -1) {
                int repeatTime = r / (times - lastTime[newPos]);
                long long madeMoney = money - lastMoney[newPos];
                money += madeMoney * repeatTime;
                r = r % (times - lastTime[newPos]);
            }
            else {
                lastTime[newPos] = times;
                lastMoney[newPos] = money;
            }
        }
        cout << "Case #" << test + 1 << ": " << money << endl;
    }
    return 0;
}
