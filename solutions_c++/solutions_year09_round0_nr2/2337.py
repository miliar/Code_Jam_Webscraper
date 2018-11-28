#include <cstdio>
#include <cstdlib>
#include <cstring>

#define TAM 100

using namespace std;

char label;
int h, w;
char sink[TAM][TAM];
int alt[TAM][TAM];

char dfs(int i, int j){
  if (sink[i][j] == '*'){
    int x = i, y = j;
    int cur = alt[i][j];
    if (i > 0 && alt[i-1][j] < cur){
      x = i-1;
      y = j;
      cur = alt[x][y];
    }
    if (j > 0 && alt[i][j-1] < cur){
      x = i;
      y = j-1;
      cur = alt[x][y];
    }
    if (j < w-1 && alt[i][j+1] < cur){
      x = i;
      y = j+1;
      cur = alt[x][y];
    }
    if (i < h-1 && alt[i+1][j] < cur){
      x = i+1;
      y = j;
      cur = alt[x][y];
    }

    if (x == i && y == j){
      sink[i][j] = label++;
    }
    else {
      sink[i][j] = dfs(x,y);
    }
  }
  return sink[i][j];
}

int main(){
  int t;

  scanf("%d", &t);
  for (int k = 1; k <= t; k++){
    scanf("%d %d", &h, &w);
    
    for (int i = 0; i < h; i++)
      for (int j = 0; j < w; j++)
	scanf("%d", &alt[i][j]);
    
    memset(sink, '*', TAM*TAM*sizeof(char));
    label = 'a';
    for (int i = 0; i < h; i++)
      for (int j = 0; j < w;j++){
	if (sink[i][j] == '*'){
	  dfs(i, j);
	}
      }
    
    printf("Case #%d:\n", k);
    for (int i = 0; i < h; i++){
      printf("%c", sink[i][0]);
      for (int j = 1; j < w; j++){
	printf(" %c", sink[i][j]);
      }
      printf("\n");
    }
  }

  return 0;
}
