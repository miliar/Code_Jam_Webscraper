#include <iostream>
#include <algorithm>

using namespace std;

bool check(int x, int p){
  return x >= p * 3 - min(1, p) * 2;
}

bool check_surprising(int x, int p){
  return x >= p * 3 - min(p, 2) * 2;
}

int main(){
  ios_base::sync_with_stdio(0);
  int tests;
  cin >> tests;
  for(int test = 1; test <= tests; ++test){
    int n, s, p;
    cin >> n >> s >> p;
    int arr[n];
    for(int i = 0; i < n; ++i)
      cin >> arr[i];
    sort(arr, arr + n);
    int ans = 0;
    for(int i = 0; i < n; ++i){
      if(s > 0){
	if(check_surprising(arr[i], p)){
	  ++ans;
	  --s;
	  continue;
	}
      }
      if(check(arr[i], p))
	++ans;
    }
    cout << "Case #" << test << ": " << ans << endl;
  }
}
