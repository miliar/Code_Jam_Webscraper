/*! g++ -g main.cpp
 */

#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <cstdlib>
#include <map>
#include <algorithm>



using namespace std;

class magicka{
public:
  map<char, pair<char, char> > combine;
  map<char, char> opposed;
  map<char, int> appear;
  vector<char> elem_list;

  magicka(){
    for(char i = 0; i < 26; ++i){
      appear['A' + i] = 0;
    }
  }

  void register_comb(string s){
    combine[s[0]] = pair<char, char>(s[1], s[2]);
    combine[s[1]] = pair<char, char>(s[0], s[2]);
  }

  void register_opposed(string s){
    opposed[s[0]] = s[1];
    opposed[s[1]] = s[0];
  }

  void receive_element(char x){
    if(elem_list.size() > 0){
      if(combine.find(x) != combine.end() && elem_list.back() == combine[x].first){
	appear[elem_list.back()]--;
	elem_list.back() = combine[x].second;
	appear[elem_list.back()]++;
      }
      else if(opposed.find(x) != opposed.end() && appear[opposed[x]] > 0){
	elem_list.clear();
	for(map<char, int>::iterator it = appear.begin(); it != appear.end(); ++it){
	  it->second = 0;
	}
      }
      else{
	elem_list.push_back(x);
	appear[x]++;
      }
    }
    else{
      elem_list.push_back(x);
      appear[x]++;
    }
  }

  ostream& print_list(ostream& os) const {
    os << "[";
    if(elem_list.size() > 0){
      for(size_t i = 0; i < elem_list.size() - 1; ++i){
	os << elem_list[i] << ", ";
      }
      os << elem_list.back();
    }
    return os << "]";
  }
  
  void print_all(){
    cout << "combine" << endl;
    for(map<char, pair<char, char> >::iterator it = combine.begin(); it != combine.end(); ++it){
      cout << it->first << "\t" << it->second.first << "\t" << it->second.second << endl;
    }
    cout << "opposed" << endl;
    for(map<char, char>::iterator it = opposed.begin(); it != opposed.end(); ++it){
      cout << it->first << "\t" << it->second << endl;
    }
    cout << "appear" << endl;
    for(map<char, int>::iterator it = appear.begin(); it != appear.end(); ++it){
      cout << it->first << "\t" << it->second << endl;
    }
    cout << "elem_list" << endl;
    print_list(cout) << endl;
  }
};

ostream& operator<<(ostream& os, const magicka& m){
  return m.print_list(os);
}

void solve(int x){
  magicka mag;
  int c, d, n;
  string buf;
  cin >> c;
  for(int i = 0; i < c; i++){
    cin >> buf;
    mag.register_comb(buf);
  }
  cin >> d;
  for(int i = 0; i < d; ++i){
    cin >> buf;
    mag.register_opposed(buf);
  }
  cin >> n >> buf;
  for(int i = 0; i < n; ++i){
    mag.receive_element(buf[i]);
    //mag.print_all();
  }
  cout << "Case #" << x << ": " << mag << endl;
}

int main(int argc, char *argv[]){
  int n;
  cin >> n;

  for(int i = 0; i < n; ++i){
    solve(i + 1);
  }

  return 0;
}
