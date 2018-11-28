#include "stdafx.h"


#include <iostream>
#include <fstream>
#include <sstream>
#include <memory>
#include <limits>
#include <list>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <algorithm>
#include <stdlib.h>

using std::cin;
using std::cout;
using std::endl;
using std::set;
using std::map;
using std::max;
using std::min;
using std::stringstream;

using std::ifstream;
using std::ofstream;
using std::stack;
using std::string;
using std::vector;
using std::numeric_limits;

class CodeJameCredtCard {
public:
    void Solve(const string& input_file, const string& output_file) {
        ifstream input(input_file.c_str());
        ofstream output(output_file.c_str());

        int case_number;
        input >> case_number;

        for (int i = 0; i < case_number; ++i) {
            int card_value = 0;
            vector<int> values;
            int first;
            int second;

            ReadCase(input, card_value, values);
            SolveProblem(card_value, values, first, second);
            WriteCaseResult(i+1, output, first, second);
        }
        input.close();
        output.close();
    }
private:
    void SolveProblem(int card_value, const vector<int>& values, int& first, int& second) {
        for (size_t i = 0; i < values.size(); ++i) {
            for (size_t j = i + 1; j < values.size(); ++j) {
                if (values[i] + values[j] == card_value) {
                    first = i + 1;
                    second = j + 1;
                }
            }
        }
    }

    void ReadCase(ifstream& input_stream, int& card_value, vector<int>& values) {
        input_stream >> card_value;

        int values_number;
        input_stream >> values_number;

        for (int i = 0; i < values_number; ++i) {
            int val;
            input_stream >> val;
            values.push_back(val);
        }
    }
    void WriteCaseResult(int case_num, ofstream& output_stream, int first, int second) {
        cout << "Case #" << case_num << ": " << min(first, second) << " " << second << std::endl;
        output_stream << "Case #" << case_num << ": " << min(first, second) << " " << second << std::endl;
    }
};

class CodeJameRobot {
public:
    void Solve(const string& input_file, const string& output_file) {
        ifstream input(input_file.c_str());
        ofstream output(output_file.c_str());

        int case_number;
        input >> case_number;

        for (int i = 0; i < case_number; ++i) {
            vector<char> steps;
            vector<int> orangeSteps;
            vector<int> blueSteps;

            ReadCase(input, steps, orangeSteps, blueSteps);
            int time = SolveProblem(steps, orangeSteps, blueSteps);
            WriteCaseResult(i+1, output, time);
        }
        input.close();
        output.close();
    }
private:
    int SolveProblem(vector<char>& steps, vector<int>& orangeSteps, vector<int>& blueSteps) {
        int curO = 1;
        int curB = 1;

        int stepIndexO = 0;
        int stepIndexB = 0;

        char curRobotStep = steps[0];
        int step = 0;
        for (int i = 0; i <= 110000; ++i) {
            if (curRobotStep == 'B') {
                // press
                if (blueSteps[stepIndexB] == curB) {
                    stepIndexB++;
                    step++;
                    if (step < steps.size())
                        curRobotStep = steps[step];
                } else if (curB > blueSteps[stepIndexB]) {
                    curB--;
                } else if (curB < blueSteps[stepIndexB]) {
                    curB++;
                }

                if (stepIndexO < orangeSteps.size()) {
                    if (curO > orangeSteps[stepIndexO]) {
                        curO--;
                    } else if (curO < orangeSteps[stepIndexO]) {
                        curO++;
                    }
                }
            } else {
                // press
                if (orangeSteps[stepIndexO] == curO) {
                    stepIndexO++;
                    step++;
                    if (step < steps.size())
                        curRobotStep = steps[step];
                } else if (curO > orangeSteps[stepIndexO]) {
                    curO--;
                } else if (curO < orangeSteps[stepIndexO]) {
                    curO++;
                }

                if (stepIndexB < blueSteps.size()) {
                    if (curB > blueSteps[stepIndexB]) {
                        curB--;
                    } else if (curB < blueSteps[stepIndexB]) {
                        curB++;
                    }
                }
            }

            if (step == steps.size()) {
                return i + 1;
            }
        }
        return 0;
    }

    void ReadCase(ifstream& input_stream, vector<char>& steps, vector<int>& orangeSteps, vector<int>& blueSteps) {
        int step_number;
        input_stream >> step_number;

        for (int i = 0; i < step_number; ++i) {
            char symbol;
            int val;
            input_stream >> symbol;
            input_stream >> val;

            steps.push_back(symbol);

            if (symbol == 'B') {
                blueSteps.push_back(val);
            } else {
                orangeSteps.push_back(val);
            }
        }
    }
    void WriteCaseResult(int case_num, ofstream& output_stream, int time) {
        cout << "Case #" << case_num << ": " << time << std::endl;
        output_stream << "Case #" << case_num << ": " << time << std::endl;
    }
};


int main() {
    CodeJameRobot t;
    t.Solve("c:\\Sources\\CodeJam\\CodeJam\\input\\task1.txt", "c:\\Sources\\CodeJam\\CodeJam\\output\\task1.txt");

    return 0;
}