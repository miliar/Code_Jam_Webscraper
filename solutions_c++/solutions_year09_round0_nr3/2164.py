#include<iostream>
#include<string>
using namespace std;
int arr[600][25];
string t = "welcome to code jam.";
int main() {
  int N;
  cin >> N;cin.ignore();
  for (int n = 1; n <= N; ++n) {
    for (int i =0; i < 600; ++i) for (int j = 0; j < 25; ++j) arr[i][j] = 0;
    arr[0][0] = 1;
    string s;
    getline(cin, s);s+='.';
    int ans = 0;
    for (int i = 1; i <= s.length(); ++i)
      for (int j = 0; j < i; ++j)
        for (int k = 0; k < t.length(); ++k) 
          if (arr[j][k] && (!j || !k || s[j-1] == t[k-1]) && s[i-1] == t[k])  
             arr[i][k+1] = (arr[i][k+1]+ arr[j][k])%10000;

    cout<<"Case #"<<n<<": ";
    int x = arr[s.length()][t.length()];
    if (x < 1000) cout<<"0";
    if (x < 100) cout<<"0";
    if (x < 10) cout<<"0";
    cout<<x<<endl;
  }
  return 0;
}