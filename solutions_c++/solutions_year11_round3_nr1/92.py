#include <iostream>
#include <cstdio>
using namespace std;

const int MaxN = 51;

int n, m;
char output[MaxN][MaxN + 10];

int main() {
  int t; scanf("%d", &t);
  for (int test = 1; test <= t; test++) {
    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; i++) {
      scanf(" %s", output[i]);
    }

    bool ok = true;
    for (int i = 0; i < n; i++)
      for (int j = 0; j < m; j++) {
	if (output[i][j] == '#'){
	  if (i > n - 1 || j > m - 1) ok = false;
	  else if (output[i+1][j] != '#' || output[i][j+1] != '#' || output[i+1][j+1] != '#')
	    ok = false;
	  else{
	    output[i][j] = '/'; output[i][j+1] = '\\';
	    output[i+1][j] = '\\'; output[i+1][j+1] = '/';
	  }
	}
      }

    printf("Case #%d:\n", test);
    if (!ok) printf("Impossible\n");
    else{
      for (int i = 0; i < n; i++){
	for (int j = 0; j < m; j++) printf("%c", output[i][j]);
	printf("\n");
      }
    }
  }

  return 0;
}

 
