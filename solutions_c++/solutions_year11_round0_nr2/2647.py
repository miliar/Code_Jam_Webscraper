#include <iostream>
#include <sstream>
#include <map>
#include <utility>

using namespace std;

// ./a.out < XXX.in.txt > XXX.out.txt

int main() {
  // read in the number of test cases
  int T;
  cin >> T;
  cin.get();

  // read in data for test cases
  for(int test=1; test<=T; test++) {
    char str[1000];
    stringstream ss;
    cin.getline(str, 1000);
    ss << str;

    int C;
    ss >> C;
    map< char, char > cbase;
    map< pair<char, char>, char > combine;
    for (int i=0; i<C; i++) {
      string c;
      ss >> c;
      pair<char, char> base(c[0], c[1]);
      combine[base] = c[2];
      pair<char, char> base1(c[1], c[0]);
      combine[base1] = c[2];
      cbase[c[0]] = c[1];
      cbase[c[1]] = c[0];
    }
    int D;
    ss >> D;
    map< char, char > opposite;
    for (int i=0; i<D; i++) {
      string c;
      ss >> c;
      opposite[c[0]] = c[1];
      opposite[c[1]] = c[0];
    }
    int N;  ss >> N;
    string invoke, res;
    ss >> invoke;
    res += invoke[0];
    for (int i=1; i<N; i++) {
      map< char, char >::iterator it;
      it = cbase.find(invoke[i]);
      string::reverse_iterator rit = res.rbegin();
      if( it!=cbase.end() && it->second == *rit ) {
        *rit = combine[make_pair(invoke[i], *rit)];
        continue;
      }
      it = opposite.find(invoke[i]);
      if( it!=opposite.end() && res.find(it->second)!=-1 ) { res.clear(); continue; }
      res += invoke[i];
    }

    cout << "Case #" << test << ": [";
    int i=0;
    for (; i+1<res.length(); i++) {
      cout << res[i] << ", ";
    }
    if(i<res.length()) cout << res[i];
    cout << "]" << endl;
  }

  return 0;
}

