#include <iostream>
#include <vector>
#include <string>
#include <utility>
#include <algorithm>

using namespace std;

bool solve(int, int, vector<string>&);

int main(){
  int num_cases;
  cin >> num_cases;
  for(int i = 0; i < num_cases; i++){
    int r,c;
    cin >> r >> c;
    vector<string> pic;
    for(int j = 0; j < r; j++){
      string s;
      cin >> s;
      pic.push_back(s);
    }
    bool ok = solve(r,c,pic);
    cout << "Case #" << i+1 << ":"<< endl;
    if(!ok)
      cout << "Impossible" << endl;
    else {
      for(int j = 0; j < r; j++){
	cout << pic[j] << endl;
      }
    }
  }
}

bool solve(int r, int c, vector<string>& pic){
  for(int i = 0; i < r;){
    size_t p = pic[i].find('#',0);
    if(p == string::npos){i++; continue;}
    else{
      if(p+1 == c) return false;
      if(i+1 == r) return false;
      pic[i][p] = '/';
      if(pic[i][p+1] == '#') pic[i][p+1] = '\\'; else return false;
      if(pic[i+1][p] == '#') pic[i+1][p] = '\\'; else return false;
      if(pic[i+1][p+1] == '#') pic[i+1][p+1] = '/'; else return false;
    }
  }
  return true;
}
