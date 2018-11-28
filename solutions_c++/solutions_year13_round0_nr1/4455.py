#include<iostream>
#include<vector>
#include<string>

using namespace std;

bool isX(char a){
  return (a=='X' || a=='T');
}
bool isY(char a){
  return (a=='O' || a=='T');
}


int analyze(char a, char b, char c, char d){
  if (isX(a)&&isX(b)&&isX(c)&&isX(d)){
    return 2;
  }
  if (isY(a)&&isY(b)&&isY(c)&&isY(d)){
    return 1;
  }
  if ((a=='.')||(b=='.')||(c=='.')||(d=='.'))
    return 0;
  return -1;
}

int main(){
  int T;
  cin>>T;
  for (int t=1;t<=T;t++){
    string s;
    string s2="";
    for (int i=0;i<4;i++){
      cin>>s;
      s2+=s.substr(0,4);
    }
    //cout<<s2<<endl;
    //    cin>>s;
    int result = -1;
    for (int i=0;i<4;i++){
      result=max(analyze(s2[i],s2[i+4],s2[i+8],s2[i+12]),result);
      result=max(analyze(s2[4*i],s2[4*i+1],s2[4*i+2],s2[4*i+3]),result);
    }
    result=max(analyze(s2[0],s2[5],s2[10],s2[15]),result);
    result=max(analyze(s2[3],s2[6],s2[9],s2[12]),result);
    
    string res;
    if (result==0)
      res = "Game has not completed";
    if (result ==-1)
      res = "Draw";
    if (result == 1)
      res = "O won";
    if (result == 2)
      res = "X won";
    cout<<"Case #"<<t<<": "<<res<<endl;
  }
}
