#include <iostream>
#define N 105
#define HIGH 20000
#define DEAD 4
using namespace std;

int alt[N][N];
int dir[N][N];
char mark[N][N];
int dh[4] = {-1,0,0,1};
int dw[4] = {0,-1,1,0};

void dfs(int i, int j, char ord){
  if (mark[i][j] != 0) return;
  //cout<<i<<' '<<j<<endl;
  mark[i][j] = ord;
  for (int l = 0; l<4; ++l)
    if ( dir[i+dh[l]][j+dw[l]] == 3-l )
      dfs(i+dh[l], j+dw[l], ord);
}

int main(){

  int n;
  cin >> n;
  for (int i=0; i<n;++i){
    memset(dir,0,sizeof(dir));
    memset(mark,0,sizeof(mark));
    int h,w;
    cin >>h >>w;
    for (int j=0; j<h; ++j)
      for (int k =0; k<w; ++k)
	cin >> alt[j+1][k+1];
    for (int j=0; j<=h+1; ++j){
      alt[j][0] = HIGH;
      alt[j][w+1] = HIGH;
      dir[j][0] = DEAD;
      dir[j][w+1] = DEAD;
    }
    for (int j=0; j<w+1; ++j){
      alt[0][j] = HIGH;
      alt[h+1][j] = HIGH;
      dir[0][j] = DEAD;
      dir[h+1][j] = DEAD;
    }

    for (int j = 1; j<=h; ++j)
      for (int k = 1; k<=w; ++k){
	int t = DEAD;
	for (int l = 0;l<4; ++l)
	  if (( alt[j+dh[l]][k+dw[l]] < alt[j][k] ) 
	      && ((t==DEAD) || ( alt[j+dh[l]][k+dw[l]] < alt[j+dh[t]][k+dw[t]] )))
	    t = l;
	dir[j][k] = t;
      }
    
    // for (int j = 0; j<=h+1; ++j){
    //   for (int k = 0; k<=w+1; ++k)
    // 	cout<<mark[j][k]<<' ';
    //   cout<<endl;
    // }
    char ord = 'a';
    for (int j = 1; j<=h; ++j)
      for (int k = 1; k<=w; ++k)
	if (mark[j][k] == 0){
	  int ti = j, tj = k;
	  while (dir[ti][tj] != DEAD){
	    ti = ti + dh[dir[ti][tj]];
	    tj = tj + dw[dir[ti][tj]];
	  }
	  dfs(ti,tj,ord);
	  ord++;
	}

    cout << "Case #"<<i+1<<":"<<endl;
    for (int j = 1; j<=h; ++j){
      for (int k = 1; k<w; ++k)
	cout << mark[j][k] << ' ';
      cout << mark[j][w] << endl;
    }
  }
}
