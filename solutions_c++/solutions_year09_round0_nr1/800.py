#include<iostream>
#include<string>
using namespace std;
#define REP(i,b,n) for(int i=b;i<n;i++)
#define rep(i,n)   REP(i,0,n)
bool table[26][15];

void clear(){
  rep(i,26)rep(j,15)table[i][j]=false;
}

bool isexist(string &a){
  rep(i,a.size()){
    if ( table[a[i]-'a'][i] == false)return false;
  }
  return true;
}

int solve(string tar,string *in,int n){
  for(int i=0,p=0;i<tar.size();i++,p++){
    if ( tar[i] !='('){
      table[tar[i]-'a'][p]=true;
    }else {
      i++;
      while(i<tar.size()&&tar[i] != ')'){
	table[tar[i]-'a'][p]=true;
	i++;
      }
    } 
  }
  
  int ret=0;
  rep(i,n){
    if ( isexist(in[i]))ret++;
  }

  return ret;
}

main(){
  int l,d,n;
  while(cin>>l>>d>>n){
    string in[d];
    rep(i,d)cin>>in[i];
    int tc=1;
    
    rep(i,n){
      clear();
      string tar;
      cin>>tar;
      cout << "Case #"<<tc++<<": "<<solve(tar,in,d)<<endl;
    }

  }
  return false;
}
