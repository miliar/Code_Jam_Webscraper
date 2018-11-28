#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <queue>

using namespace std;


int main(void) {
    int nC;
    scanf("%d", &nC);
    for (int cC = 0; cC < nC; ++cC) {
        priority_queue<int> queues[3];  // cards with 0 draws, 1 draw or 2 draws
        int score = 0, turns = 1;
        int drawn = 0;
        int nCards;
        scanf("%d", &nCards);
        for (int i = 0; i < nCards; ++i) {
            int c, s, t;
            scanf("%d %d %d", &c, &s, &t);
            if (t) {
                turns += t - 1;
                score += s;
                drawn += c;
            } else {
                if (c || s)
                    queues[c].push(s);
            }
        }

        int deck[80][3];
        int dS = 0;
        scanf("%d", &nCards);
        for (int i = 0; i < nCards; ++i) {
            // process as if in hand until drawn == 0
            int c, s, t;
            scanf("%d %d %d", &c, &s, &t);
            if (drawn) {
                --drawn;
                if (t) {
                    turns += t - 1;
                    score += s;
                    drawn += c;
                } else {
                    if (c || s)
                        queues[c].push(s);
                }
            } else {
                deck[dS][0] = c;
                deck[dS][1] = s;
                deck[dS][2] = t;
                ++dS;
            }
        }

        int dPtr = 0;
        int bestScore = score;
        while (true) {
            if (!turns) break;
            if (queues[0].empty() && queues[1].empty() && queues[2].empty())
                break;
            
            vector<int> temp;
            int currS = score;
            for (int i = 0; i < turns; ++i) {
                if (!queues[0].empty()) {
                    int sc = queues[0].top();
                    currS += sc;
                    temp.push_back(sc);
                    queues[0].pop();
                } else break;
            }
            for (vector<int>::iterator it = temp.begin(); it != temp.end();
                 ++it)
                 queues[0].push(*it);
            if (currS > bestScore) bestScore = currS;
            if (queues[1].empty()) break;
            
            // now, try to play card at queues[1].
            --turns;
            score += queues[1].top();
            queues[1].pop();
            if (!turns) break;
            while (dPtr < dS) {
                if (deck[dPtr][2]) {
                    turns += deck[dPtr][2] - 1;
                    score += deck[dPtr][1];
                    if (!deck[dPtr][0]) {
                        ++dPtr;
                        break;
                    } else ++dPtr;
                } else {
                    if (deck[dPtr][0] || deck[dPtr][1])
                        queues[deck[dPtr][0]].push(deck[dPtr][1]);
                    dPtr++;
                    break;
                }
            }
        }
        if (score > bestScore) bestScore = score;
        printf("Case #%d: %d\n", cC + 1, bestScore);
    }
    return 0;
}
