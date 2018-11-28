#include <cstdio>
#include <algorithm>
#include <cstring>
#include <map>
#include <cmath>
#include <vector>
#include <set>
#include <cstdlib>
using namespace std;
int Q,X,Y;
int ok;
char buf[55];
char tile[55][55];
int main(){
  scanf("%d",&Q);
  for(int q=1;q<=Q;q++){
    printf("Case #%d:\n",q);
    ok=1;
    for(int i=0;i<55;i++) for(int j=0;j<55;j++) tile[i][j]='.';
    scanf("%d %d",&Y,&X);
    for(int i=0;i<Y;i++){
      scanf("%s",&buf);
      for(int j=0;j<X;j++){
        if (buf[j]=='.'){
           if (tile[i][j]!='.')
              ok=0;
        }else{
          if (tile[i][j]=='.'){
            tile[i][j]='/';
            tile[i][j+1]='\\';
            tile[i+1][j+1]='/';
            tile[i+1][j]='\\';
            if (i+1>=Y) ok=0;
            if (j+1>=X) ok=0;
            }
             
        }
      }
      
    }
    if (ok==0) printf("Impossible\n");
    else{
      for(int i=0;i<Y;i++){
        for(int j=0;j<X;j++)
          printf("%c",tile[i][j]);
        printf("\n");
      }
    }
  }
}
