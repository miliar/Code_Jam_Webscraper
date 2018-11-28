#include <cstdio>

using namespace std;

char c[100][100];

#define IMP printf("Impossible\n");

void singleCase(){
  int n,m;
  scanf("%d %d",&n,&m);
  for(int i=0; i<n; i++){
    scanf("%s",c[i]);
  }
  
  for(int i=0; i<n; i++){
    for(int j=0; j<m; j++){
      if (c[i][j] == '#') {
        if (i == n-1 || j == m-1){
          IMP;
          return;
        }
        for(int x=0; x<=1; x++) {
          for(int y = 0; y<=1; y++) {
            if (c[i+x][j+y] != '#') {
              IMP;
              return ;
            }
          }
        }
        
        c[i][j] = '/'; c[i][j+1] = '\\';
        c[i+1][j] = '\\'; c[i+1][j+1] = '/';
        
      }
    }
  }
  
  for(int i=0; i<n; i++){
    puts(c[i]);
  }
}

int main() {
  int test;
  scanf("%d",&test);
  for(int i=1; i<=test; i++){
    printf("Case #%d:\n",i);
    singleCase();
  }
  return 0;
}

