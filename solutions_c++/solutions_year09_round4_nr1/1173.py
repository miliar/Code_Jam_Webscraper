#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <climits>

using namespace std;

bool test(const std::vector<int>& v) {
  for(size_t i = 0 ; i < v.size() ; i++ ) {
    if(int(i+1) < v[i]) { return false;}
  }
  return true;
}

int main() {
  int T;
  cin >> T;
  for(int i = 0 ; i <T ; i++ ) {
    int N;
    cin >> N;
    string line;
    getline(cin, line);

    std::vector<int> v;
    for(int y = 0 ; y < N; y++ ){
      getline(cin, line);
      string::size_type r = line.rfind('1');
      if(r == string::npos) {
        r = 0;
      } else {
        r = r+1;
      }
      //cerr << r << endl;
      v.push_back(r);
    }
    
    int result = 0;

    std::set<std::vector<int> > c;
    std::vector<std::vector<int> > q;
    std::vector<std::vector<int> > qq;
    q.push_back(v);

    while(!q.empty()) {
      for(size_t j = 0 ; j < q.size() ; j++ ) {
        const vector<int>& vv = q[j];
        if(test(vv)) {
          goto solve;
        }

        for(size_t j = 0 ; j < vv.size()-1; j++ ) {
          std::vector<int> vvv = vv;
          std::swap(vvv[j],vvv[j+1]);
          if(c.find(vvv) != c.end()) { continue; }
          c.insert(vvv);
          qq.push_back(vvv);
        }
      }

      q.swap(qq);
      qq.clear();
      result++;
    }

 solve:
    cout << "Case #" << i+1 << ": " << result << endl;
  }
}

