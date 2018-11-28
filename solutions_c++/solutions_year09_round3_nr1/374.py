#include <iostream>
#include <vector>
#include <sstream>
#include <iomanip>
#include <map>
#include <set>

using namespace std;

void skipws(std::istream& is) {
  char c;
  for(;;) {
    if(!is.get(c)) {
      return;
    }
    if(!isspace(c)) {
      is.unget();
      return;
    }
  }
}

int main() {
  int T;
  cin >> T;
  string line;
  getline(cin, line);

  for(int i = 0 ; i< T; i++ ) {
    getline(cin, line);
    //line.erase(line.end()-1);

    set<char> s;
    for( size_t j = 0 ; j < line.size() ; j++ ) {
      s.insert(line[j]);
    }

    size_t base = s.size();
    //cerr << base << endl;

    if( base == 1 ) {
      int m = 0;
      for(size_t j = 0 ; j < line.length() ; j++ ) {
        m *= 2;
        m += 1;
      }
      cout << "Case #" << i+1 << ": " << m << endl;
      continue;
    }

    map<char,int> d;
    int k = 0;
    for(set<char>::iterator j = s.begin() ; j != s.end() ; j++ ) {
      d[*j] = k++;
      //cerr << *j << "= " << d[*j] << std::endl;
    }

    vector<int> v;
    for(size_t j = 0 ; j < base ; j++ ) {
      v.push_back(j);
    }

    long long mx = LONG_LONG_MAX;
    do  {
#if 0
      cerr << "p ";
      for(size_t j = 0 ; j < v.size() ; j++ ) {
        cerr << v[j] << ", ";
      }
      cerr << endl;
#endif      
      if(v[d[line[0]]] == 0) { continue; }

      long long m = 0;
      for(size_t k = 0 ; k < line.size() ; k++ ) {
        char c = line[k];
        int n = v[d[c]];
        //cerr << "n: " << n << endl;
        m *= base;
        m += n;
      }
      //cerr << m << std::endl;
      if( m < mx ) { mx = m; }
    } while(next_permutation(v.begin(),v.end()));

#if 1
    cout << "Case #" << i+1 << ": " << mx << endl;
#endif
  }

  return 0;
}
