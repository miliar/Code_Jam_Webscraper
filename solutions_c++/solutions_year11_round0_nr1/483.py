#include <cstdio>
#include <vector>
#include <deque>
using namespace std;

int abs(int x) {
    return x < 0 ? -x : x;
}

int solve() {
    int b = 1, o = 1, steps = 0;

    int n;
    char r[105] = {};
    int p[105] = {};
    deque<int> blue, orange;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf(" %c %d", &r[i], &p[i]);
        if (r[i] == 'O')
            orange.push_back(p[i]);
        else
            blue.push_back(p[i]);
    }

    int i = 0;
    while (orange.size() && blue.size()) {
        bool bmoved = false, omoved = false;
        bool bpushed = false, opushed = false;
        if (orange.front() != o) {
            omoved = true;
            o += (orange.front() > o)? 1 : -1;
//            printf("Move Orange\n");
        }

        if (blue.front() != b) {
            bmoved = true;
            b += (blue.front() > b)? 1 : -1;
//            printf("Move Blue\n");
        }

        if (r[i] == 'O') {
            if (!omoved) {
                // push orange button
                i++;
                orange.pop_front();
                opushed = true;
//                printf("Push Orange\n");
            }
        } else {
            if (!bmoved) {
                // push blue button
                i++;
                blue.pop_front();
                bpushed = true;
//                printf("Push Blue\n");
            }
        }

        if (bmoved || omoved || bpushed || opushed)
            steps++;
//        printf("---\n");
    }
    
    // move the remaining one to the button and push it
    deque<int> left = (orange.size() ? orange : blue);
    int pos = (orange.size() ? o : b);
    while (!left.empty()) {
        steps += abs(pos - left.front()) + 1;
        pos = left.front();
        left.pop_front();
    }

    return steps;
}

int main() {
    int T;
    scanf("%d\n", &T);
    for (int i = 0; i < T; i++) {
        printf("Case #%d: %d\n", i+1, solve());
    }
    return 0;
}
