#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int main()
{
  int T;
  cin >> T;
  for(int t = 1; t <= T; t++)
  {
    vector<int> pos;
    vector<char> who;
    int N;
    cin >> N;
    for(int i = 0; i < N; i++)
    {
      int pos_;
      string who_;
      cin >> who_ >> pos_;
      pos.push_back(pos_);
      who.push_back(who_[0]);
    }

    int pos_o = 1;
    int pos_b = 1;
    int tt = 0;
    size_t a = 0;
    while(a < pos.size())
    {
      bool o_done = false;
      bool b_done = false;
      tt++;
      if(who.at(a) == 'O' && pos_o == pos.at(a))
      {
        o_done = true;
        a++;
        if(a >= pos.size()) { break; }
      }
      else if(who.at(a) == 'B' && pos_b == pos.at(a))
      {
        b_done = true;
        a++;
        if(a >= pos.size()) { break; }
      }
      for(size_t i = a; !o_done && i < pos.size(); i++)
      {
        if(who.at(i) == 'O')
        {
          if(pos_o < pos.at(i))
          {
            pos_o++;
          }
          else if(pos_o > pos.at(i))
          {
            pos_o--;
          }
          break;
        }
      }
      for(size_t i = a; !b_done && i < pos.size(); i++)
      {
        if(who.at(i) == 'B')
        {
          if(pos_b < pos.at(i))
          {
            pos_b++;
          }
          else if(pos_b > pos.at(i))
          {
            pos_b--;
          }
          break;
        }
      }
    }
    cout << "Case #" << t << ": " << tt << endl;
  }
}

