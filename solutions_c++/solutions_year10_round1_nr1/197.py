#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstdio>
#include <vector>

using namespace std;
#define REP(i,N) for (int i = 0; i<(N); i++) 
#define ll long long

int N, K;
int table[52][52];
bool R,B;

int dx[8] = {-1,0,1,1,1,0,-1,-1};
int dy[8] = {-1,-1,-1,0,1,1,1,0};

bool valid( int x, int y){
  return 0<=x && x<N && 0<=y && y<N;
}

void check(int t[52][52]){
  if (R && B) return;

  for (int k=0; k<N; k++){
    for (int i=N-1; i>0; i--){
      for (int j=0; j<N; j++){
	if (t[i][j] == 0) {t[i][j] = t[i-1][j]; t[i-1][j] = 0;}
      }
    }
  }
  /*
    for (int i=0; i<N; i++){
      for (int j=0; j<N; j++){
	cout << t[i][j] << " ";
      }cout << endl;
    }cout << endl;
    v*/
  
  for (int i=0; i<N; i++){
    for (int j=0; j<N; j++){
      for (int cc = 0; cc <2; cc++){
	int c;
	if (cc == 0) c = 1;
	else c = -1;
	for (int d=0; d<8; d++){
	  bool f = true;
	  for (int k=0; k<K; k++){
	    int x = i+dx[d]*k;
	    int y = j+dy[d]*k;
	    if (!(valid( x,y) && t[x][y] == c)) {f=false; break;}
	  }
	  if (f && c==1) R = true;
	  if (f && c==-1) B = true;
	}
      }
    }
  }
}

void rotater(){
  int t[52][52];
  for (int i=0; i<N; i++){
    for (int j=0; j<N; j++){
      t[i][j] = table[j][N-i-1];
    }
  }

  check(t);
}

void rotatel(){
  int t[52][52];
  for (int i=0; i<N; i++){
    for (int j=0; j<N; j++){
      t[j][N-i-1] = table[i][j];
    }
  }

  check(t);
}

int main(){
  int T;
  cin >> T;
  for (int iii=0; iii<T; iii++){
    cin >> N>>K;
    R = B = false;
    for (int i=0; i<N; i++){
      for (int j=0; j<N; j++){
	char c = '\n';
	while (c == '\n') c = getchar();
	if (c == '.') table[i][j] = 0;
	if (c == 'R') table[i][j] = 1;
	if (c == 'B') table[i][j] = -1;
      }
    }
    //    check(table);
    //    rotater();
    rotatel();
    printf ("Case #%d: ",iii+1);
    if (R && B) printf( "Both\n");
    else if (R) printf( "Red\n");
    else if (B) printf( "Blue\n");
    else printf( "Neither\n");
    /*
    for (int i=0; i<N; i++){
      for (int j=0; j<N; j++){
	cout << table[i][j] << " ";
      }cout << endl;
    }cout << endl;
    */
  }
  return 0;
}
