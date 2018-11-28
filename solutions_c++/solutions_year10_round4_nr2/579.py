#include <iostream>
#include <vector>

using namespace std;

int rounds;
vector<int> canMiss;
vector<vector<int> > tick;

int INF = 1<<29;
int cache[11][1100][11];

int go(int rr, int rpos, int missed) {
    if (rr < 0) return (canMiss[rpos] >= missed) ? 0 : INF;
    
    int &ans = cache[rr][rpos][missed];
    if (ans >= 0) return ans;

    int ticketPrice = tick[rounds-rr-1][rpos];
    //cout << "ticketPrice="<<ticketPrice<<endl;
    //if (ticketPrice != 1) cout << "BAD!"<<endl;

    ans = INF;
    ans <?= ticketPrice + go(rr-1, 2*rpos, missed) + go(rr-1, 2*rpos+1, missed);
    ans <?= go(rr-1, 2*rpos, missed+1) + go(rr-1, 2*rpos+1, missed+1);
    //cout << "GO " << rr <<","<<rpos<<","<<missed<< " = " << ans<<endl;
    return ans;
}

int main() {
    int cases;
    cin >> cases;

    for(int c=0; c<cases; c++) {
        cin >> rounds;
        tick.resize(rounds);
        canMiss.resize(1<<rounds);
        memset(cache,-1,sizeof(cache));

        for(int i=0; i<canMiss.size(); i++) cin >> canMiss[i];
        //cout << "CASE " << (c+1) << " rounds="<<rounds<<endl;

        for(int r=rounds-1; r >= 0; r--) {
            vector<int> tt;
            for(int i=0; i<(1<<r); i++) { int price; cin >> price; tt.push_back(price); }
            tick[r] = tt;
        }

        cout << "Case #" <<(c+1) << ": " << go(rounds-1, 0, 0) << endl;
    }
}
