#include <stdio.h>
#include <vector>
#include <string.h>
using namespace std;
int dx[] = {1,1,1,0,0,-1,-1,-1};
int dy[] = {-1,0,1,1,-1,-1,0,1};
int main(){
  int tt; scanf("%d",&tt);
  for (int ti=1;ti<=tt;ti++){
    int n, K; scanf("%d%d",&n,&K);
    char a[n][n+1],b[n][n];
    vector<char> s[n];
    int h[n]; memset(h,0,sizeof(h));
    for (int i=0;i<n;i++){
      scanf("%s",a[i]);
      
    }
    memset(b,'.',sizeof(b));
  
    for (int i=0;i<n;i++){
      for (int j=n-1;j>=0;j--){
        if (a[i][j]!='.'){
          s[i].push_back(a[i][j]);
        }
      }
      for (int j=0;j<s[i].size();j++){
        b[n-1-j][n-1-i] = s[i][j];
      }
    }

    bool rwin=false, bwin=false;

    for (int i=0;i<n;i++){
      for (int j=0;j<n;j++){
        if (b[i][j]=='.')continue;
      //  printf("ij %d %d\n",i,j);
        bool con=false;
        char check=b[i][j];
        for (int d=0;d<8 && !con;d++){
          bool con=true;
          //printf("d %d\n",d);
          for (int k=1;k<K && con;k++){
            int x=i+k*dx[d], y=j+k*dy[d];
            //printf("%d %d",x,y);
            if (x<0 || x>=n || y<0 || y>=n)con=false;
            if (b[x][y]!=check)con=false;
          }

          if (con){ 
            if (check=='R') rwin=true;
            else bwin=true;
          }
        }
      }
    }
    
    if (bwin&&rwin){
      printf("Case #%d: Both\n", ti);
    }else if (bwin){
      printf("Case #%d: Blue\n", ti);
      
    }else if (rwin){
      printf("Case #%d: Red\n", ti);
    }else{
      printf("Case #%d: Neither\n", ti);
    }
/*
    for (int i=0;i<n;i++){
      for (int j=0;j<n;j++){
        printf("%c",b[i][j]);
      }
      puts("");
    }
    puts(""); */
  }
  return 0;
}
