#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;

int L, D, N;
char word[25];
string input;
vector< vector<int> > vvi;
map<string,bool> m;

int f(int k){
  if(k == L) return m[string(word)]?1:0;
  int ret = 0;
  for(int i = 0; i < (int) vvi[k].size(); ++i){
    word[k] = vvi[k][i];
    word[k+1] = '\0';
    //cerr << string(word) << endl;
    if(m[string(word)]) ret += f(1 + k);
  }
  return ret;
}

int main(){
  cin >> L >> D >> N;
  for(int i = 0; i < D; ++i){
    cin >> input;
    for(int j = 0; j < L; ++j){
      word[j] = input[j];
      word[j+1] = '\0';
      m[string(word)] = true;
    }
  }
  for(int i = 0; i < N; ++i){
    cin >> input;
    vvi.clear();
    int ind = 0;
    vector<int> vi;
    for(int j = 0; j < L; ++j){
      vi.clear();
      if(input[ind] == '('){
        ++ind;
        while(input[ind] != ')'){
          vi.push_back(input[ind]);
          ++ind;
        }
      } else {
        vi.push_back(input[ind]);
      }
      ++ind;
      vvi.push_back(vi);
    }
    cout << "Case #" << 1 + i << ": " << f(0) << endl;
  }
}
