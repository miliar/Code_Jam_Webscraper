#include <iostream>
#include <string>
#include <vector>
#include <cstring>
#include <cstdio>

using namespace std;

const string welcome = "welcome to code jam";
string line;
int dp[510][20];

int check(int pos1,int pos2) {
  if (line[pos1]!=welcome[pos2])
    return 0;
  if (pos2==(welcome.size()-1))
    return 1;
  if (dp[pos1][pos2]!=-1)
    return dp[pos1][pos2];
  int all = 0;
  for(int i=pos1+1;i<line.size();i++) {
    all += check(i,pos2+1);
  }
  dp[pos1][pos2] = all%10000;
  return all;
}

string ans() {
  int all = 0;
  for(int i=0;i<line.size();i++)
    all += check(i,0);
  char c[10];
  sprintf(c,"%d",all);
  string str(c);
  if (str.length()>4) {
    str = str.substr(str.length()-4,4);
  }
  while(str.length()<4)
    str = "0" + str;
  return str;
}

int main() {
  int T;
  cin >> T;
  cin.get();
  for(int t=1;t<=T;t++) {
    char l[500];
    cin.getline(l,500);
    line = string(l);
    memset(dp,-1,sizeof(dp));
    cout << "Case #" << t << ": " << ans() << endl;
  }
  return 0;
}
