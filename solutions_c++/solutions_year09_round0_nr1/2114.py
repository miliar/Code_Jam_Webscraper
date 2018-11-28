#include<iostream>
#include<string>
#include<vector>
using namespace std;
vector<string> v;
string s;
int L, D, N;
int match(int i, int k, int t) {
  if (k == L) return 1;
  int t2;
  if (s[t] != '(') {
    if (s[t] == v[i][k]) return match(i, k+1, t+1);
    else return 0;
  } 
  for (t2 = t; s[t2]!=')';t2++);
  for (int j = t+1; j < t2; ++j)
    if (s[j] == v[i][k])
      return match(i, k+1, t2+1);
  return 0;
}

int main() {
  cin>>L>>D>>N;
  while (D--) {
    cin>>s;
    v.push_back(s);
  }
  int j = 0;
  while (N--) {
    cin>>s;
    int cnt = 0;
    for (int i = 0; i < v.size(); ++i)
      cnt += match(i, 0, 0);
    cout<<"Case #"<<(++j)<<": "<<cnt<<endl;
  }
  return 0;
}