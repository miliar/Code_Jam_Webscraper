#include <iostream>
#include <cstdlib>
#include <algorithm>
using namespace std;

void solve(int caseno){
  int k;
  cin >> k;
  long long *x = new long long[k], *y = new long long[k];
  for(int i=0; i<k; ++i){
    cin >> x[i];
  }
  for(int i=0; i<k; ++i){
    cin >> y[i];
  }
  sort(x,x+k);
  sort(y,y+k);
  //int negsx = 0;
  long long ttl = 0;
  /*
  while(negsx < k && x[negsx] < 0 && y[k-1-negsx] > 0){
    ttl += x[negsx]*y[k-1-negsx];
    negsx++;
  }
  int posx = k-1;
  while(x[posx] > 0 && y[k-1-posx] < 0){
    ttl += x[posx]*y[k-1-posx];
    --posx;
  }
  for(int i
  */
  for(int i=0; i<k; ++i){
    ttl+= x[i]*y[k-1-i];
  }
 
  printf("Case #%d: ",caseno);
  cout << ttl << endl;
}

int main(){
  int n;
  cin >> n;
  for (int i=0; i<n; ++i)
    solve(i+1);
  return 0;
}
