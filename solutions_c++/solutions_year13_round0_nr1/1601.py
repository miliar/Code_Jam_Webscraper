#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<algorithm>
#include<map>
#include<vector>
#include<deque>
using namespace std;
bool Win(string s[],char c){
  int cnt1,cnt2=0;
  for(int i=0;i<4;i++){
    cnt1=cnt2=0;
    for(int k=0;k<4;k++){
      if(s[i][k]==c||s[i][k]=='T')cnt1++;
      if(s[k][i]==c||s[k][i]=='T')cnt2++;
    }
    if(cnt1==4||cnt2==4)return true;
  }
  cnt1=cnt2=0;
  for(int i=0;i<4;i++){
    if(s[i][i]==c||s[i][i]=='T')cnt1++;
    if(s[i][3-i]==c||s[i][3-i]=='T')cnt2++;
  }
  if(cnt1==4||cnt2==4)return true;
  return false;
}
int dotCount(string s[]){
 int dc=0;
 for(int i=0;i<4;i++)for(int k=0;k<4;k++)
   if(s[i][k]=='.')dc++;
  return dc;
}
int main(){
  int t;
  scanf("%d",&t);
  for(int tc=1;tc<=t;tc++){
    string s[4];
    for(int z=0;z<4;z++)cin>>s[z];
    printf("Case #%d: ",tc);
    if(Win(s,'X'))printf("X won");
    else if(Win(s,'O'))printf("O won");
    else if(dotCount(s)==0)printf("Draw");
    else printf("Game has not completed");
    putchar('\n');
  }
  return 0;
}
