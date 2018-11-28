#include <iostream>
#include <cstdlib>

using namespace std;

struct button {
    int color;
    int pos;
};

struct robot {
    int pos;
    int steps_left;
    int order;
};

int N;
button B[100];
robot R[2];
int order;

void find_next_order(int r)
{
    for(int i = order; i < N; i++) {
        if(B[i].color == r) {
            R[r].order = i;
            R[r].steps_left = abs(B[i].pos-R[r].pos) + 1;
            return;
        }
    }
    R[r].order = 9999;
}

int other_robot(int r)
{
    if(r == 0) return 1;
    return 0;
}

int solve()
{
    int steps = 0;
    order = 0;
    for(int i = 0; i < 2; i++) {
        R[i].pos = 1;
        find_next_order(i);
    }
    while(order < N) {
        // Which robot to press the next button?
        int r1 = 0;
        if(R[1].order < R[0].order) r1 = 1;
        // Press button
        steps += R[r1].steps_left;
        R[r1].pos = B[order].pos;
        int r2 = other_robot(r1);
        R[r2].steps_left -= R[r1].steps_left;
        if(R[r2].steps_left < 1) R[r2].steps_left = 1;
        // Fetch next "order"
        order++;
        find_next_order(r1);
    }
    return steps;
}

void read_input()
{
    cin >> N;
    for(int j = 0; j < N; j++) {
        char c;
        cin >> c;
        if(c == 'O') {
            B[j].color = 0;
        } else {
            B[j].color = 1;
        }
        cin >> B[j].pos;
    }
}

int main()
{
    int T;
    cin >> T;
    for(int i = 0; i < T; i++) {
        read_input();
        int result = solve();
        cout << "Case #" << i+1 << ": " << result << endl;
    }
}
