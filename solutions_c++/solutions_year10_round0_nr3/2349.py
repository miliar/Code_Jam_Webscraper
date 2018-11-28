#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <cmath>

using namespace std;

#define ll long long

int main() {
    ifstream in("roller.in");
    ofstream out("roller.txt");
    int t;
    in >> t;
    for (int z=1; z<=t; z++) {
        ll R, k;
        ll N;
        ll ret = 0;
        in >> R >> k >> N;
        queue<ll> q, tq;
        for (ll n=0; n<N; n++) {
            ll tmp;
            in >> tmp;   
            q.push(tmp);
        }
        for (ll r=0; r<R; r++) {
            ll crnt=0;
            while (!q.empty()) {
                if (crnt + q.front() > k)
                    break;
                    
                crnt += q.front();
                tq.push(q.front());
                q.pop();
            }
            //out << "  added " << crnt << " euros" << endl;
            ret += crnt;
            while (!tq.empty()) {
                q.push(tq.front());
                tq.pop();   
            }
        }
        out << "Case #" << z << ": " << ret << endl;        
    }
}
