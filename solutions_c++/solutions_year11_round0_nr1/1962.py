#include <iostream>
#include <cstdlib>
#include <vector>
#include <string>
#include <fstream>
#include <queue>

using namespace std;

#define PROBLEM_1

string FILE_PATH = "C:\\Documents and Settings\\Administrator\\Desktop\\";

void bot_trust();

int main()
{

#ifdef PROBLEM_1
  bot_trust();
#endif

  return 0;
}

void bot_trust()
{
  unsigned T, N;
  string ifile_path = FILE_PATH + "A-large.in", ofile_path = FILE_PATH + "output.txt";
  string input;
  int int_input;
  
  ifstream ifile; ofstream ofile;
  ifile.open(ifile_path.c_str());

  ifile >> T;
  ofile.open(ofile_path.c_str());

  for (unsigned i = 0; i < T; i++)
  {
    unsigned steps_total = 0;

    ifile >> N;
    vector<string> robot;
    vector<int> button;
    for (unsigned j = 0; j < N; j++)
    {
      ifile >> input;
      robot.push_back(input);
      ifile >> int_input;
      button.push_back(int_input);
    }

    int robot_b_pos = 1, robot_o_pos = 1;
    int robot_b_steps = 0, robot_o_steps = 0;

    for (unsigned j = 0; j < N; j++)
    {
      int abs = 0;
      if (j == 0)
      {
        steps_total += button[j];
        if (robot[j] == "B")
        {
          robot_b_pos = button[j];
          robot_b_steps = button[j];
        }
        else
        {
          robot_o_pos = button[j];
          robot_o_steps = button[j];
        }
      }
      else
      {
        if (robot[j-1] != robot[j])
        {
          if (robot[j] == "B")
          {
            abs = button[j] - robot_b_pos;
            if (abs < 0)
              abs = -abs;
            abs -= robot_o_steps;
            if (abs >= 0)
            {
              robot_b_steps += abs+1;
              steps_total += abs+1;
            }
            else
            {
              robot_b_steps = 1;
              steps_total++;
            }
            robot_b_pos = button[j];
            robot_o_steps = 0;
          }
          else
          {
            abs = button[j] - robot_o_pos;
            if (abs < 0)
              abs = -abs;
            abs -= robot_b_steps;

            if (abs >= 0)
            {
              robot_o_steps += abs+1;
              steps_total += abs+1;
            }
            else
            {
              robot_o_steps = 1;
              steps_total++;
            }
            robot_o_pos = button[j];
            robot_b_steps = 0;
          }
        }
        else
        {
          if (robot[j] == "B")
          {
            abs = button[j] - button[j-1];
            if (abs < 0)
              abs = -abs;
            robot_b_steps += abs+1;
            robot_b_pos = button[j];
            steps_total += abs+1;
          }
          else
          {
            abs = button[j] - button[j-1];
            if (abs < 0)
              abs = -abs;
            robot_o_steps += abs+1;
            robot_o_pos = button[j];
            steps_total += abs+1;
          }
        }
      }
    }
    ofile << "Case #" << i+1 << ": " << steps_total << endl;
  }

  ofile.close();
  ifile.close();
}