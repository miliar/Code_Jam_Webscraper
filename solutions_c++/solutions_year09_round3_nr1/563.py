#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <map>
#include <algorithm>
#include <iterator>
#include <cstring>
using namespace std;

#define all(v) (v).begin(), (v).end()
typedef unsigned long long ll;
bool ar[36];


ll getMinTime(const string &s)
{
  memset(ar, 0, 36);
  map<char, int> mci;
  vector<int> vi;
  vi.push_back(1);
  vi.push_back(0);
  for (int i = 2; i <=40; i++)
    vi.push_back(i);
  
  int c = 0;
  for (int i = 0; i< s.size(); i++) {
    if (s[i] >= '0' && s[i] <= '9' && ar[s[i] -'0'] == false) {
      mci[s[i] ] = vi[c++];
      ar[s[i] - '0' ] = true;
    } else if (s[i] >= 'a' && s[i] <= 'z' && ar[s[i] - 'a'+10 ] == false) {
      mci[s[i] ] = vi[c++];
      ar[s[i] - 'a' +10] = true;
    }
  }

  ll sum = 0;
  if (c <= 1) ++c;
  for (int i = 0; i < s.size(); i++) {
    sum = sum*c+ mci[s[i] ];
  }

  return sum;
}

int main(int argc, char **argv)
{
  if (argc < 2) {
    cerr  << "Usage: " << argv[0] << " <input file>\n";
    return 1;
  }
  ifstream fin(argv[1]);
  if (!fin) {
    cerr << "Could not open file " << argv[1] << endl;
    return 1;
  }
  int test;
  fin >> test;
  for (int i = 0; i < test; i++) {
    string s;
    fin >> s;
    cout <<"Case #" << i+1 << ": " << getMinTime(s) << endl;
  }
  fin.close();

  return 0;
}
  
