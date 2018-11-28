#include <iostream>
#include <cstdlib>
#include <vector>
#include <string>
#include <fstream>
#include <queue>

using namespace std;

#define PROBLEM_2

string FILE_PATH = "C:\\Documents and Settings\\Administrator\\Desktop\\";

void bot_trust();
void magicka();

int main()
{

#ifdef PROBLEM_1
  bot_trust();
#endif
#ifdef PROBLEM_2
  magicka();
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

void magicka()
{
  unsigned T, C, D;
  ifstream ifile; ofstream ofile;
  string ifile_path = FILE_PATH + "B-large.in", ofile_path = FILE_PATH + "output.txt";

  ifile.open(ifile_path.c_str());

  ifile >> T;
  ofile.open(ofile_path.c_str());

  for (unsigned i = 0; i < T; i++)
  {
    string N, input, output;
    string possible_output;
    vector<string> combine, oppose;

    ifile >> C;
    for (unsigned j = 0; j < C; j++)
    {
      ifile >> input;
      combine.push_back(input);
    }

    ifile >> D;
    for (unsigned j = 0; j < D; j++)
    {
      ifile >> input;
      oppose.push_back(input);
    }

    ifile >> N >> N;
    unsigned left = 0, combined_left = 0;
    bool maybe_opposed = false;
    for (unsigned j = 0; j < N.size(); j++)
    {
      // invoke
      output.push_back(N[j]);
      // combine (if possible)
      int last = output.size() - 1;
      if (last >= 1)
      {
        for (unsigned k = 0; k < combine.size(); k++)
        {
          if ((combine[k][0] == output[last-1] && combine[k][1] == output[last]) || (combine[k][1] == output[last-1] && combine[k][0] == output[last]))
          {
            output = output.substr(0,last-1);
            output.push_back(combine[k][2]);
            last--;
            k = combine.size();
          }
        }
      }
      for (unsigned k = 0; k < oppose.size() && last >= 1; k++)
      {
        if (output.find(oppose[k][0]) != string::npos && output.find(oppose[k][1]) != string::npos)
        {
          output = "";
          k = oppose.size();
        }
      }
    }// end for j
    output += possible_output;
    ofile << "Case #" << i+1 << ": [";
    for (unsigned k = 0; k < output.size(); k++)
    {
      ofile << output[k];
      if (k != output.size() - 1)
        ofile << ", ";
    }
    ofile << "]" << endl;
  }

  ofile.close();
  ifile.close();
}