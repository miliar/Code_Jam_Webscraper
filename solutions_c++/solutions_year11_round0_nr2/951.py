#include <sstream>
#include <cstdio>
#include <cstring>
#include <string>
#include <iostream>
#include <algorithm>
#include <vector>
#include <bitset>
#include <set>
#include <deque>
#include <boost/unordered_map.hpp>
#include <boost/unordered_set.hpp>

using namespace std;
#define AUTO(a, b) typeof(b) a = (b)

typedef unsigned long long ull;
typedef unsigned uint;

boost::unordered_map<pair<char,char>, char>  mix;
unsigned opp[26];

string solve(string const& s)
{
  ostringstream ss;
  ss << '[';
  
  vector<char> st;
  for( int i = 0, n = s.size(); i != n; ++i )
  {
    st.push_back(s[i]);
    
    while( st.size() >= 2 )
    {
      pair<char,char> p(st[st.size()-1], st[st.size()-2]);
      AUTO(it, mix.find(p));
      if( it == mix.end() )
        break;
      st.pop_back();
      st.back() = it->second;
    }
    if( st.size() >= 2 )
    {
      int x = st.back()-'A';
      for( int j = 0; j+1 != st.size(); ++j )
        if( opp[x] & (1<<(st[j]-'A')) )
        {
          st.clear();
          break;
        }
    }
  }
  if( !st.empty() )
  {
    ss << st[0];
    for( int i = 1; i != st.size(); ++i )
      ss << ", " << st[i];
  }
  ss << ']';
  return ss.str();
}

int main()
{
  int T;
  cin >> T;
  for( int C = 1; C <= T; C++ )
  {
    mix.clear();
    memset(opp, 0, sizeof(opp));
   
    int m;
    cin >> m;

    string tmp;
    for( int i = 0; i != m; ++i )
    {
      cin >> tmp;
      pair<char,char> p(tmp[0], tmp[1]);
      mix.insert(make_pair(p, tmp[2]));
      swap(p.first, p.second);
      mix.insert(make_pair(p, tmp[2]));
    }
    
    cin >> m;
    for( int i = 0; i != m; ++i )
    {
      cin >> tmp;
      opp[tmp[0]-'A'] |= (1<<(tmp[1]-'A'));
      opp[tmp[1]-'A'] |= (1<<(tmp[0]-'A'));
    }
    
    cin >> m >> tmp;
    cout << "Case #" << C << ": " << solve(tmp) << '\n';
  }
  return 0;
}