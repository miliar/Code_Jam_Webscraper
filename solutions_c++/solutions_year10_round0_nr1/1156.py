#include <iostream>
#include <string>
#include <sstream>
#include <set>
#include <iostream>

using namespace std;

int getint(string s){
  istringstream iss(s);
  int i;
  iss >> i;
  return i;
}

int pow(int num, int power){
  int res = 1;
  for(int i=0;i<power;++i){
    res *= num;
  }
  return res;
}

int main()
{
  string line;
  int T;
  getline(cin, line);
  T = getint(line);

  for(int i=0;i<T;i++){
    set<int> s;
    int N,K;
    getline(cin, line);
    istringstream iss(line);
    iss >> N;
    iss >> K;
    int p = 2 << (N-1);
    
    string res = (K % p == p-1) ? "ON": "OFF";
    cout << "Case #" << i+1 << ": " << res << endl;    
  }
  return 0;
}
