#include<iostream>
#include<string>
using namespace std;
int T;
string mp[4];
string check(string p){
  int flg=1;
  for(int i=0;i<4;i++){
    flg=1;
    for(int j=0;j<4;j++){
      if(mp[i][j]!=p[0]&&mp[i][j]!='T'){flg=0;break;}
    }
    if(flg==1)return p;
  }
  for(int i=0;i<4;i++){
    flg=1;
    for(int j=0;j<4;j++){
      if(mp[j][i]!=p[0]&&mp[j][i]!='T'){flg=0;break;}
    }
    if(flg==1)return p;
  }
  flg=1;
  for(int i=0;i<4;i++){
    if(mp[i][i]!=p[0]&&mp[i][i]!='T'){flg=0;break;} 
  }
  if(flg==1)return p;
  flg=1;
  for(int i=0;i<4;i++){
    if(mp[i][3-i]!=p[0]&&mp[i][3-i]!='T'){flg=0;break;} 
  }
  if(flg==1)return p;
  return "-";
}

int main(){
  cin>>T;
  for(int t=0;t<T;t++){
    string ans="";
    bool bl=false;
    string winner="-";
    for(int i=0;i<4;i++)cin>>mp[i];
    for(int i=0;i<4;i++){
      for(int j=0;j<4;j++){
        if(mp[i][j]=='.')bl=true;
      }
    }
    winner=check("X");
    if(winner=="-")winner=check("O");
    //cout<<winner<<endl;
    if(bl==false&&winner=="-"){
      ans="Draw";
    }else if(winner=="-"){
      ans="Game has not completed";
    }else{
      ans=(string)(winner)+" won";
    }
    cout<<"Case #"<<t+1<<": ";cout<<ans<<endl;
  }

}
