#include <iostream>
#include <queue>
using namespace std;

const int BUFSIZE = 1024;
int main() {
    queue<int> o,b;
    queue<bool> order;
    int num;
    cin >> num;
    for(int i=0;i<num;++i) {
        int numMoves;
        cin >> numMoves;
        for(int j=0;j<numMoves;++j) {
            char which;
            int button;
            cin >> which;
            cin >> button;
            if(which=='O') {
                o.push(button);
                order.push(true);
            } else {
                b.push(button);
                order.push(false);
            }
        }
        int totalMoves = 0;
        int oPos=1,bPos=1;
        while(!(o.empty() && b.empty())) {
            ++totalMoves;
            bool pushedButton = false;
            if(!o.empty()) {
                if(o.front() > oPos)
                    ++oPos;
                else if(o.front() < oPos)
                    --oPos;
                else if(order.front()) {
                    o.pop();
                    pushedButton = true;
                }
            }
            if(!b.empty()) {
                if(b.front() > bPos)
                    ++bPos;
                else if(b.front() < bPos)
                    --bPos;
                else if(!order.front()) {
                    b.pop();
                    pushedButton = true;
                }
            }
            if(pushedButton)
                order.pop();
        }
        cout << "Case #" << i+1 << ": " << totalMoves << endl;
    }
    return 0;
}
