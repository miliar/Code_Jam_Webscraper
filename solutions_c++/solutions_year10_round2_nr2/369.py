#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

const int MAXN = (1 << 20);

class Duck {
public:
    int x;
    int v;
    int fly;

    Duck() : x(0), v(0), fly(0) {
    }

    bool operator<(const Duck& duck) const {
        if(this->fly != duck.fly) {
            return this->fly < duck.fly;
        }
        else {
            return this->x > duck.x;
        }
    }
};

Duck ducks[64];

int T;
int n, k, b, t;

int main() {
    cin >> T;
    for(int ca = 1; ca <= T; ca++) {
        
        cin >> n >> k >> b >> t;
        for(int i = 0; i < n; i++) {
            cin >> ducks[i].x;
        }
        for(int i = 0; i < n; i++) {
            cin >> ducks[i].v;
            ducks[i].fly = 0;
        }
        
        for(int i = n-1; i >= 0; i--) {
            if(ducks[i].x + ducks[i].v * t < b) {
                ducks[i].fly = MAXN;
                continue;
            }

            int fly = 0;
            for(int j = i + 1; j < n; j++) {
                if(ducks[j].fly == MAXN) {
                    fly++;
                    continue;
                }

                fly += ducks[j].fly;
                break;
            }
            ducks[i].fly = fly;
        }

        sort(ducks, ducks+n);

        int ans = 0;
        for(int i = 0; i < k; i++) {
            if(ducks[i].fly == MAXN) {
                ans = -1;
                break;
            }
            ans += ducks[i].fly;
        }

        if(ans >= 0) {
            cout << "Case #" << ca << ": " << ans << endl;
        }
        else {
            cout << "Case #" << ca << ": IMPOSSIBLE" << endl;
        }
    }
    return 0;
}
