#include <iostream>
#include <list>
#include <cmath>

using namespace std;

class Robot {
    public:
        Robot();
        void addInstruction(int button);
        void move();
        bool isAtButton();
        void pushButton();
        void reset();

    private:
        list<int> instructions;
        int currentPosition;
        int currentTarget;
};

Robot::Robot() {
    reset();
}

void Robot::reset() {
    currentPosition = 1;
    currentTarget = 1;
    instructions.clear();
}

void Robot::addInstruction(int button) {
    if (instructions.empty()) {
        currentTarget = button;
    }
    instructions.push_back(button);
}

bool Robot::isAtButton() {
    return (currentPosition == currentTarget);
}

void Robot::pushButton() {
    instructions.pop_front();
    currentTarget = instructions.front();
}

void Robot::move() {
    int distance = currentTarget - currentPosition;
    int absDistance = static_cast<int>(abs(static_cast<double>(distance)));

    if (distance != 0) {
        int delta = distance/absDistance;
        currentPosition += delta;
    }
}

int main(int argc, const char *argv[])
{
    Robot robot1;
    Robot robot2;
    Robot* currentRobot = &robot1;
    Robot* otherRobot = &robot2;
    list<char> turns;

    int T = 0;
    cin >> T;

    for (int k = 0; k < T; k++) {
        int N = 0;
        turns.clear();
        robot1.reset();
        robot2.reset();

        cin >> N;

        for (int j = 0; j < N; j++) {
            char c = 0;
            int button = 0;

            cin >> c;
            cin >> button;

            turns.push_back(c);
            if (c == 'O') {
                robot1.addInstruction(button);
            } else if (c == 'B') {
                robot2.addInstruction(button);
            }
        }

        int time = 0;
        while (!turns.empty()) {
            char turn = turns.front();
            turns.pop_front();

            if (turn == 'O') {
                currentRobot = &robot1;
                otherRobot = &robot2;
            } else {
                currentRobot = &robot2;
                otherRobot = &robot1;
            }

            while (!currentRobot->isAtButton()) {
                time++;

                currentRobot->move();
                otherRobot->move();
            }

            time++;
            currentRobot->pushButton();
            otherRobot->move();
        }

        cout << "Case #" << k+1 << ": " << time << endl;
    }

    return 0;
}
