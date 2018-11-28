#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <cstdio>
#include <map>
#include <algorithm>

#define For(i,n) for(int i=0;i<(n);i++)
#define For1(i,n) for(int i=1;i<=(n);i++)
#define ll long long
#define clear(d) memset(d,0,sizeof(d))
#define INF 2000000000

using namespace std;

int T[200][200];
int T1[200][200];
int T2[200][200];

int main(){
  int CN;
  cin >> CN;
  For1(CI,CN){
    clear(T);
    clear(T1);
    clear(T2);
    int N,K;
    cin >> N >> K;
    For(h,N){
      string s;
      cin >> s;
      For(w,N){
        //1:R,2:B
        T[h][N-1-w] = s[w]=='.' ? 0 : s[w]=='R' ? 1 : 2;
      }
    }
    For(h,N){
      int cur=0;
      For(w,N){
        if(T[h][w]){
          T[h][cur]=T[h][w];
          cur++;
        }
      }
      for(;cur<N;cur++){
        T[h][cur]=0;
      }
    }
    For(h,N){
      For(w,N)
        T1[h][w+h] = T[h][w];
    }
    For(h,N){
      For(w,N)
        T2[h][w+N-1-h] = T[h][w];
    }

    bool red=false, blue=false;

    For(h,N){
      int rc=0,bc=0;
      For(w,N){
        if(T[h][w]==1){
          bc=0;
          rc++;
          if(rc==K && !red){
            red=true;
          }
        }
        else if(T[h][w]==2){
          rc=0;
          bc++;
          if(bc==K && !blue){
            blue=true;
          }
        }
        else{
          rc=0;
          bc=0;
        }
      }
    }

    For(w,N){
      int rc=0,bc=0;
      For(h,N){
        if(T[h][w]==1){
          bc=0;
          rc++;
          if(rc==K && !red){
            red=true;
          }
        }
        else if(T[h][w]==2){
          rc=0;
          bc++;
          if(bc==K && !blue){
            blue=true;
          }
        }
        else{
          rc=0;
          bc=0;
        }
      }
    }

    For(w,2*N){
      int rc=0,bc=0;
      For(h,N){
        if(T1[h][w]==1){
          bc=0;
          rc++;
          if(rc==K && !red){
            red=true;
          }
        }
        else if(T1[h][w]==2){
          rc=0;
          bc++;
          if(bc==K && !blue){
            blue=true;
          }
        }
        else{
          rc=0;
          bc=0;
        }
      }
    }

    For(w,2*N){
      int rc=0,bc=0;
      For(h,N){
        if(T2[h][w]==1){
          bc=0;
          rc++;
          if(rc==K && !red){
            red=true;
          }
        }
        else if(T2[h][w]==2){
          rc=0;
          bc++;
          if(bc==K && !blue){
            blue=true;
          }
        }
        else{
          rc=0;
          bc=0;
        }
      }
    }


    if(red && blue)
      cout << "Case #" << CI << ": Both" << endl;
    else if(red)
      cout << "Case #" << CI << ": Red" << endl;
    else if(blue)
      cout << "Case #" << CI << ": Blue" << endl;
    else
      cout << "Case #" << CI << ": Neither" << endl;
  }
}
