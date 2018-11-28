#include <iostream>
#include <sstream>
#include <cstring>
#include <vector>
#include <stack>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <ctime>
#include <cstdio>
#include <cstdlib>

using namespace std;

#define DPRINT printf
#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
#define MP(a,b) make_pair(a,b)


class Robot {
public:
    int pos;
    int opId;
    int nextButton;
    Robot *partner;
    queue<pair<int,int> > opList;
    bool finish;

    Robot() {
        pos = 1;
        finish = false;
    }
    void setPartner(Robot *p) {
        partner = p;
    }
    bool action() {
        if ((nextButton - pos) == 0) {
            return push();
        }
        else {
            move();
            return false;
        }
    }
    void move() {
        // move.
        nextButton - pos > 0 ? pos++ : pos--;
    }
    bool push() {
        // wait.
        if (!partner->finish && (partner->opId < opId)) {
            return false;
        }
        // get next operation.
        return true;
    }
    bool nextOp() {
        if (opList.empty()) {
            finish = true;
            return false;
        }
        pair<int,int> op = opList.front();
        opList.pop();
        opId = op.first;
        nextButton = op.second;
        return true;
    }
};


int main (void) {
    int T;
    cin >> T;
    REP(i, T) {
        // get operation list.
        queue<pair<int,int> > blueOp;
        queue<pair<int,int> > orangeOp;
        int N;
        cin >> N;
        REP(j, N) {
            char R; int P;
            cin >> R >> P;
            if (R == 'B') { blueOp.push(MP(j,P)); }
            else { orangeOp.push(MP(j,P)); }
        }

        // test.
        int pasttime = 0;
        Robot blue, orange;
        blue.setPartner(&orange);
        orange.setPartner(&blue);
        blue.opList = blueOp;
        orange.opList = orangeOp;

        blue.nextOp();
        orange.nextOp();


        while (true) {
            bool b = blue.action();
            bool o = orange.action();
            if (b) { blue.nextOp(); }
            if (o) { orange.nextOp(); }
            //cout << blue.pos << "," << orange.pos << ":" << blue.finish << "," << orange.finish<< endl;
            pasttime++;
            if (!(!blue.finish || !orange.finish)) { break; }
        }
        cout << "Case #" << (i + 1) << ": " << pasttime << endl;
    }
    return 0;
}


