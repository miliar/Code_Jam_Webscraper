#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cctype>
#include <cassert>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>

#define D(x) cerr << #x << " = " << x << endl
#define REP(i,a,n) for(int i=(a); i<(int)(n); i++)
#define FOREACH(it,v) for(typeof((v).begin()) it=(v).begin(); it!=(v).end(); ++it)
#define ALL(v) (v).begin(), (v).end()

typedef long long int64;

const int INF = (int)(1e9);
const int64 INFLL = (int64)(1e18);
const double EPS = 1e-13;

const int SIZE = 4;
char matrix[SIZE][SIZE];

int dx[] ={0,-1,0,1,-1,-1,1,1};
int dy[] ={-1,0,1,0,-1,1,1,-1};

bool validate(int x, int y){
  return x >=0 && x < SIZE && y>=0 && y<SIZE;
}

using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  freopen("a.in","r", stdin);
  freopen("a.out","w",stdout);
  
  int t;
  cin >> t;
  
  for(int k=1; k<=t;k++){
    for(int i=0; i<SIZE; i++){
      string line;
      cin >> line;
      for(int j=0;j<SIZE;j++)
          matrix[i][j] = line[j];
    }
    
    bool winX = false;
    bool winO = false;
    bool completed  = true;
    for(int i=0;i<SIZE;i++){
        for(int j=0; j<SIZE;j++){
          char c = matrix[i][j];
          if(c == '.')
            completed = false;
            
          if(c != 'T'){              
              for(int l=0;l<SIZE*2; l++){
                
                int count = 1;
                int nx = i;
                int ny = j;
                
                for(int m=1; m<SIZE;m++){
                  nx = nx+dx[l];
                  ny = ny+dy[l];
                  
                  if(validate(nx,ny) && (matrix[nx][ny] == c || matrix[nx][ny] == 'T')){
                    count++;
                  }else
                    m = SIZE;
                }
                
                if(count == 4 && c == 'O'){
                    winO = true;
                    i = SIZE; 
                    j = SIZE;
                    l = SIZE*2;
                    
                }
                else if(count == 4 && c == 'X'){
                    winX = true;
                    i = SIZE; 
                    j = SIZE;
                    l = SIZE*2;
                }
              }            
          }
        }
    }
    
    if(!winO && !winX && completed){
      cout << "Case #"<<k<<": Draw"<<endl;
    }else if(winO){
      cout << "Case #"<<k<<": O won"<<endl;
    }else if(winX){
      cout << "Case #"<<k<<": X won"<<endl;      
    }else if(!winO && !winX && !completed){
      cout << "Case #"<<k<<": Game has not completed"<<endl;
    }
    
  }
  
  return 0;
}

