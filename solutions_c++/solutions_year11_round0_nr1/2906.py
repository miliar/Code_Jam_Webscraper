#include <iostream>
#include <algorithm>
#include <utility>
#include <vector>

#include <stdint.h>
#include <limits.h>

using namespace std;

int main()
{
  int T;
  cin >> T;

  for(int ti = 1; ti <= T; ti++)
  {
    int N;
    cin >> N;
    vector<int> blue_positions, 
                orange_positions, 
                blue_steps, 
                orange_steps;
    blue_positions.reserve(N);
    blue_steps.reserve(N);
    orange_positions.reserve(N);
    orange_steps.reserve(N);
    for(int ni = 0; ni < N; ni++)
    {
      char color;
      int position;
      cin >> color >> position;
      if(color == 'B')
      {
        blue_positions.push_back(position);
        blue_steps.push_back(ni);
      }
      else
      {
        orange_positions.push_back(position);
        orange_steps.push_back(ni);
      }
    }
    // signal values to ensure completion of other bot's steps
    blue_steps.push_back(INT_MAX);
    orange_steps.push_back(INT_MAX);
    // these positions don't modify time, because bot will be going there in a
    // `background' 'cause correspoding step is too large
    blue_positions.push_back(1);
    orange_positions.push_back(1);
    
    int time = 0;
    int position_o = 1,
        position_b = 1;
    int target_o = -1,
        target_b = -1;
    
    size_t blue_it = 0,
           orange_it = 0;

    while(!(blue_it >= blue_positions.size() - 1 && orange_it >= orange_positions.size() - 1))
    {
      bool orange_turn = orange_steps.at(orange_it) < blue_steps.at(blue_it);
      target_o = orange_positions.at(orange_it);
      target_b = blue_positions.at(blue_it);
      // extracted from conditions
      int o_moves = abs(target_o - position_o) + 1;
      int b_moves = abs(target_b - position_b) + 1;
      if(orange_turn)
      {
        if(position_o == target_o)
        {
          // orange is on the position, just press & proceed to next step
          time += 1;
          orange_it++;
        }
        else
        {
          // orange isn't on the position, moving and pressing
          time += abs(target_o - position_o) + 1;
          position_o = target_o;
          orange_it++;
        }

        if(position_b == target_b)
        {
          // blue is on the position, just wait
        }
        else
        {
          // blue isn't on the position, moving while possible
          int b_moves_needed = target_b - position_b;
          if(abs(b_moves_needed) <= o_moves)
          {
            // blue has enough moves to reach position, simply move it
            position_b = target_b;
          }
          else
          {
            // blue hasn't enough moves to reach position, so move it while
            // possible (during orange's movement) in the appropriate direction
            if(b_moves_needed < 0)
            {
              position_b -= o_moves;
            }
            else
            {
              position_b += o_moves;
            }
          }
        }
      }
      else
      {
        // same for blue
        if(position_b == target_b)
        {
          time += 1;
          blue_it++;
        }
        else
        {
          time += abs(target_b - position_b) + 1;
          position_b = target_b;
          blue_it++;
        }

        if(position_o == target_o)
        {
        }
        else
        {
          int o_moves_needed = target_o - position_o;
          if(abs(o_moves_needed) <= b_moves)
          {
            position_o = target_o;
          }
          else
          {
            // blue hasn't enough moves to reach position, so move it while
            // possible (during orange's movement) in the appropriate direction
            if(o_moves_needed < 0)
            {
              position_o -= b_moves;
            }
            else
            {
              position_o += b_moves;
            }
          }
        }
      }
    }
    cout << "Case #" << ti << ": " << time << endl;
  }

  return 0;
}
