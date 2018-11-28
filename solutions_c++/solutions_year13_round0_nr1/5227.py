//In the Name of God
#include <iostream>
#include <vector>
#include <cstring>
#include <string>

using namespace std;

int t;
string s[4];

int f(string s){
  int x = 0 , o = 0;
  for(int i = 0 ; i < 4 ; i ++)
    if(s[i] == '.')
      return -1;
    else if(s[i] == 'X')
      x++;
    else if(s[i] == 'O')
      o++;
    else{
      x++;
      o++;
    }
  if(x == 4)
    return 1;
  else if(o == 4)
    return 2;
  return -1;
}

bool out(int res){
  if(res == -1)
    return false;
  else if(res == 1)
    cout << "X won" << endl;
  else if(res == 2)
    cout << "O won" << endl;
  return true;
}

void func(){
  for(int i = 0 ; i < 4 ; i++){
    int res = f(s[i]);
    if(out(res))
      return ;
  }
  for(int i = 0 ; i < 4 ; i++){
    string s1 = "";
    for(int j = 0 ; j < 4 ; j++)
      s1.push_back(s[j][i]);
    int res = f(s1);
    if(out(res))
      return ;
  }
  string s1 = "";
  for(int i = 0 ; i < 4 ; i++)
    s1.push_back(s[i][i]);
  int res = f(s1);
  if(out(res))
    return ;
  s1 = "";
  for(int i = 0 ; i < 4 ; i++)
    s1.push_back(s[i][3 - i]);
  res = f(s1);
  if(out(res))
    return ;
  for(int i = 0 ; i < 4 ; i++)
    for(int j = 0 ; j < 4 ; j++)
      if(s[i][j] == '.'){
	cout << "Game has not completed" << endl;
	return ;
      }
  cout << "Draw" << endl;
}  

int main(){
  cin >> t;
  for(int z = 0 ; z < t ; z++){
    for(int i = 0 ; i < 4 ; i++)
      cin >> s[i];
    cout << "Case #" << z + 1 << ": ";
    func();
  }
  return 0;
}
