#include <iostream>
#include <algorithm>
using namespace std;

void calc(string str){
  str = "0" + str;
  next_permutation(str.begin(), str.end());
  if(str[0] == '0'){
    for(int i=1; i<str.length(); i++) cout << str[i];
    cout << endl;
    return;
  }else{
    cout << str << endl;
  }
}

int main(){
  int T;
  string N;
  cin >> T;
  for(int i=0; i<T; i++){
    cin >> N;
    cout << "Case #" << i+1 << ": ";
    calc(N);
  }
  return 0;
}
