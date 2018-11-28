#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main(){
  int T;
  cin >> T;
  for(int tno = 0; tno < T; tno++){
    long long n;
    cin >> n;
    vector<int> v;
    while( n ) {
      v.push_back(n % 10);
      n /= 10;
    }
    v.push_back(0);
    reverse(v.begin(), v.end());
    
    next_permutation(v.begin(), v.end());

    cout << "Case #" << tno + 1 << ": ";
    int start = 0;
    for(int i = 0; i < v.size(); i++){
      if( start == 0 && v[i] ) start = 1;
      if( start ) cout << v[i];
    }
    cout << endl;
  }
}
