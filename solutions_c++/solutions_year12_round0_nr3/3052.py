#include <iostream>
#include <sstream>

using namespace std;

long long toNum(string s) { istringstream iss(s); long long t; iss >> t; return t;}
string toString(long long n) { ostringstream oss; oss << n; return oss.str();}

string rotate(string const& start)
{
  string ret;

  for (int i = 1; i < start.size(); i++)
    ret += start[i];
  ret += start[0];

  return ret;
}

int cnt(int n, int hi, int lo)
{
  string start = toString(n);
  string cur   = rotate(start);
  int    ret   = 0;
  
  while (start != cur)
  {
    int tmp = toNum(cur);
    if (tmp >= lo && tmp <= hi)
      ret++;
  
    cur = rotate(cur);
  }

  return ret;
}

int main()
{
  int T, A, B;
  cin >> T;
  
  for (int t = 1; t <= T; t++)
  {
    cin >> A >> B;
    int ans = 0;
    for (int i = A; i <= B; i++)
      ans += cnt(i, B, A);
    
    cout << "Case #" << t << ": " << (ans/2) << endl;
  }

  return 0;
}