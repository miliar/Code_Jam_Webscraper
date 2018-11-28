#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <string>
#include <utility>

using namespace std;

int main(int argc, char *argv[])
{
  pair<char,char> cp;
  map<pair<char,char>,char> combined;
  map<pair<char,char>,char>::iterator cit;

  map<char,char> opposed;
  map<char,char>::iterator oit;

  vector<char> v;
  vector<char>::iterator vit;

  string s;
  char c;
  int T, N, i, j;

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
  for (i = 0; i < T; i++)
  {
    out << "Case #" << i + 1 << ": ";
    combined.clear();
    opposed.clear();
    v.clear();
    in >> N;
    for (j = 0; j < N; j++)
    {
      in >> s;
      if (s.length() != 3)
      {
        cerr << "Error in input" << endl;
        return 1;
      }
      if (s[0] < s[1])
      {
        cp.first = s[0];
        cp.second = s[1];
      }
      else
      {
        cp.first = s[1];
        cp.second = s[0];
      }
      combined[cp] = s[2];
    }
    in >> N;
    for (j = 0; j < N; j++)
    {
      in >> s;
      if (s.length() != 2)
      {
        cerr << "Error in input" << endl;
        return 1;
      }
      opposed[s[0]] = s[1];
      opposed[s[1]] = s[0];
    }
    in >> N >> s;
    for (j = 0; j < N; j++)
    {
      if (v.empty())
      {
        v.push_back(s[j]);
        continue;
      }
      c = s[j];
      if (c < v.back())
      {
        cp.first = c;
        cp.second = v.back();
      }
      else
      {
        cp.first = v.back();
        cp.second = c;
      }
      cit = combined.find(cp);
      if (cit != combined.end())
      {
        v.pop_back();
        v.push_back(cit->second);
      }
      else
      {
        oit = opposed.find(c);
        if (oit != opposed.end())
        {
          for (vit = v.begin(); vit != v.end(); vit++)
            if (*vit == oit->second)
            {
              v.clear();
              c = 0;
              break;
            }
        }
        if (c)
          v.push_back(c);
      }
    }
    out << "[";
    c = 0;
    for (vit = v.begin(); vit != v.end(); vit++)
    {
      if (!c)
      {
        out << *vit;
        c++;
      }
      else
        out << ", " << *vit;
    }
    out << "]" << endl;
  }

  return 0;
}

