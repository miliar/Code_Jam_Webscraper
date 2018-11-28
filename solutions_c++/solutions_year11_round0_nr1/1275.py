
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <queue>

using namespace std;

enum Bot {
    ORANGE,
    BLUE
} lastActed = ORANGE;

int pos[2] = { 1, 1 };
int actionsSinceLastChange = 0;
unsigned int actionCount = 0;

void init() {
    pos[0] = pos[1] = 1;
    actionCount = actionsSinceLastChange = 0;
}

// actions needed to reach a button
unsigned int getActionsNeeded(enum Bot bot, int target) {
    return abs(pos[bot] - target);
}

void readTarget() {
    char botCode;
    int target;
    cin >> botCode >> target;

    enum Bot bot = (botCode == 'O') ? ORANGE : BLUE;
    if (bot == lastActed) {
        int actionsNeeded = getActionsNeeded(bot, target) + 1; // +1 = button press
        actionsSinceLastChange += actionsNeeded;
        actionCount += actionsNeeded;
    } else {
        int actionsNeeded = getActionsNeeded(bot, target);
        if (actionsSinceLastChange < actionsNeeded) {
            actionsSinceLastChange = actionsNeeded - actionsSinceLastChange + 1;
        } else {
            actionsSinceLastChange = 1;
        }
        actionCount += actionsSinceLastChange;
        lastActed = bot;
    }
    pos[bot] = target;
}

void readTargets() {
    unsigned int n;
    cin >> n;
    for (unsigned int i = 0; i < n; ++i) {
        readTarget();
    }
}

int doTestcase() {
    init();
    readTargets();
    return actionCount;
}

int main(int argc, char *argv[]) {
    unsigned int t;
    cin >> t;
    for (unsigned int i = 0; i < t; ++i) {
        cout << "Case #" << i + 1 << ": " << doTestcase() << endl;
    }
    return 0;
}

