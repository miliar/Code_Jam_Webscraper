#include<iostream>
#include<cstdio>
#include<sstream>
#include<vector>
#include<map>
#include<cassert>
#include<set>
#include<iomanip>
#include<queue>


using namespace std;

void swap(int& a, int& b){
  int t = a;
  a = b;
  b = t;
}

int solve(vector<int>& a){
  const int N = a.size();
  int cnt = 0;
  for(int i=0;i<N;++i){
    int pos;
    for(pos=i;pos<N;++pos){
      if(a[pos] <= i+1){
	break;
      }
    }
    assert(pos != N);
    //    cout << a[pos] << " " << (i+1) << endl;

    assert(a[pos] <= i+1);
    cnt += pos-i;
    for(int j=pos;j>i;--j){
      swap(a[j], a[j-1]);
    }
  }

//   for(int i=0;i<N;++i){
//     cout << a[i] << " ";
//   }
//   cout << endl;
  return cnt;
}

int main(){
  int T; cin >> T;
  for(int t=0;t<T;++t){
    int N; cin >> N;
    vector<int> a(N);
    for(int i=0;i<N;++i){
      string line; cin >> line;
      assert(N == line.size());
      int j;
      for(j=0;j<N;++j){
	if(line[line.size()-j-1] != '0') break;
      }
      a[i] = N-j;
      //      cout << a[i] << endl;
    }
    cout << "Case #" << (t+1) << ": " << solve(a) << endl;

  }
}
