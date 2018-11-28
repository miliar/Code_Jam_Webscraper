#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
using namespace std;

//string str1 = "ynficwlbkuomxsev.pdrjgtha.";
//string str2 = "abcdefghijklmnopqrstuvwxyz";

string str1 = "abcdefghijklmnopqrstuvwxyz";
//string str2 = "yhesocvxduiglbkr.tnwjpfma."; //q,z
string str2 = "yhesocvxduiglbkrztnwjpfmaq";

int main(){
  int T;
  cin >> T;
  char ch[200];
  getchar();
  for (int testCase = 1; testCase<=T; testCase++){
    int ans;
    scanf("%[^\n]",ch);
    getchar();
    for (int i=0; ch[i]; i++){
      if (ch[i] == ' ') continue;
      ch[i] = str2[ch[i] - 'a'];
    }
    printf ("Case #%d: %s\n",testCase,ch);
  }
}
