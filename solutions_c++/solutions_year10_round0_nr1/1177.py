#include<iostream>
using namespace std;

int main(){

  int T;
  cin >> T;
  for(int t = 1; t <= T; t++){
    int N, K;
    cin >> N >> K;
    cout << "Case #" << t << ": "
	 << ((((1<<N)-1) & K) == ((1<<N)-1) ? "ON" : "OFF") << endl;
  }

  return 0;
}
