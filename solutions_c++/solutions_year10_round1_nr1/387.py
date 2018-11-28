#include <cstdio>
#include <string>
using namespace std;

int main(){
  int T;
  scanf("%d",&T);
  
  string answers[] = {"Neither", "Blue", "Red", "Both"};
  
  
  for(int Case = 1;Case<=T; Case++){
    int res = 0;
    int N,K;
    scanf("%d%d",&N,&K);
    char map[N+1][N+1];
    for(int i=0; i<N; i++)
      scanf("%s", map[i]);
    char map2[N+1][N+1];
    for(int j=0; j<N; j++){
      int k = N-1;
      for(int i=N-1; i>=0; i--)
        if(map[j][i]!='.')
          map2[k--][j] = map[j][i];
      for(;k>=0; k--)
        map2[k][j] = '.';    
    }
  /*  for(int i=0; i<N; i++){
      map2[i][N] = 0;
      printf("%s\n",map2[i]);
    }*/
    
    for(int j=0; j<N; j++)
    for(int i=0; i+K<=N; i++){
      bool flag = true;
      for(int k=i; k<i+K; k++)
        if(map2[j][k]!='B')
          flag = false;
      if(flag) res |= 1;
    }
    
    for(int j=0; j<N; j++)
    for(int i=0; i+K<=N; i++){
      bool flag = true;
      for(int k=i; k<i+K; k++)
        if(map2[k][j]!='B')
          flag = false;
      if(flag) res |= 1;
    }    
    
    for(int i=0; i+K<=N; i++)
    for(int j=0; j+K<=N; j++){
      bool flag = true;
      for(int k=0; k<K; k++)
        if(map2[i+k][j+k]!='B')
          flag = false;
      if(flag) res |= 1;      
    }    
    
    for(int i=0; i+K<=N; i++)
    for(int j=K-1; j<N; j++){
      bool flag = true;
      for(int k=0; k<K; k++)
        if(map2[i+k][j-k]!='B')
          flag = false;
      if(flag) res |= 1;      
    }        
    
    for(int j=0; j<N; j++)
    for(int i=0; i+K<=N; i++){
      bool flag = true;
      for(int k=i; k<i+K; k++)
        if(map2[j][k]!='R')
          flag = false;
      if(flag) res |= 2;
    }
    
    for(int j=0; j<N; j++)
    for(int i=0; i+K<=N; i++){
      bool flag = true;
      for(int k=i; k<i+K; k++)
        if(map2[k][j]!='R')
          flag = false;
      if(flag) res |= 2;
    }    
    
    for(int i=0; i+K<=N; i++)
    for(int j=0; j+K<=N; j++){
      bool flag = true;
      for(int k=0; k<K; k++)
        if(map2[i+k][j+k]!='R')
          flag = false;
      if(flag) res |= 2;      
    }    
    
    for(int i=0; i+K<=N; i++)
    for(int j=K-1; j<N; j++){
      bool flag = true;
      for(int k=0; k<K; k++)
        if(map2[i+k][j-k]!='R')
          flag = false;
      if(flag) res |= 2;      
    }      
        
    printf("Case #%d: %s\n",Case, answers[res].c_str());
  }    
}
