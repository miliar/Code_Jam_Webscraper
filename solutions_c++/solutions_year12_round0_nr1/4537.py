#include <algorithm>
#include <bitset>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>
using namespace std;

string googlerese = "yhesocvxduiglbkrztnwjpfmaq";

void solve(void){
  string input;
  getline(cin, input);
  for(int i=0; i<input.size(); i++){
    if(input[i] == ' '){
      cout << ' ';
    }else{
      cout << googlerese[input[i]-'a'];
    }
  }
  cout << endl;  
}

int main(void){
  int testCaseCount;
  cin >> testCaseCount;
  cin.ignore();
  for(int i=1; i<=testCaseCount; i++){
    cout << "Case #" << i << ": ";
    solve();
  }
  return 0;
}
