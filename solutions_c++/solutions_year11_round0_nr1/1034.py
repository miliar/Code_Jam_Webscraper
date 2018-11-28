#include <iostream>
#include <deque>
#include <utility>
#include <vector>
#include <cstdlib>

using namespace std;

typedef vector<pair<bool, int> > TestCase;

void parseInput(vector<TestCase>* inputs) {
    int caseNumber;
    cin >> caseNumber;
    
    for(int i = 0; i < caseNumber; ++i) {
        TestCase currentCase;

        int buttons;
        cin >> buttons;

        for(int j = 0; j < buttons; ++j) {
            char color;
            cin >> color;
            int position;
            cin >> position;

            currentCase.push_back(make_pair(color == 'O', position));
        }

        inputs->push_back(currentCase);
    }
}

int solveTestCase(TestCase& testCase) {
    int positions[2] = { 1, 1 };
    int credits[2] = { 0, 0 };
    int secondsElapsed = 0;

    for(int i = 0; i < testCase.size(); ++i) {
        int index = static_cast<int>(testCase[i].first);
        int otherIndex = (index + 1) % 2;

        int timeRequired = max(abs(positions[index] - testCase[i].second) + 1 - credits[index], 1);
        secondsElapsed += timeRequired;
        credits[otherIndex] += timeRequired;
        positions[index] = testCase[i].second;
        credits[index] = 0;
    }

    return secondsElapsed;
}

void outputSolution(int caseNo, int answer) {
    cout << "Case #" << caseNo << ": " << answer << endl;
}

int main() {
    vector<TestCase> inputs;
    parseInput(&inputs);
    for(int i = 0; i < inputs.size(); ++i) {
        outputSolution(i + 1, solveTestCase(inputs[i]));
    }
    return 0;
}

