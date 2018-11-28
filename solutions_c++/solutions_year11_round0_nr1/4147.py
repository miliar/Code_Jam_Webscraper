#include <iostream>
#include <fstream>
#include <vector>
#include <utility>

using namespace std;

int main(int argc, char *argv[])
{
  vector<int> orange, blue;
  vector<int>::iterator o, b;

  pair<char,int> item;
  vector< pair<char,int> > task;
  vector< pair<char,int> >::iterator t;

  int T, N, time, o_pos, b_pos;

  ifstream in;
  ofstream out;

  if (argc == 3)
  {
    in.open(argv[1]);
    if (!in.is_open())
    {
      cerr << "Error opening " << argv[1] << endl;
      return 0;
    }
    out.open(argv[2]);
    if (!out.is_open())
    {
      in.close();
      cerr << "Error opening " << argv[2] << endl;
      return 0;
    }
  }
  else
  {
    in.open("in.txt");
    if (!in.is_open())
    {
      cerr << "Error opening in.txt" << endl;
      return 0;
    }
    out.open("out.txt");
    if (!out.is_open())
    {
      in.close();
      cerr << "Error opening out.txt" << endl;
      return 0;
    }
  }

  in >> T;
  for (int i = 0; i < T; i++)
  {
    orange.clear();
    blue.clear();
    task.clear();
    out << "Case #" << i + 1 << ": ";
    in >> N;
    for (int j = 0; j < N; j++)
    {
      in >> item.first >> item.second;
      task.push_back(item);
      switch (item.first)
      {
        case 'O' :
          orange.push_back(item.second);
          break;

        case 'B' :
          blue.push_back(item.second);
          break;

        default :
          cerr << "WTF?! Error in input" << endl;
          return 1;
      }
    }

    time = 0;
    o_pos = b_pos = 1;
    o = orange.begin();
    b = blue.begin();
    t = task.begin();
    while (t != task.end())
    {
      time++;
      if (t->first == 'O')
      {
        if (b_pos < *b)
          b_pos++;
        else if (b_pos > *b)
          b_pos--;
        if (o_pos == *o)
        {
          t++; //push the button
          o++;
        }
        else
        {
          if (o_pos < *o)
            o_pos++;
          else
            o_pos--;
        }
      }
      else
      {
        if (o_pos < *o)
          o_pos++;
        else if (o_pos > *o)
          o_pos--;
        if (b_pos == *b)
        {
          t++; //push the button
          b++;
        }
        else
        {
          if (b_pos < *b)
            b_pos++;
          else
            b_pos--;
        }
      }
    }
    out << time << endl;
  }

  return 0;
}

