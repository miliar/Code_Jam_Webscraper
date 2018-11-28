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

vector <string> split(const string _s, const string del);
int toInt(string s) {int r = 0; istringstream ss(s); ss >> r; return r;}
string toStr(int n) {ostringstream ss; ss << n; return ss.str();}
string toStr(char n) {ostringstream ss; ss << n; return ss.str();}

string sortStr(string a, string b) { // stable
    if (a > b)
        return b + a;
    else
        return a + b;
}

string run(vector <string> inputs)
{
  string ret;
  int i = 0;
  map <string, string> comb;
  map <string, int> oppo;
  string invoke;

  // get combine
  if (toInt(inputs[i]) > 0) {
      int j = i + toInt(inputs[i]);
      for (i++; i < j + 1; i++) {
          string s1 = toStr(inputs[i][0]);
          string s2 = toStr(inputs[i][1]);
          string s3 = toStr(inputs[i][2]);
          string a = sortStr(s1, s2);
          comb.insert(map<string, string>::value_type(a, s3));
          // cout << a << " " << s3 << endl;
      }
  }
  else {
      i++;
  }

  // get opponent
  if (toInt(inputs[i]) > 0) {
      int j = i + toInt(inputs[i]);
      for (i++; i < j + 1; i++) {
          string s1 = toStr(inputs[i][0]);
          string s2 = toStr(inputs[i][1]);
          string a = sortStr(s1, s2);
          oppo.insert(map<string, int>::value_type(a, 1));
          // cout << a << endl;
      }
  }
  else {
      i++;
  }

  invoke = inputs[++i];
  vector <string> elist;

  for (i = 0; i < invoke.length(); i++) {
      // cout << invoke[i] << endl;
      elist.push_back(toStr(invoke[i]));

      // string hoge;
      // for (int j = 0; j < elist.size(); j++) {
      //     hoge += elist[j];
      // }
      // cout << hoge << endl;

      if (elist.size() > 1) {
          string tar;
          vector <string>::iterator it1, it2;

          // combine
          it1 = elist.end() - 1;
          it2 = it1 - 1;
          tar = sortStr(*it2, *it1);
          if (comb.count(tar) > 0) {
              string rep = comb[tar];
              elist.erase(it2, it1 + 1);
              elist.push_back(rep);
          }

          // opponent
          int del = 0;
          for (it1 = elist.begin(); it1 != elist.end() - 1; it1++) {
              for (it2 = it1 + 1; it2 != elist.end(); it2++) {
                  tar = sortStr(*it1, *it2);
                  // cout << tar << endl;
                  if (oppo.count(tar) > 0) {
                      del = 1;
                      break;
                  }
              }
              if (del == 1)
                  break;
          }
          if (del == 1)
              elist.clear();
      }
  }


  ret = "[";
  for (i = 0; i < elist.size(); i++) {
      ret += elist[i];
      if (i != elist.size() - 1)
          ret += ", ";
  }
  ret += "]";
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
