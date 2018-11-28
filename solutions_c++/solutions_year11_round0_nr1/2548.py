#include<iostream>
#include<vector>
#include<queue>

using namespace std;

int move(int pos, int goal) {
    if(pos == goal)
        return pos;
    else if(pos < goal)
        return pos+1;
    else
        return pos-1;
}

int main()
{
    int T; cin >> T;
    for(int t = 1; t <= T; ++t) {
        int N; cin >> N;
        vector<int> worker(N);
        vector< queue<int> > goal(2);

        for(int i = 0; i < N; ++i) {
            char w; int g;
            cin >> w >> g;
            worker[i] = (w == 'B');
            goal[worker[i]].push(g);
        }

        vector<int> pos(2, 1);

        int i = 0, steps = 0;
        while(i < N) {
            int next = (worker[i]+1)%2;
            if(pos[next] != goal[next].front())
                pos[next] = move(pos[next], goal[next].front());
            
            if(pos[worker[i]] == goal[worker[i]].front()) {
                goal[worker[i]].pop();
                ++i;
            } else
                pos[worker[i]] = move(pos[worker[i]], goal[worker[i]].front());

            ++steps;
        }

        cout << "Case #" << t << ": " << steps << endl;
    }

    return 0;
}
