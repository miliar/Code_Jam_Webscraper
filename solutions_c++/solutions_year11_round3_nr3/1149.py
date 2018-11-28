#include <iostream>
#include <vector>
#include <string>
#include <utility>
#include <algorithm>

using namespace std;

int solve(int,int,int,const vector<int>&);

int main(){
  int num_cases;
  cin >> num_cases;
  for(int i = 0; i < num_cases; i++){
    int n,l,h;
    cin >> n >> l >> h;
    vector<int> others;
    for(int j = 0; j < n; j++){
      int o;
      cin >> o;
      others.push_back(o);
    }
    int r = solve(n,l,h,others);
    if(r == -1)
      cout << "Case #" << i+1 << ": NO" << endl;
    else
      cout << "Case #" << i+1 << ": " << r << endl;
  }
}

int solve(int n, int l, int h, const vector<int>& others){
  for(int i = l; i <= h; i++){
    bool ok = true;
    for(size_t j = 0; j < others.size(); j++){
      if(others[j] % i != 0 && i % others[j] != 0){
	ok = false; break;
      }
    }
    if(ok) return i;
  }
  return -1;
}
