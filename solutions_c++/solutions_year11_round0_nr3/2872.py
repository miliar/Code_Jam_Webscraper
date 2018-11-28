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
#define first(n) ((uint) ((1U << (n)) - 1U))

vector <string> split(const string _s, const string del);
int toInt(string s) {int r = 0; istringstream ss(s); ss >> r; return r;}
string toStr(int n) {ostringstream ss; ss << n; return ss.str();}

uint next(uint x) {
    uint smallest = x & -x;
    uint ripple = x + smallest;
    uint new_smallest = ripple & -ripple;
    uint ones = ((new_smallest / smallest) >> 1) - 1;
    return ripple | ones;
}

string run(vector <int> inputs)
{
  string ret;
  int i, j, max = 0, csize = inputs.size();
  int limit = csize / 2;
  uint x;

  for (i = 1; i <= limit; i++) {
      x = first(i);
      while (!(x & ~first(csize))) {
          uint s = x;
          int psum1 = 0, psum2 = 0;
          int ssum1 = 0, ssum2 = 0;
          for (j = 1; j <= csize; j++) {
              if (s & 1) {
                  psum1 ^= inputs[j-1];
                  ssum1 += inputs[j-1];
              }
              else {
                  psum2 ^= inputs[j-1];
                  ssum2 += inputs[j-1];
              }
              s >>= 1;
          }

          if (psum1 == psum2) {
              if (ssum1 > max)
                  max = ssum1;
              if (ssum2 > max)
                  max = ssum2;
          }
          x = next(x);
      }
  }

  if (max > 0)
      ret = toStr(max);
  else
      ret = "NO";

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
  for (unsigned int i=0; i<tmp.size(); i++) args.push_back(toInt(tmp[i]));

  for (int lineNum = 0; lineNum<args[0]; lineNum++)
    {
      string result;
      vector <int> tokens;

      getline(file, line); // num of candies;
      getline(file, line);
      tmp = split(line, " ");
      for (unsigned int i=0; i<tmp.size(); i++) tokens.push_back(toInt(tmp[i]));

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
