#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <climits>

using namespace std;

int check(vector<int> a1, vector<int> a2){
  if(a1.size() == 0 || a2.size() == 0) return -1;
  int sum1 = 0, sum2 = 0;
  for(int i = 0; i < a1.size(); i++){
    sum1 = sum1 ^ a1[i];
  }

  
  for(int i = 0; i < a2.size(); i++){
    sum2 = sum2 ^ a2[i];
  }

  if(sum1 == sum2){
    int sum3 = 0;
    for(int i = 0; i < a1.size(); i++){
      sum3 += a1[i];
    }
    return sum3;
  } else {
    return -1;
  }
}

int solve(vector<int> v, vector<int> a1 = vector<int>(), vector<int> a2 = vector<int>()){
  if(v.size() == 0)
    return check(a1, a2);
  

  int val = v.back();
  v.pop_back();

  a1.push_back(val);
  int r1 = solve(v, a1, a2);
  a1.pop_back();
  
  a2.push_back(val);
  int r2 = solve(v, a1, a2);
  a2.pop_back();

  return r1 > r2 ? r1 : r2;
}

int main() {
  int t;
  cin >> t;
  for(int i = 0; i < t; i++){
    vector<int> v;
    int n;
    cin >> n;
    while(n--){
      int tmp;
      cin >> tmp;
      v.push_back(tmp);
    }

    int ret = solve(v);
    cout << "Case #" << (i+1) << ": ";
    if(ret == -1){
      cout << "NO";
    }else{
      cout << ret;
    }
    cout << endl;
  }
}

