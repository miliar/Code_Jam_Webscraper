#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <climits>
#include <cstdio>
using namespace std;

#define for_(_i, _n) for (int _i = 0; _i < _n; _i++)
#define for_it(_it, _ctr) for (_it = _ctr.begin(); _it != _ctr.end(); _it++)
#define for_itt(_it, _ctr, _type) for (_type::iterator _it = _ctr.begin(); _it != _ctr.end(); _it++)
#define for_rit(_rit, _ctr) for (_rit = _ctr.rbegin(); _rit != _ctr.rend(); _rit++)
#define for_ritt(_rit, _ctr, _type) for (_type::reverse_iterator _rit = _ctr.rbegin(); _rit != _ctr.rend(); _rit++)
#define output(_icase, _result) cout << "Case #" << (_icase + 1) << ": " << _result << endl

ifstream is;

void init(int argc, char *argv[])
{
  is.open((argc > 1)? argv[1]: "test.in");
  if (!is.good())
  {
    cerr << "Input file error\n";
    exit(1);
  }
}

int read_i(int *v1 = 0, int *v2 = 0, int *v3 = 0)
{
  int val;
  string str;
  getline(is, str);
  stringstream ss(str);
  ss >> val;
  if (v1)
    *v1 = val;
  if (v2)
    ss >> *v2;
  if (v3)
    ss >> *v3;
  return val;
}

void read_ia(int *a, int n)
{
  string str;
  getline(is, str);
  stringstream ss(str);
  for_(i,n)
  {
    ss >> a[i];
  }
}

string &read_s(string &str)
{
  getline(is, str);
  return str;
}

string read_s()
{
  string str;
  getline(is, str);
  return str;
}

void process_case(int id)
{
   string line;
  read_s(line);
  stringstream ss(line);

  char ch;
  int N, po, pb, to, tb, pos, steps, total, add;
  po = pb = 1;
  to = tb = 0;
  total = 0;
  ss >> N;
  for_(i,N) {
    ss >> ch;
    ss >> pos;
    if (ch == 'O')
    {
      steps = abs(po - pos) + 1;
      add = (tb >= steps)? 1: steps - tb;
      to += add;
      total += add;
      tb = 0;
      po = pos;
    }
    else
    {
      steps = abs(pb - pos) + 1;
      add = (to >= steps)? 1: steps - to;
      tb += add;
      total += add;
      to = 0;
      pb = pos;
    }
  }
  output(id, total);
}


int main(int argc, char *argv[])
{ 
  init(argc, argv);

  int T = read_i();
  for_(i,T)
  {
    process_case(i);
  }
  
  return 0;
}

