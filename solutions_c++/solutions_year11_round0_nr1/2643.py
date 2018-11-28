#include <iostream>
#include <math.h>
#include <vector>

using namespace std;

struct rpair {
    char color;
    int cind;
    int pos;
};

void debprint(vector<rpair>& task)
{
    for(size_t i = 0; i < task.size(); ++i) {
        cout << task[i].color << " " << task[i].pos << " ";
    }
}

long getSteps(int to, int from)
{
    return abs(to - from) + 1;
}

int solve(vector<rpair>& task)
{
    int curCol = 0;
    long curSec = 0;
    long tot = 0;
    int curPos[2] = {1, 1};
    for(size_t i = 0; i < task.size(); ++i)
    {
        long steps = getSteps(task[i].pos, curPos[task[i].cind]);
        curPos[task[i].cind] = task[i].pos;
        if(curCol != task[i].cind) {
            long diffSteps = ((steps <= curSec ? 1 : (steps - curSec)) + 0);
            tot += (diffSteps + 0);
            curSec = (diffSteps + 0);
        } else {
            tot += steps;
            curSec += steps;
        }
        curCol = task[i].cind;
//        cout << "task:" << task[i].color << task[i].pos << ", steps = " << steps << " curSec = " << curSec << " tot = " << tot << endl;
    }
//    tot += 0;
    return tot;
}

void TC(int T)
{
    int N = 0;
    cin >> N;
    if(N<=0){
        return;
    }
    vector<rpair> task = vector<rpair>(N);
    for (int i = 0; i < N; ++i) {
        cin >> task[i].color >> task[i].pos;
        task[i].cind = (task[i].color == 'O' ? 0 : 1);
    }
//    debprint(task);
    cout << "Case #" << T + 1 << ": " << solve(task) << endl;
}

int main()
{
    int N = 0;
    cin >> N;
    for(int i = 0; i < N; ++i) {
        TC(i);
    }
    return 0;
}
