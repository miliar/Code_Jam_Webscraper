#include <iostream>
#include <vector>
using namespace std;

struct test_sequence {
    char robot;
    int pos;
};


static int findNextPos(const vector<struct test_sequence>& tests, char robot, int from)
{
    int ret = -1;
    for (int i = from; i < tests.size(); i++) {
        if (robot == tests[i].robot) {
            ret = tests[i].pos;
            break;
        }
    }
    return ret;
}

void move(int& cur, int next, bool& moved)
{
    moved = false;
    if (next == -1)
        return;

    if (next < 0 || next > 100)
        return;

    if (cur < 0 || cur > 100)
        return;

    if (next < cur) {
        cur --;
        moved = true;
    }
    if (next > cur) {
        cur ++;
        moved = true;
    }
}

void push(char robot, int& count)
{
    count ++;
}

void engine(const vector<struct test_sequence>& tests, int casenum)
{
    int count = 0;
    int cur_B_pos = 1;
    int cur_O_pos = 1;
    char next_push_robot = tests[0].robot;
    int next_B_pos = findNextPos(tests, 'B', 0);
    int next_O_pos = findNextPos(tests, 'O', 0);
    int cur_R_P = 0;
    bool B_moved;
    bool O_moved;
    while (cur_R_P < tests.size()) {
        move(cur_B_pos, next_B_pos, B_moved);
        move(cur_O_pos, next_O_pos, O_moved);
        if (next_push_robot == 'B' && next_B_pos == cur_B_pos && !B_moved) {
            push('B', count);
            cur_R_P ++;
            if (cur_R_P < tests.size()) {
                next_B_pos = findNextPos(tests, 'B', cur_R_P);
                next_push_robot = tests[cur_R_P].robot;
            }
            continue;
        }

        if (next_push_robot == 'O' && next_O_pos == cur_O_pos && !O_moved) {
            push('O', count);
            cur_R_P ++;
            if (cur_R_P < tests.size()) {
                next_O_pos = findNextPos(tests, 'O', cur_R_P);
                next_push_robot = tests[cur_R_P].robot;
            }
            continue;
        }
        count ++;
    }
    cout << "Case #"<<casenum<<": "<<count<<endl;
}

int main(int argc, char* argv[])
{
    int testcases;
    int size;
    char robot;
    int pos;
    vector<struct test_sequence> tests(100);
    int ti = 1;

    cin >> testcases;
    //cout << testcases << endl;
    while (testcases != 0) {
        cin >> size;
        //cout << size << " ";
        tests.clear();
        while (size > 0) {
            struct test_sequence ts;
            cin >> ts.robot;
            cin >> ts.pos;
            tests.push_back(ts);
            size --;
            //cout << robot << " " << pos << " ";
        }
        engine(tests, ti);
        //cout << endl;
        testcases --;
        ti ++;
    }
    return 0;
}
