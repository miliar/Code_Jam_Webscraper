#include <cstdio>
#include <cstring>

int n;
char matriz[50][50], tmp[50];

int inv(int i) {
  for (int j = n-1; j > i; j--)
    if (matriz[i][j] == '1')
      return 1;
  return 0;
}

int pode(int k, int i) {
  for (int j = n-1; j > i; j--)
    if (matriz[k][j] == '1')
      return 0;
  return 1;
}

int move(int k, int ii) {
  int cnt = 0;
  for (int i = k-1; i >= ii; i--) {
    memcpy(tmp, matriz[i+1], sizeof(tmp));
    memcpy(matriz[i+1], matriz[i], sizeof(matriz[i+1]));
    memcpy(matriz[i], tmp, sizeof(matriz[i]));
    cnt++;
  }
  return cnt;
}

int main() {
  int nt;
  int cases = 1;

  scanf(" %d", &nt);
  while (nt--) {
    scanf(" %d", &n);
    for (int i = 0; i < n; i++)
      for (int j = 0; j < n; j++)
	scanf(" %c", &matriz[i][j]);

    int res = 0;
    for (;;) {
      for (int i = 0; i < n; i++)
	if (inv(i))
	  for (int j = i+1; j < n; j++)
	    if (pode(j, i)) {
	      res += move(j, i);
	      goto next;
	    }
      break;
    next:
      ;
    }

    printf("Case #%d: %d\n", cases++, res);
  }

  return 0;
}
