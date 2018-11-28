#include <iostream>
#include <vector>
#include <stdexcept>
#include <cmath>
using namespace std;

int main()
{
  size_t num_test_cases;
  cin >> num_test_cases;

  for (size_t i = 0; i < num_test_cases; ++i)
  {
    size_t num_buttons;
    cin >> num_buttons;
    vector<size_t> orange_buttons, blue_buttons;
    vector<bool> blue_turn;
    for (size_t j = 0; j < num_buttons; ++j)
    {
      char color;
      size_t button;
      cin >> color >> button;
      switch (color)
      {
      case 'O':
        orange_buttons.push_back(button);
        break;
      case 'B':
        blue_buttons.push_back(button);
        break;
      default:
        throw runtime_error("Invalid color");
      }
      blue_turn.push_back(color == 'B');
    }
    signed num_steps_required = 0;
    signed blue_pos = 1, orange_pos = 1;
    vector<size_t>::iterator o_iter = orange_buttons.begin(), b_iter = blue_buttons.begin();
    for (vector<bool>::iterator turn_iter = blue_turn.begin(); turn_iter != blue_turn.end(); ++turn_iter)
    {
      if (*turn_iter)
      {
        signed button_to_press = *b_iter++;
        signed steps_this_turn = abs(button_to_press - blue_pos) + 1;
        num_steps_required += steps_this_turn;
        blue_pos = button_to_press;
        if (o_iter != orange_buttons.end())
        {
          signed next_orange_button = *o_iter;
          if (abs(next_orange_button - orange_pos) <= steps_this_turn)
          {
            orange_pos = next_orange_button;
          }
          else
          {
            orange_pos += copysign(1.0, next_orange_button - orange_pos) * steps_this_turn;
          }
        }
      }
      else
      {
        signed button_to_press = *o_iter++;
        signed steps_this_turn = abs(button_to_press - orange_pos) + 1;
        num_steps_required += steps_this_turn;
        orange_pos = button_to_press;
        if (b_iter != blue_buttons.end())
        {
          signed next_blue_button = *b_iter;
          if (abs(next_blue_button - blue_pos) <= steps_this_turn)
          {
            blue_pos = next_blue_button;
          }
          else
          {
            blue_pos += copysign(1.0, next_blue_button - blue_pos) * steps_this_turn;
          }
        }
      }
      //cout << "Steps " << num_steps_required << ", OrangePos " << orange_pos << ", BluePos " << blue_pos << endl;
    }
    cout << "Case #" << i + 1 << ": " << num_steps_required << endl;
  }
}
