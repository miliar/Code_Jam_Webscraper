#include<iostream>
#include<string>
#include<algorithm>
using namespace std;

int main() {
  int N; cin>>N; string s;
for (int k = 1; k <= N; ++k) {
  cout<<"Case #"<<k<<": ";
  cin>>s;
  for (int i = 0; i < s.length(); ++i) {
    int j; int l=i;
    for (j = i+1; j < s.length(); ++j)
    if (s[j] > s[j-1]) break; else if (i && s[j] > s[i-1]) l = j;
    if (j != s.length()) continue; 
    if (i == 0) {
       s += '0';
       sort(s.begin(), s.end()); for (j = 0; j < s.length(); ++j)
       if (s[j] != '0') {swap(s[j], s[0]); break;} cout<<s<<endl;
    } else {
       swap(s[l], s[i-1]); sort(s.begin() + i, s.end());
       cout<<s<<endl;
    }
    break;
  }
}
  return 0;
}
