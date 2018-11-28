#include <iostream>
#include <string>
using namespace std;

int t,r,c;
int table[52][52];
char floor[]=".#/\\";

void calc(){
  for(int i=1;i<=r;i++){
    for(int j=1;j<=c;j++){
      if(table[i][j]==1){
        if(table[i][j+1]==1&&table[i+1][j]==1&&table[i+1][j+1]==1){
          table[i+0][j+0]=2;
          table[i+0][j+1]=3;
          table[i+1][j+0]=3;
          table[i+1][j+1]=2;
        }else {
          cout<<"Impossible"<<endl;
          return;
        }
      }
    }
  }
  
  for(int i=1;i<=r;i++){
    for(int j=1;j<=c;j++){
      cout<<floor[table[i][j]];
    }
    cout<<endl;
  }
  
  
}

int main(){
  cin>>t;
  string s;
  for(int tcase=1;tcase<=t;tcase++){
    cin>>r>>c;
    for(int i=0;i<=r+1;i++){
      if(i!=0&&i!=r+1)cin>>s;
      for(int j=0;j<=c+1;j++){
        table[i][j]=0;
        if(i==0||j==0||i==r+1||j==c+1){
          continue;
        }
        else if(s[j-1]=='#')table[i][j]=1;
      }
    }
    
    cout<<"Case #"<<tcase<<":"<<endl;
    calc();
  }
}