#include<cstdio>
#include<fstream>
#include<iostream>
#include<climits>
#include<algorithm>

#define MaxN 100
#define MaxC 255 // 0-255

#define FOR(a, b, c) for(int a=b;a<=c;a++)
#define FORD(a,b,c) for(int a=b; a>=c; a--)

using namespace std;

int Dy[MaxN + 1][MaxC + 1];
int M , N , D , I;
int Input[MaxN + 1];

int _distance(int a, int b){
  int ret = (a - b);
  if(ret < 0) ret = -ret;
  return ret;
}

void init(void){
  cin >> D >> I >> M >> N;
  FOR(i, 1, N){
    cin >> Input[i];
    FOR(j, 0, MaxC){
      Dy[i][j] = INT_MAX;
    }
  }
  FOR(j, 0, MaxC){
    Dy[0][j] = I;
  }
}

void process(void){
  FOR(i, 1, N){
    //delete
    FOR(j, 0, MaxC){
      Dy[i][j] = Dy[i-1][j] + D;
    }
    //change
    FOR(j, 0, MaxC){
      int baseCost = _distance(Input[i], j);
      int minFrom = INT_MAX;
      FOR(k, j-M, j+M){
        if(k >= 0 && k <= MaxC){
          minFrom = min(minFrom, Dy[i - 1][k]);
        }
      }
      if(i == 1){
        minFrom = 0;
      }
      Dy[i][j] = min(Dy[i][j], minFrom + baseCost);
    }
    //insert
    FOR(j, 0, MaxC){
      FOR(k ,0, MaxC){
        int d = _distance(j, k);
        if(M != 0){
          int cost = (d / M) * I;
          if(d % M != 0){
            cost += I;
          }
          Dy[i][j] = min(Dy[i][j], Dy[i][k] + cost);
        }
      }
    }
    /*
    FOR(j, 0, 10){
      cerr << Dy[i][j] << ' ';
    }
    cerr << endl;*/
  }
}

void out(int cn){
  int answer = INT_MAX;
  FOR(j, 0, MaxC){
    answer = min(answer, Dy[N][j]);
  }
  printf("Case #%d: %d\n", cn, answer);
}

int main(void){
  int K;
  cin >> K;
  FOR(i, 1, K){
    init();
    process();
    out(i);
  }
  return 0;
}

