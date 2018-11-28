#include <iostream>
#include <vector>
#include <map>
#include <sstream>

using namespace std;

bool zafarbi(int y, int x, vector<string> & o){
  bool ok=true;
  
  for(int i=y;i<=y+1;++i){
    for(int j=x;j<=x+1;++j){
      if(j<o[0].size() && i<o.size() && o[i][j]=='#'){
        ;
      }
      else {
        ok=false;
      }
    }
  }
  
  if(ok){
    o[y][x]='/';
    o[y+1][x+1]='/';
    o[y][x+1]='\\';
    o[y+1][x]='\\';
  }
  
  return ok;
}

int main(){
  int T;
  cin>>T;
  for(int t=1;t<=T;t++){
    int res=0;
    int r,c;
    cin>>r>>c;
    vector<string> pic(r);
    for(int i=0;i<r;++i) cin>>pic[i];
    
    bool ok = true;
    for(int i=0;i<r;++i){
      for(int j=0;j<c;++j){
        if(pic[i][j]=='#'){
          ok &= zafarbi(i,j,pic);
        }
        if (!ok) break;
      }
      if (!ok) break;
    }
        
    cout<<"Case #"<<t<<":"<<endl;
    if (!ok) {cout<<"Impossible\n";}
    else {
       for(int i=0;i<r;++i){
         cout<<pic[i]<<endl;
       }
    }
  }
  return 0;
}