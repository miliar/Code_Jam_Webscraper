//      robots.cpp
//      
//      Copyright 2011 Tóth Bence <totesz@totesz-desktop>
//      
//      This program is free software; you can redistribute it and/or modify
//      it under the terms of the GNU General Public License as published by
//      the Free Software Foundation; either version 2 of the License, or
//      (at your option) any later version.
//      
//      This program is distributed in the hope that it will be useful,
//      but WITHOUT ANY WARRANTY; without even the implied warranty of
//      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//      GNU General Public License for more details.
//      
//      You should have received a copy of the GNU General Public License
//      along with this program; if not, write to the Free Software
//      Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
//      MA 02110-1301, USA.


#include <iostream>
#include <fstream>
#include <vector>
#include <climits>

using namespace std;

typedef vector< pair<unsigned char, unsigned> > StepArray;

unsigned int countLength(const StepArray & steps) {
    unsigned int stepTimeSum = 0;
    vector<unsigned> position(UCHAR_MAX, 1);
    vector<unsigned> lastStepTime(UCHAR_MAX, 0);
    for (unsigned int i = 0; i < steps.size(); ++i) {
        const unsigned char agent = steps[i].first;
        const unsigned int button = steps[i].second;
        unsigned stepEndTime = lastStepTime[agent] + (button > position[agent] ? button - position[agent] : position[agent] - button);
        stepTimeSum = max(stepTimeSum, stepEndTime) + 1;
        cout << " position[agent]= " << position[agent] << "; lastStepTime[agent]=" << lastStepTime[agent] << "; dist=" << (button > position[agent] ? button - position[agent] : position[agent] - button);
        position[agent] = button;
        lastStepTime[agent] = stepTimeSum;
        cout << "; agent=" << agent << "; button=" << button << "; stepEndTime=" << stepEndTime << "; stepTimeSum=" << stepTimeSum << "; position[agent]= " << position[agent] << "; lastStepTime[agent]=" << lastStepTime[agent] << endl;
    }
    cout << endl;
    return stepTimeSum;
}

int main(int argc, char **argv)
{
    fstream input, output;
    input.open ("input.txt", fstream::in);
    output.open ("result.txt", fstream::out);
    unsigned int tcnum;
    input >> tcnum;
	for (unsigned int i = 0; i < tcnum; ++i) {
        unsigned int stepnum;
        input >> stepnum;
        StepArray steps;
        for (unsigned int j = 0; j < stepnum; ++j) {
            unsigned char agent;
            input >> agent;
            unsigned button;
            input >> button;
            steps.push_back(pair<unsigned char, unsigned>(agent, button));
        }
        output << "Case #" << i+1 << ": " << countLength(steps) << endl;
    }
    input.close();
    output.close();
	return 0;
}

