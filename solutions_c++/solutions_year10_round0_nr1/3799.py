#include <vector>
#include <algorithm>
//#include <iostream>
#include <map>
#include <cmath>
#include <set>
#include <sstream>
#include <fstream>

using namespace std;

ifstream cin("A-large.in");
ofstream cout("out.txt");

int main() {
  int T, N, K;
  cin >> T;
  for(int i = 0; i < T; i++) {
    cin >> N >> K;
    cout << "Case #" << i+1 << ": ";
    if((K+1)%(1<<N) == 0)
      cout << "ON";
    else
      cout << "OFF";
    cout << endl;
  }
}