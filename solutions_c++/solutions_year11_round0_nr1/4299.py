#include <iostream>
#include <vector>
#include <iterator>
#include <algorithm>
using namespace std;

#define ORANGE 0
#define BLUE   1
#define INVALID -1

struct state
{
    int color;
    int pos;
};

vector<state> sequence;

int getNextState(int color, int seqIndex)
{
    for (int i = seqIndex; i < sequence.size(); i++) {
        if (sequence[i].color == color) return sequence[i].pos;
    }
    return INVALID;
}

int solve()
{
    int seconds = 0;
    int seqIndex = 0;
    // 0 is orange and 1 is blue
    int rstates[2];
    int nextState[2];
    // init
    rstates[0] = rstates[1] = 1;
    nextState[ORANGE] = getNextState(ORANGE, seqIndex);
    nextState[BLUE]   = getNextState(BLUE, seqIndex);
    
    while (seqIndex < sequence.size()) {
        int seqColor = sequence[seqIndex].color;

        int colorPressed = -1;
        // check reach
        if (sequence[seqIndex].pos == rstates[seqColor]) {
            ++seqIndex;
            colorPressed = seqColor;
            nextState[seqColor] = getNextState(seqColor, seqIndex);
        }
        // move each
        for (int i = 0; i < 2; i++) {
            if (colorPressed == i || nextState[i] == INVALID) continue;
            if (nextState[i] < rstates[i])
                rstates[i]--;
            else if (nextState[i] > rstates[i])
                rstates[i]++;
        }
        ++seconds;
    }
    return seconds;
}

int main(int argc, char **argv)
{
    int T, N, button;
    char color;
    state s;
    cin >> T;
    for (int i = 0; i < T; i++) {
        cin >> N;
        sequence.resize(0);
        for (int j = 0; j < N; j++) {
            cin >> color;
            if (color == 'O') s.color = ORANGE;
            else s.color = BLUE;
            cin >> s.pos;
            sequence.push_back(s);
        }
        
        int res = solve();
        cout << "Case #" << i+1 << ": " << res << endl;
    }
    return 0;
}
