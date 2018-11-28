#include <iostream>
#include <set>

using namespace std;

int dig[10] = {1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000};
set<pair<int, int> > S;

bool isOK(int num, int slide, int digit, int limit){
  int t = (num % dig[slide]) * dig[digit - slide] + (int)(num / dig[slide]);
  //cout << "slide:" << slide << ", digit: " << digit << ", num:" << num << ", t:" << t << ", isOK: " << (int)((t >= dig[digit - 1]) && (num < t) && (t < limit)) << endl;
  //return (t >= dig[digit - 1]) && (num < t) && (t < limit) && !S.count(make_pair(num, t));
  //if((t >= dig[digit - 1]) && (num < t) && (t < limit) && !S.count(make_pair(num, t))){
  if((num < t) && (t <= limit) && !S.count(make_pair(num, t))){
    S.insert(make_pair(num, t));
    return 1;
  }
  return 0;
}

int getDigit(int num){
  if(num == 0) return 1;
  int cnt = 0;
  while(num) cnt++, num /= 10;
  return cnt;
}

int main(){
  int T;
  while(cin >> T && T){
    int a, b, digits;
    for(int i = 1; i <= T; i++){
      cin >> a >> b;
      
      digits = getDigit(a);

      int ans = 0;
      S.clear();

      for(int j = a; j <= b; j++)
	for(int k = 1; k < digits; k++)
	  if(isOK(j, k, digits, b)) ans++;

      cout << "Case #" << i << ": " << ans << endl;
    }
  }
  return 0;
}
