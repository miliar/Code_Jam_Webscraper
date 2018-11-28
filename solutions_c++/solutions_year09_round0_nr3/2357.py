#include <iostream>
#include <cstdio>
using namespace std;

long long ans;
string ptt = "welcome to code jam";
string str;

void calc(int si, int pi){
  if(si >= str.length()) return;
  if(pi == ptt.length()){ ans++; return; }
  for(int i=si; i<str.length(); i++){
    if(str[i]==ptt[pi])
      calc(i, pi+1);
  }
}

void print(int it){
  cout << it/1000; it -= it/1000*1000;
  cout << it/100;  it -= it/100*100;
  cout << it/10;   it -= it/10*10;
  cout << it;
}

int main(){
  int N;
  char c;
  cin >> N;
  c = cin.get();
  for(int i=0; i<N; i++){
    getline(cin, str);
    ans = 0;
    calc(0, 0);
    cout << "Case #" << i+1 << ": ";
    print((int)(ans%10000));
    cout << endl;
  }
  return 0;
}
