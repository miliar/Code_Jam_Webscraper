#include<iostream>
#include <fstream>
using namespace std;
int N,r,c;
char pic[51][51];
//string pic[51];
void res(int r,int c){
  for(int i=0;i<=r;i++){
    for(int j=0;j<=c;j++){
      pic[i][j]='.';
    }
  }
}
int main(){
    ifstream fin("A-small-attempt2.in");
    ofstream fout("ans.txt");
    fin>>N;
    for(int i=1;i<=N;i++){
    fin>>r>>c;
    res(r,c);
    for(int j=0;j<r;j++){
            for(int k=0; k<c; k++){
                    fin>>pic[j][k];
        }
    }
    bool f=false;
    for(int j=0;j<r;j++){
      for(int k=0;k<c;k++){
              if(pic[j][k]=='.')continue;
        if(pic[j][k]=='#'){
          pic[j][k]='/';
//          fout<<pic[j+1][k]<<' '<<pic[j][k+1]<<' '<< pic[j+1][k+1];
          if(pic[j+1][k]=='#' && pic[j][k+1]=='#' && pic[j+1][k+1]=='#'){
            pic[j+1][k]='\\';
            pic[j][k+1]='\\';
            pic[j+1][k+1]='/';
          }else{
            //fout<<j<<' '<<k<<'\n';
            f=true;
            break;
          }
        }
      }
      if(f){
        break;
      }
    }
    fout<<"Case #"<<i<<":\n";
    if(f){
      fout<<"Impossible\n";
    }else{
      for(int j=0;j<r;j++){
        for(int k=0;k<c;k++){
          fout<<pic[j][k];
        }
        fout<<'\n';
      }
    }
  }
  cin.get();
  cin.ignore();
//  system("pause");
return 0;
}
