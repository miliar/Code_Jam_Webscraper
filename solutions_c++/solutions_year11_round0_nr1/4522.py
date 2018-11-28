#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <cmath>
using namespace std;

const char ROBOT_O = 'O';
const char ROBOT_B = 'B';

void generate_steps(const vector<int>& buttons, list<int>& steps)
{
    int current_location = 1;

    for (size_t i = 0; i < buttons.size(); i++)
    {
        if (buttons.at(i) == current_location)
        {
            steps.push_back(1);
        }
        else
        {
            steps.push_back(abs(buttons[i] - current_location) + 1);
            current_location = buttons[i];
        }
    }
}

void perform_button_push(int& total_time, int& last_action_time, list<int>& steps)
{
    total_time = max(total_time + 1, last_action_time + steps.front());
    steps.pop_front();
    last_action_time = total_time;
}

// perform the actual processing for a sequence
// uses the list of buttons for both robots, and the order of button pushes
int process_sequence(const vector<int>& o_buttons, const vector<int>& b_buttons,
        const vector<char>& ordering)
{
    list<int> o_steps, b_steps;
    // get a list of the number of steps (or actions) needed from one button
    // push to the next
    generate_steps(o_buttons, o_steps);
    generate_steps(b_buttons, b_steps);

    int time = 0; // counter for time taken so far
    int last_o_time = 0, last_b_time = 0; // remembers the last button push for each robot

    for (size_t i = 0; i < ordering.size(); i++)
    {
        const char robot = ordering[i];
        if (robot == ROBOT_O)
        {
            perform_button_push(time, last_o_time, o_steps);
        }
        else
        {
            perform_button_push(time, last_b_time, b_steps);
        }
    }

    return time;
}

int main(int argc, char* argv[])
{
    // read filename from first argument
    const string filename = argv[1];

    ifstream in(filename.c_str());

    int num_cases = 0;
    in >> num_cases;

    // read in all of the data
    for (int i = 0; i < num_cases; i++)
    {
        int num_buttons;
        // store the locations of buttons for both robots
        vector<int> o_buttons, b_buttons;
        // store the sequence of button pushes (either 'O' or 'B')
        vector<char> ordering;

        in >> num_buttons;

        for (int j = 0; j < num_buttons; j++)
        {
            char robot_type = 0;
            int button_location = 0;
            in >> robot_type >> button_location;

            if (robot_type == ROBOT_O)
            {
                o_buttons.push_back(button_location);
            }
            else
            {
                b_buttons.push_back(button_location);
            }

            ordering.push_back(robot_type);
        }

        const int time = process_sequence(o_buttons, b_buttons, ordering);
        cout << "Case #" << i+1 << ": " << time << endl;
    }

    return 0;
}
