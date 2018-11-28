#include<iostream>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<algorithm>
#include<cmath>

using namespace std;


int main(){
  int T; cin >> T;
  for(int t=0;t<T;++t){
    int N; cin >> N;
    vector<int> a(N), b(N);
    for(int i=0;i<N;++i)
      cin >> a[i];
    for(int i=0;i<N;++i)
      cin >> b[i];

    sort(a.begin(), a.end());
    sort(b.rbegin(), b.rend());
    long long prod = 0LL;
    for(int i=0;i<N;++i){
      prod += a[i]*(long long)b[i];
    }
    cout << "Case #" << (t+1) << ": " << prod << endl;
    
  }
}
