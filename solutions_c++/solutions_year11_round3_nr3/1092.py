#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>
#define PI 3.14159265358979323846264338327950288
#define MOD 100003
using namespace std;

void cal() {
  int N, L, H;
  cin>>N>>L>>H;
  
  vector<int> note(N);
  for(int i = 0; i < N; i++) cin>>note[i];

  for(int i = L; i <= H; i++) {
    int j;
    for(j = 0; j < N; j++) 
      if ( ( i > note[j] ) ? i % note[j] != 0 : note[j] % i != 0 ) break;

    if ( j == N ) {
      cout<<i;
      return;
    }
  }

  cout<<"NO";

}

int main() {
  
  int T;
  cin>>T;
  for(int i = 1; i <= T; i++) {
    cout<<" Case #"<<i<<": ";
    cal();
    cout<<endl;
  }

  return 0;
}
