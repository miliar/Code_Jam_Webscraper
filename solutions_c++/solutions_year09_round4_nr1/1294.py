#include <string>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> read_data()
{
  int N;
  cin >> N;
  vector<int> v;
  for ( int n=0; n<N; ++n )
  {
    string line;
    cin >> line;
    int vv = 0, p = line.length() - 1;
    while ( p >= 0 and line[p] == '0' )
    {
      ++vv; --p;
    }
    v.push_back(p + 1);
  }
  return v;
}

int bads(const vector<int> &dst)
{
  int N = dst.size();
  int b = 0;
  for ( int i=0; i < N; ++i )
    for ( int j=i + 1; j<N; ++j )
      if ( dst[i] > dst[j] )
        ++b;
  return b;
}

bool good(const vector<int> &d, const vector<int> &p)
{
  int N = d.size();
  for ( int i=0; i<N; ++i )
    if ( d[p[i]] > i + 1 )
      return false;
  return true;
}

int best(const vector<int> &d)
{
  int N = d.size();
  vector<int> p(N);
  for ( int i=0; i<N; ++i )
    p[i] = i;
  int best = 1000000000;
  do
  {
    if ( good(d, p) )
      best = min(best, bads(p));
  } while ( next_permutation(p.begin(), p.end()) );
  return best;
}



int main()
{
  int T;
  cin >> T;
  for ( int t=1; t<=T; ++t )
  {
    vector<int> v = read_data();
    cout << "Case #" << t << ": " << best(v) << endl;
  }
  return 0;
}
