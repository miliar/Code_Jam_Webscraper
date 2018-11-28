#include <iostream>
#include <cstdio>

using namespace std;

int main(){
  int T;
  cin >> T;
  for(int t=1;t<=T;t++){
    int R,C;
    cin >> R >> C;
    char buf[R][C];
    for(int i=0;i<R;i++){
      string s;
      cin >> s;
      for(int j=0;j<C;j++){
        buf[i][j] = s[j];
        if(buf[i][j] == '#')
          buf[i][j] = 'b';
      }
    }
    bool imp = false;
    for(int i=0;i<R;i++){
      int cons = 0;
      for(int j=0;j<C;j++){
        if(buf[i][j]=='b')
          cons++;
        if(buf[i][j]=='.'||j==C-1){
          if(cons%2)
            imp = true;
          cons = 0;
        }
      }
    }

    for(int j=0;j<C;j++){
      int cons = 0;
      for(int i=0;i<R;i++){
        if(buf[i][j]=='b')
          cons++;
        if(buf[i][j]=='.'||i==R-1){
          if(cons%2)
            imp = true;
          cons = 0;
        }
      }
    }
    if(imp){
      cout << "Case #" << t << ":" << endl << "Impossible" << endl;
      continue;
    }
    while(true){
      bool next = false;
      for(int i=0;i<R;i++){
        for(int j=0;j<C;j++){
          if(buf[i][j]=='b'){
            
            if(i>0){
              if(buf[i-1][j]=='b')
                continue;
            }
            if(j>0){
              if(buf[i][j-1]=='b')
                continue;
            }

            if(i>0&&j>0){
              if(buf[i-1][j-1]=='b')
                continue;
            }
            
            next = true;
            if(buf[i][j] != 'b' && buf[i][j] != '.' && buf[i][j]!='/')
              imp = true;
            else
              buf[i][j] = '/';
            if(buf[i][j+1] != 'b' && buf[i][j+1] != '.' && buf[i][j+1]!='\\')
              imp = true;
            else
              buf[i][j+1] = '\\';

            if(buf[i+1][j] != 'b' && buf[i+1][j] != '.' && buf[i+1][j]!='\\')
              imp = true;
            else
              buf[i+1][j] = '\\';

            if(buf[i+1][j+1] != 'b' && buf[i+1][j+1] != '.' && buf[i+1][j+1]!='/')
              imp = true;
            else
              buf[i+1][j+1] = '/';
            
            if(next)
              break;

          }
          if(next)
            break;
        }
      }
      if(!next || imp)
        break;
    }


    if(imp)
      cout << "Case #" << t << ":" << endl << "Impossible" << endl;
    else
      {
        cout << "Case #" << t << ":" << endl;
        for(int i=0;i<R;i++){
          for(int j=0;j<C;j++){
            cout << buf[i][j];
          }
          cout << endl;
        }
      }
  }
  return 0;
}
