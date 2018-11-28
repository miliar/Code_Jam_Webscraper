#include <iostream>
#include <string>
using namespace std;

int main(){
  int t;
  cin>>t;
  string s[4];
  for(int test = 1, tot = 0; test <= t; test ++, tot = 0){
    bool X = 0, O = 0;
    for(int i=0,x=0,o=0;i<4;i++)
      cin>>s[i];
    for(int i=0,x=0,x1=0,x2=0,x3=0,o=0,o1=0,o2=0,o3=0;i<4;i++,x=0,x1=0,x2=0,x3=0,o=0,o1=0,o2=0,o3=0){
      for(int j=0;j<4;j++){
	if (s[i][j] == 'X' || s[i][j]=='T')
	  x++;
	if(s[i][j] == 'O' || s[i][j]=='T')
	  o++;
	if(s[j][i] == 'X' || s[j][i] == 'T')
	  x1++;
	if(s[j][i] == 'O' || s[j][i] == 'T')
	  o1++;
	if(s[j][j] == 'O' || s[j][j] == 'T')
	  o2++;
	if(s[j][j] == 'X' || s[j][j] == 'T')
	  x2++;
	if(s[j][3-j] == 'X' || s[j][3-j] == 'T')
	  x3++;
	if(s[j][3-j] == 'O' || s[j][3-j] == 'T')
	  o3++;
	if(s[i][j] != '.')
	  tot++;
      }
      if(x==4 || x1==4 || x2==4 || x3==4) X=1;
      if(o==4 || o1==4 || o2==4 || o3==4) O=1;
    }
    cout<<"Case #"<<test<<": ";
    if(X)
      cout<<"X won\n";
    else if(O)
      cout<<"O won\n";
    else if(tot==16)
      cout<<"Draw\n";
    else
      cout<<"Game has not completed\n";
  }
  return 0;
}
