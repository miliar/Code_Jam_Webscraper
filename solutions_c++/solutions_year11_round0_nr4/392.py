#include <iostream>
#include <algorithm>

using namespace std;

int main(){
  int t;
  cin >> t;
  for (int caseCnt=1;caseCnt<=t;++caseCnt){
    cout << "Case #"<<caseCnt<<": ";
    int n;
    int a[1000],b[1000];
    cin >> n;
    for (int i = 0; i< n ; ++i){
      cin >> a[i];
      b[i] = a[i];
    }
    sort(a,a+n);
    int x = 0;
    for (int i = 0; i<n;++i)
      if (a[i]!=b[i])
	++x;
    cout<<x<<".000000\n";
  }
}
