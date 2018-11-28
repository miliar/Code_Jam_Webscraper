#include <cstdio>

int main(){
  int n; scanf("%d\n", &n);
  for(int z = 0; z < n; z++) {
    int r, c; scanf("%d %d\n", &r, &c);
    char map[100][100];
    for(int i = 0; i < r; i++) 
	scanf("%s", map[i]);

    bool flag = true;
    for (int i = 0; i < r && flag; i++) {
      for (int j = 0; j < c && flag; j++) {
	if(map[i][j] == '#' && map[i][j+1] == '#' && map[i+1][j] == '#' && map[i+1][j+1] == '#') {
	  map[i][j] = '/'; map[i+1][j] = '\\'; map[i][j+1] = '\\'; map[i+1][j+1] = '/';
	} else if (map[i][j] != '.' && map[i][j] != '\\' && map[i][j] != '/'){ flag = false; }
      }
    }
    if (flag) {
      printf("Case #%d:\n", z+1);
      for(int i = 0; i < r; i++)
	puts(map[i]);
    } else {printf("Case #%d:\nImpossible\n", z+1);
    }
  }
  return 0;
}


	

