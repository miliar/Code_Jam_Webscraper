#include<cstdio>
#include<fstream>
#include<iostream>

#define MaxN 100

#define FOR(a, b, c) for(int a=b;a<=c;a++)
#define FORD(a,b,c) for(int a=b; a>=c; a--)

using namespace std;

int Old[MaxN + 1][MaxN + 1];
int New[MaxN + 1][MaxN + 1];
int K, N;
const int EMPTY = 0, RED = 1, BLUE = 2;
int Answer;//0->neither, 1->red, 2->blue 3->both

void init(void){
  memset(Old, -1, sizeof(Old));
  memset(New, -1, sizeof(New));
  cin >> N >> K;
  FOR(i, 0, N-1){
    FOR(j, 0, N-1){
      char c;
      cin >> c;
      if(c == 'R'){
        Old[i][j] = RED;
      } else if(c == 'B'){
        Old[i][j] = BLUE;
      } else{
        Old[i][j] = EMPTY;
      }
    }
  }
  Answer = 0;
}

bool winning(int tok){
  int cnt;
  //col
  FOR(i, 0, N-1){
    cnt = 0;
    FOR(j, 0, N-1){
      if(New[i][j] == tok){
        cnt++;
        if(cnt == K) return true;
      } else{
        cnt = 0;
      }
    }
  }
  //row
  FOR(j, 0, N-1){
    cnt = 0;
    FOR(i, 0, N-1){
      if(New[i][j] == tok){
        cnt++;
        if(cnt == K) return true;
      } else{
        cnt = 0;
      }
    }
  }
  //dig1
  FOR(k, 0, 2 * N - 2){
    cnt = 0;
    FOR(i, 0, N-1){
      int j = k - i;
      if(j < 0 || j >= N){
        cnt = 0;
        continue;
      }
      if(New[i][j] == tok){
        cnt++;
        if(cnt == K) return true;
      } else{
        cnt = 0;
      }
    }
  }
  //dig2
  FOR(k, -(N-1), N-1){
    cnt = 0;
    FOR(i, 0, N-1){
      int j = k + i;
      if(j < 0 || j >= N){
        cnt = 0;
        continue;
      }
      if(New[i][j] == tok){
        cnt++;
        if(cnt == K) return true;
      } else{
        cnt = 0;
      }
    }
  }
  return false;
}

void process(void){
  FOR(i, 0, N-1){
    FOR(j, 0, N-1){
      int ii = j;
      int jj = N-i-1;
      New[ii][jj] = Old[i][j];
    }
  }
  //Gravity
  FOR(j, 0, N-1){
    int ii = N-1;
    FORD(i, N-1, 0){
      if(New[i][j]){
        int tmp = New[i][j];
        New[i][j] = EMPTY;
        New[ii--][j] = tmp;
      }
    }
  }
  /*
  FOR(i, 0, N-1){
    FOR(j, 0, N-1){
      cerr << New[i][j];
    }
    cerr << endl;
  }
  */
  if(winning(RED)) Answer += RED;
  if(winning(BLUE)) Answer += BLUE;
}

void out(int c){
  printf("Case #%d: ", c);
  if(Answer == 0){
    printf("Neither");
  } else if(Answer == 1){
    printf("Red");
  } else if(Answer == 2){
    printf("Blue");
  } else{
    printf("Both");
  }
  printf("\n");
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
