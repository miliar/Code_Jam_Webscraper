//UltraBlue
#include<iostream>
using namespace std;
int t,r,c;
char pic[51][51];
void res(int r,int c){
  for(int i=0;i<=r;i++){
    for(int j=0;j<=c;j++){
      pic[i][j]='.';
    }
  }
}
int main(){
  cin>>t;
  for(int i=1;i<=t;i++){
    cin>>r>>c;
    res(r,c);
    for(int j=0;j<r;j++){
      for(int k=0;k<c;k++){
        cin>>pic[j][k];
      }
    }
    bool f=false;
    for(int j=0;j<r;j++){
      for(int k=0;k<c;k++){
        if(pic[j][k]=='#'){
          pic[j][k]='/';
          if(pic[j+1][k]=='#' && pic[j][k+1]=='#' && pic[j+1][k+1]=='#'){
            pic[j+1][k]='\\';
            pic[j][k+1]='\\';
            pic[j+1][k+1]='/';
          }else{
            //cout<<j<<' '<<k<<'\n';
            f=true;
            break;
          }
        }
      }
      if(f){
        break;
      }
    }
    cout<<"Case #"<<i<<":\n";
    if(f){
      cout<<"Impossible\n";
    }else{
      for(int j=0;j<r;j++){
        for(int k=0;k<c;k++){
          cout<<pic[j][k];
        }
        cout<<'\n';
      }
    }
  }
system("pause");
return 0;
}
