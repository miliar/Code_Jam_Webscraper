#include <iostream>
#include <vector>
#include <utility>
#include <string>
#include <algorithm>
#include <numeric>
#include <iomanip>
#include "../../../print.hpp"

using namespace std;

typedef long long ll;


vector<int> b, e, w;

 
bool comp(int i, int j){
  return w[i] < w[j];
}

double  solve(int x, int s, int r, int T,vector<int> & _b, vector<int> & _e,  vector<int> & _w){
  b = _b;e = _e;w = _w;
  double ans = 0;
  int n = w.size();

  vector<int> ind(n + 1);
  for(int i = 0;i <n + 1;i++){
    ind[i] = i;
  }

  vector<int > len(n);
  for(int i = 0;i < n ;i++){
    len[i] = e[i] - b[i];
  }

  int sum = accumulate(len.begin(), len.end(), 0);
  b.push_back(0);
  e.push_back(x - sum);
  w.push_back(0);
  n++;

  sort(ind.begin(), ind.end(), comp);

  //  print (b);
  //print (e);
  //print (w);
  //print (ind);
    

  for(int i = 0;i < n; i++){
    if(ans < T){
      double buf = (e[ind[i]] - b[ind[i]]) / (double)(r + w[ind[i]]);
      if(buf + ans <= T){
	ans += buf;
      }else{
	ans = T + (e[ind[i]] - b[ind[i]] - (T - ans) * (r + w[ind[i]])) /(double) (s + w[ind[i]]);
      }
    }else{
      ans += (e[ind[i]] - b[ind[i]]) / (double)(s + w[ind[i]]);
    }

  }
  

  return ans;
}


int main(){
  int t;cin >> t;
  for(int j = 1;j<=t;j++){
    int x, s, r, T, n;
    cin >> x >> s >> r >> T >> n;
    vector<int> _b(n);
    vector<int> _e(n);
    vector<int >  _w(n);
    for(int i= 0;i < n;i++){
      cin >> _b[i] >> _e[i] >> _w[i];
    }
    double ans = solve(x, s, r, T, _b, _e,_w);

		       
    cout << "Case #" << j << ": " << setprecision(10) <<  ans <<endl;
  }
  return 0;

}
