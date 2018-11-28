#include <iostream>
#include <map>
#include <list>
#include <vector>
#include <set>

using namespace std;

int main()
{

  int T;
  cin >> T;

  for (int i = 0; i < T; ++i) {
    
    int C;
    cin >> C;
    
    std::map<std::pair<char, char>, char> combine_map;
    for (int j = 0; j < C; ++j) {
      char a, b, c;
      cin >> a >> b >> c;
      combine_map.insert(make_pair(make_pair(a,b), c));
      combine_map.insert(make_pair(make_pair(b,a), c));
    }

    int D;
    cin >> D;
    std::set<std::pair<char, char> > delete_map;
    for (int j = 0; j < D; ++j) {
      char a, b;
      cin >> a >> b;
      delete_map.insert(make_pair(a, b));
      delete_map.insert(make_pair(b, a));
    }
    
    int N;
    cin >> N;
    
    std::vector<char> result;
    for (int j = 0; j < N; ++j) {
      char a;
      cin >> a;

      if (result.empty() == true) {
        result.push_back(a);
        continue;
      }

      std::map<std::pair<char, char>, char>::iterator it = 
        combine_map.find(make_pair(a, result.back()));
      if (it != combine_map.end()) {
        result.back() = it->second;
        continue;
      }

      bool insert = true;
      for (std::vector<char>::iterator itl = result.begin();
           itl != result.end(); ++itl) {
        
        for (std::set<std::pair<char, char> >::iterator its = 
               delete_map.begin();
             its != delete_map.end(); ++its) {
          if (its->first == a && its->second == *itl) {
            insert = false;
            break;
          }
        }
        if (insert == false)
          break;
      }

      if (insert == false) {
        result.clear();
      } else {
        result.push_back(a);
      }
    }

    cout << "Case #" << i+1 << ": [";
    if (result.empty() == false) {
      for (int it = 0; it < result.size() - 1; ++it) {
        cout << result[it] << ", ";
      }
      cout << result.back();
    }
    cout << "]" << endl;
  }
  
  return 0;
}
