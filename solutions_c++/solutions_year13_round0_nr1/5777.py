#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;
string s,ss;

bool check(int a,int b,int c,int d,char e){
  return (s[a] == s[b] && s[b] == s[c] && s[c] == s[d] && s[c] == e);
}

vector<int> v;
int main(void){
  int x,o,t;
  int c;
  cin >> t;
  for(int k = 1; k <= t; k++){
    x = o = c = 0;
    s = "";
    v.clear();
    for(int i = 0; i < 4; i++){
      cin >> ss;
      s += ss;
    }
    for(int i = 0; i < (int)s.size(); i++){
      if(s[i] == 'T'){
	v.push_back(i);
	s[i] = 'X';
      }
      if(s[i] == '.') c++;
    }

    if(check(0,1,2,3,'X')) x++;
    if(check(4,5,6,7,'X')) x++;
    if(check(8,9,10,11,'X')) x++;
    if(check(12,13,14,15,'X')) x++;
    if(check(0,4,8,12,'X')) x++;
    if(check(1,5,9,13,'X')) x++;
    if(check(2,6,10,14,'X')) x++;
    if(check(3,7,11,15,'X')) x++;
    if(check(0,5,10,15,'X')) x++;
    if(check(3,6,9,12,'X')) x++;

    for(int i = 0; i < (int)v.size(); i++) s[v[i]] = 'O';

    if(check(0,1,2,3,'O')) o++;
    if(check(4,5,6,7,'O')) o++;
    if(check(8,9,10,11,'O')) o++;
    if(check(12,13,14,15,'O')) o++;
    if(check(0,4,8,12,'O')) o++;
    if(check(1,5,9,13,'O')) o++;
    if(check(2,6,10,14,'O')) o++;
    if(check(3,7,11,15,'O')) o++;
    if(check(0,5,10,15,'O')) o++;
    if(check(3,6,9,12,'O')) o++;

    cout << "Case #" << k << ": ";
    if(!o && !x){
      if(c) cout << "Game has not completed" << endl;
      else cout << "Draw" << endl;
    }else if(o == x) cout << "Draw" << endl;
    else if(o < x) cout << "X won" << endl;
    else if(o > x) cout << "O won" << endl;
  }
}
