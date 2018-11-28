#include <cstdio>
#include <cstdlib>
#include <string>

using namespace std;

bool verifica(int a[100][100], int n, int k, char c){
  for (int i = 0; i < n; i++){
    for (int j = 0; j < n; j++){
      if (a[i][j] == c){
	int cont = 1;
	for (int x = 1; j+x < n && a[i][j+x] == c; x++)
	  cont++;
	if (cont >= k) return true;
	cont = 1;
	for (int x = 1; i+x < n && a[i+x][j] == c; x++)
	  cont++;
	if (cont >= k) return true;
	cont = 1;
	for (int x = 1; i+x < n && j+x < n && a[i+x][j+x] == c; x++)
	  cont++;
	if (cont >= k) return true;
	cont = 1;
	for (int x = 1; i-x >= 0 && j+x < n && a[i-x][j+x] == c; x++)
	  cont++;
	if (cont >= k) return true;
      }
    }
  }

  return false;
}

int main(){
  int t, n, k, a[100][100];

  scanf("%d", &t);
  for (int caso = 1; caso <= t; caso++){
    scanf("%d %d", &n, &k);
    getchar();
    for (int i = 0; i < n; i++){
      for (int j = 0; j < n; j++){
	a[i][j] = getchar();
      }
      getchar();
    }

    for (int i = 0; i < n; i++){
      int j, k;
      for (j = n-1, k = n-1; j >= 0; j--){
	if (a[i][j] != '.'){
	  char c = a[i][j];
	  a[i][j] = '.';
	  a[i][k] = c;
	  k--;
	}
      }
    }

    bool blue = verifica(a, n, k, 'B');
    bool red = verifica(a, n, k, 'R');
    printf("Case #%d: ", caso);
    if (blue and red)
      printf("Both\n");
    else if (blue)
      printf("Blue\n");
    else if (red)
      printf("Red\n");
    else
      printf("Neither\n");

    /*for (int i = 0; i < n; i++){
      for (int j = 0; j < n; j++)
	printf("%c", a[i][j]);
      printf("\n");
      }*/
  }

  return 0;
}
