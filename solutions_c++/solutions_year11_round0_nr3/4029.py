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

void read_i(int *a, int n)
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

int N;
int max_val;
int *p1, *p2;

void run(int s1, int x1, int s2, int x2, int level)
{
  if (level > N / 2)
    return;

  int nx1, nx2, ns1, ns2;
  for_(i, N) {
    if (!p1[i])
      continue;
    ns1 = s1 - p1[i];
    nx1 = x1 ^ p1[i];
    p2[i] = p1[i];
    p1[i] = 0;
    ns2 = s2 + p2[i];
    nx2 = x2 ^ p2[i];

    if (nx1 == nx2) {
      int nmax = (s1 > s2)? ns1: ns2;
      if (nmax > max_val)
        max_val = nmax;
    }
    run(ns1, nx1, ns2, nx2, level + 1);
    p1[i] = p2[i];
    p2[i] = 0;
  }
}



void process_case(int id)
{
  N = read_i();
  p1 = new int[N];
  p2 = new int[N];
  int s1 = 0;
  int x1 = 0;
  read_i(p1, N);
  for_(i, N) {
    p2[i] = 0;
    s1 += p1[i];
    x1 ^= p1[i];
  }
  max_val = -1;
  run(s1, x1, 0, 0, 1);
  
  if (max_val > 0)
    output(id, max_val);
  else
    output(id, "NO");
    
  delete [] p1;
  delete [] p2;
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

