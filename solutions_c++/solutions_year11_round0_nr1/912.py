#include <iostream>
#include <deque>
using namespace std;

class Move {
    public:
    char robot;
    int button;
};


int main()
{
    int t;
    cin >> t;
    for (int q=1; q<=t; q++) {
        int n;
        cin >> n;
        deque <Move> moves,blueMoves,orangeMoves;
        Move one_move;
        for (int i=0; i<n; i++) {
            cin >> one_move.robot >> one_move.button;
            moves.push_back(one_move);
            if (one_move.robot=='B') {
                blueMoves.push_back(one_move);
            }
            else {
                orangeMoves.push_back(one_move);
            }
        }
        int ans=0,blueButton=1,orangeButton=1;

        while (!moves.empty()) {
            ans++;
            int blueMoved=0,orangeMoved=0;
            if (blueButton==moves.front().button && moves.front().robot=='B') {
                moves.pop_front();
                blueMoves.pop_front();
                blueMoved++;
            }
            else {
                if (orangeButton==moves.front().button && moves.front().robot=='O') {
                    moves.pop_front();
                    orangeMoves.pop_front();
                    orangeMoved++;
                }
            }

            if (!blueMoved) {
                if (blueMoves.front().button>blueButton) blueButton++;
                if (blueMoves.front().button<blueButton) blueButton--;
            }
            if (!orangeMoved) {
                if (orangeMoves.front().button>orangeButton) orangeButton++;
                if (orangeMoves.front().button<orangeButton) orangeButton--;
            }
        }
        cout << "Case #" << q << ": " << ans << endl;
    }
    return 0;
}
