#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <cmath>
#include <ext/hash_map>
#include <ext/hash_set>
#include <fstream>
#include <iostream>
using namespace std;

namespace __gnu_cxx
{
        template<> struct hash< std::string >
        {
                size_t operator()( const std::string& x ) const
                {
                        return hash< const char* >()( x.c_str() );
                }
        };
}

using __gnu_cxx::hash_map;

#define sz(a) ((int)a.size())
#define all(a) a.begin(), a.end()

const int INF = (1 << 31) - 1;

template <class T>
void print(const vector<T>& v) {
  for (int i = 0; i< sz(v); ++i)
    cout << v[i] << " ";
  cout << endl;
}

void print(const vector<string>& v) {
  for (int i = 0; i< sz(v); ++i)
    cout << v[i] << endl;
  cout << endl;
}

char mapping[27];
void init() {
  memset(mapping, '-', sizeof(mapping));

  mapping['y' - 'a'] = 'a';
  mapping['e' - 'a'] = 'o';
  mapping['q' - 'a'] = 'z';

  string lhs[] = {
      "ejp mysljylc kd kxveddknmc re jsicpdrysi",
      "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
      "de kr kd eoya kw aej tysr re ujdr lkgc jv"
  };

  string rhs[] = {
      "our language is impossible to understand",
      "there are twenty six factorial possibilities",
      "so it is okay if you want to just give up"
  };

  for (int i = 0; i < 3; ++i) {
    for (int j = 0; j < sz(lhs[i]); ++j) {
      if (lhs[i][j] != ' ')
        mapping[lhs[i][j] - 'a'] = rhs[i][j];
    }
  }

  bool check[26];
  memset(check, false, sizeof(check));

  for (int i = 0; i < 26; ++i) {
    if (mapping[i] != '-') {
      check[mapping[i] - 'a'] = true;
    }
  }

  char c;
  for (int i = 0; i < 26; ++i) {
    if (check[i] == false) {
      c = i + 'a';
    }
  }

  for (int i = 0; i < 26; ++i) {
    if (mapping[i] == '-')
      mapping[i] = c;
  }

//  for (int i = 0; i < 26; ++i)
//    cout << char(i + 'a') << "\t" << mapping[i] << endl;
}

int main() {
  init();
  ifstream in("in.txt");
  ofstream out("out.txt");
  int t;
  in >> t;
cout << t << endl;
  char ip[102];
  in.getline(ip, 101);
  cout << ip << endl;
  for (int i = 0; i < t; ++i) {
    in.getline(ip, 101);
    string ret = "";
    for (int j = 0; j < strlen(ip); ++j) {
      if (ip[j] != ' ') {
        ret += mapping[ip[j] - 'a'];
      } else {
        ret += ' ';
      }
    }
    out << "Case #" << i + 1 << ": " << ret << endl;
  }
  in.close();
  out.close();
	return 0;
}
