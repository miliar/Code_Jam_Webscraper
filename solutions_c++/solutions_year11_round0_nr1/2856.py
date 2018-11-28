#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <utility>
#include <set>
#include <cctype>
#include <queue>
#include <stack>
#include <fstream>

using namespace std;
typedef unsigned int uint;

vector <string> split(const string _s, const string del);
int toInt(string s) {int r = 0; istringstream ss(s); ss >> r; return r;}
string toStr(int n) {ostringstream ss; ss << n; return ss.str();}

int moveMachine(int pos, int tar) {
    if (pos < tar)
        return ++pos;
    else if (pos > tar)
        return --pos;
    return pos;
}

string run(vector <string> inputs)
{
  string ret;
  int seqsize = toInt(inputs[0]);
  vector <pair <string, int> > seq, oseq, bseq;
  int bpos = 1, bcurr = 0, btar = 0, opos = 1, ocurr = 0, otar = 0;
  int time = 0, pushed;
  string turn;

  for (uint i = 1; i < inputs.size(); i += 2) {
      seq.push_back(make_pair(inputs[i], toInt(inputs[i+1])));
      if (inputs[i] == "O")
          oseq.push_back(make_pair(inputs[i], toInt(inputs[i+1])));
      if (inputs[i] == "B")
          bseq.push_back(make_pair(inputs[i], toInt(inputs[i+1])));
  }

  for (int i = 0; i < seqsize; i++) {
      turn = seq[i].first; // O or B
      if (bcurr < bseq.size())
          btar = bseq[bcurr].second;
      if (ocurr < oseq.size())
          otar = oseq[ocurr].second;
      pushed = 0;
      // cout << turn << " " << btar << " " << otar << endl;

      while (pushed == 0) {
          // cout << bpos << " " << opos << endl;
          if (turn == "O" && opos == otar) {
              pushed = 1;
              ocurr++;
              bpos = moveMachine(bpos, btar);
          }
          else if (turn == "B" && bpos == btar) {
              pushed = 1;
              bcurr++;
              opos = moveMachine(opos, otar);
          }
          else {
              bpos = moveMachine(bpos, btar);
              opos = moveMachine(opos, otar);
          }
          time++;
      }
  }

  ret = toStr(time);

  return ret;
}

int main(int argc, char ** argv)
{
  if (argc != 2)
  {
    cout << "Usage " << argv[0] << " <input file name>\n";
    return 0;
  }

  ifstream file (argv[1]);
  string line;
  vector <string> tmp;
  vector <int> args;

  getline(file, line);
  tmp = split(line, " ");
  for (uint i=0; i < tmp.size(); i++) args.push_back(toInt(tmp[i]));

  for (int lineNum = 0; lineNum<args[0]; lineNum++)
    {
      string result;
      vector <string> tokens;

      getline(file, line);
      tmp = split(line, " ");
      for (unsigned int i=0; i<tmp.size(); i++) tokens.push_back(tmp[i]);

      result = run(tokens);
      cout << "Case #" << lineNum+1 << ": " << result << endl;
    }

  return 0;
}

vector <string> split(const string _s, const string del)
{
  vector <string> ret;
  string s = _s;

  while (!s.empty())
    {
      size_t pos = s.find(del);
      string sub = "";
      sub = s.substr(0, pos);
      ret.push_back(sub);
      if (pos != string::npos)
          pos += del.size();
      s.erase(0, pos);
    }

  return ret;
}
