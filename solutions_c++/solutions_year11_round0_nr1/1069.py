#include <iostream>
#include <string>
#include <list>

using namespace std;

void solve(int i) {
    int ans = 0;

    int steps = 0;
    cin >> steps;

    int loc = 0;
    string p;
    list<int> vO, vB;
    list<bool> isO;
    while(steps--) {
        cin >> p >> loc;
        if(p=="O") {
            isO.push_back(true);
            vO.push_back(loc);
        } else {
            isO.push_back(false);
            vB.push_back(loc);
        }
    }

    int locO = 1, locB = 1;
    for(int T=1;;T++) {
        bool isOnow = *isO.begin();
        int Otarget = *vO.begin();
        int Btarget = *vB.begin();
        if(locO == Otarget) {
            if(isOnow) {
                vO.pop_front();
                isO.pop_front();
            }
        } else {
            if(locO < Otarget)	locO++;
            else				locO--;
        }
        if(locB == Btarget) {
            if(!isOnow) {
                vB.pop_front();
                isO.pop_front();
            }
        } else {
            if(locB < Btarget)	locB++;
            else				locB--;
        }
        if(isO.size()==0) {
            ans = T;
            break;
        }
    }
    cout << "Case #" << i << ": " << ans << endl;
}

int main(int argc, void **argv) {
    int N;
    cin >> N;
    for(int i=0;i<N;i++) {
        solve(i+1);
    }
}

