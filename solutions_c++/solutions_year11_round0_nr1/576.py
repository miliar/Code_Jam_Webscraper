#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <iterator>
#include <utility>

enum ERobot {
    R_ORANGE,
    R_BLUE
};

int pressButton(int& robotPos, int buttonPos, int freeTimeToAction) {
    int timeToMoveToButton = std::abs(robotPos - buttonPos);
    robotPos = buttonPos;
    return 1 + std::max(0, timeToMoveToButton - freeTimeToAction);
}

int main() {
    std::ifstream input("test.in");
    std::ofstream output("test.out");

    int numTests;
    input >> numTests;
    for (int testIdx = 1; testIdx <= numTests; ++testIdx) {
        int numButtonsToPress;
        input >> numButtonsToPress;

        int completeTime = 0;
        int orangePos = 1;
        int bluePos = 1;

        ERobot prevActiveRobot = R_ORANGE;
        int freeActionTime = 0;
        for (int actionIdx = 0; actionIdx < numButtonsToPress; ++actionIdx) {
            std::string color;
            int buttonPos;
            input >> color >> buttonPos;
            ERobot robot = color == "O" ? R_ORANGE : R_BLUE;

            int& activeRobotPos = robot == R_ORANGE ? orangePos : bluePos;
            if (robot != prevActiveRobot) {
                int timeToPressButton = pressButton(activeRobotPos, buttonPos, freeActionTime);
                completeTime += timeToPressButton;
                freeActionTime = timeToPressButton;
            } else {
                int timeToPressButton = pressButton(activeRobotPos, buttonPos, 0);
                completeTime += timeToPressButton;
                freeActionTime += timeToPressButton;
            }
            prevActiveRobot = robot;
        }
        output << "Case #" << testIdx << ": " << completeTime << std::endl;
    }

    input.close();
    output.close();

    return 0;
}