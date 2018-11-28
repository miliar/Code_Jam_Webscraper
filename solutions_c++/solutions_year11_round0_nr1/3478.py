#include <vector>
#include <iostream>

using namespace std;

struct Button
{
    bool fOrangeM;
    int numM;
};

struct Robot
{
    int posM;
    int timeM;
};

inline int max(int i1, int i2) {
    return (i1 > i2) ? i1 : i2;
}

inline int abs(int i1, int i2) {
    return i1 < 0 ? -i1 : i1;
}

static int solve(vector<Button> &buttons)
{
    Robot r[2];
    r[0].posM = 1;
    r[0].timeM = 0;
    r[1].posM = 1;
    r[1].timeM = 0;
    int size = buttons.size();
    for (int i = 0; i < size; i++) {
        Button &button = buttons[i];
        Robot &robot = r[button.fOrangeM];
        int pos = button.numM;
        int t2 = robot.timeM + abs(robot.posM - pos);
        robot.timeM = max(r[!button.fOrangeM].timeM, t2) + 1;
        robot.posM = pos;
    }
    return max(r[0].timeM, r[1].timeM);
}

static void print(vector<Button> &buttons)
{
    int size = buttons.size();
    cout << size << " ";
    for (int i = 0; i < size; i++) {
        char c = 'B';
        if (buttons[i].fOrangeM) {
            c = 'O';
        }
        cout << c << " " << buttons[i].numM << " ";
    }
    cout << "\n";
}

int main(int argc, const char *argv[])
{
    int T = 0;
    cin >> T;
    vector<Button> buttons;
    for (int i = 0; i < T; i++)
    {
        int numButtons = 0;
        cin >> numButtons;
        buttons.resize(numButtons);
        for (int n = 0; n < numButtons; n++)
        {
            char c = '\0';
            int num = 0;
            cin >> c;
            cin >> num;
            buttons[n].fOrangeM = (c == 'O');
            buttons[n].numM = num;
        }
//        print(buttons);
        int solution = solve(buttons);
        cout << "Case #" << (i + 1) << ": " << solution << "\n";
    }
}
