#include <cmath>
#include <string>
#include <vector>
#include <algorithm>
#include <utility>
#include <iostream>

using namespace std;

enum BotColor {
    ORANGE,
    BLUE
};

typedef pair<BotColor, int> ButtonPress;
typedef vector<ButtonPress>::const_iterator ButtonPressItr;

bool OrangeButtonPress(const ButtonPress& press) {
    return press.first == ORANGE;
}

bool BlueButtonPress(const ButtonPress& press) {
    return press.first == BLUE;
}

int CountButtonPresses(const vector<ButtonPress>& presses) {
    int total_steps = 0;
    int current_pos[2] = { 1, 1 };
    ButtonPressItr next_press[2];
    next_press[ORANGE] = find_if(presses.begin(), presses.end(), OrangeButtonPress);
    next_press[BLUE] = find_if(presses.begin(), presses.end(), BlueButtonPress);
    
    for (size_t i = 0; i < presses.size(); ++i) {
        BotColor current_bot = (next_press[ORANGE] < next_press[BLUE] ? ORANGE : BLUE);
        BotColor other_bot = (current_bot == ORANGE ? BLUE : ORANGE);
        
        int num_steps = abs(current_pos[current_bot] - next_press[current_bot]->second) + 1;
        current_pos[current_bot] = next_press[current_bot]->second;
        total_steps += num_steps;
        
        if (next_press[other_bot] != presses.end()) {
            if (current_pos[other_bot] < next_press[other_bot]->second) {
                current_pos[other_bot] = min(next_press[other_bot]->second, current_pos[other_bot] + num_steps);
            } else {
                current_pos[other_bot] = max(next_press[other_bot]->second, current_pos[other_bot] - num_steps);
            }
        }
        
        next_press[current_bot] = find_if(next_press[current_bot] + 1, presses.end(),
            (current_bot == ORANGE ? OrangeButtonPress : BlueButtonPress));
    }
    
    return total_steps;
}

int main(int argc, char** argv) {
    int num_test_cases;
    cin >> num_test_cases;
    
    for (int i = 0; i < num_test_cases; ++i) {
        int num_button_presses;
        cin >> num_button_presses;
        
        vector<ButtonPress> presses(num_button_presses);
        for (size_t j = 0; j < presses.size(); ++j) {
            string color;
            cin >> color >> presses[j].second;
            presses[j].first = (color == "O" ? ORANGE : BLUE);
        }
        
        cout << "Case #" << (i + 1) << ": " << CountButtonPresses(presses) << endl;
    }
    
    return 0;
}
