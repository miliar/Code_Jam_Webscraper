#include <cstdio>
#include <string>

using namespace std;

char tab[100][100];

int main() {
  int T, N, K, cases = 1;

  scanf(" %d", &T);

  while (T--) {
    scanf(" %d%d", &N, &K);
    
    for (int i = 0; i < N; i++)
      scanf(" %s", tab[i]);

    for (int i = 0; i < N; i++)
      for (int j = N-1; j >= 0; j--) {
	char c = tab[i][j]; tab[i][j] = '.';
	int k;
	for (k = j; k < N; k++)
	  if (tab[i][k] != '.') break;
	tab[i][k-1] = c;
      }

    // printf("----------------------------\n");
    // for (int i = 0; i < N; i++)
    //   printf("%s\n", tab[i]);
    // printf("----------------------------\n");

    bool won[2] = {false, false};
    for (int i = 0; i < N; i++)
      for (int j = 0; j < N; j++) {
	if (tab[i][j] == '.') continue;
	char color = tab[i][j];
	int k, r;
	for (k = j, r = 0; r < K && k < N; r++, k++) if (tab[i][k] != color) break;
	if (r == K) won[tab[i][j] == 'R' ? 0 : 1] = true;
	for (k = i, r = 0; r < K && k < N; r++, k++) if (tab[k][j] != color) break;
	if (r == K) won[tab[i][j] == 'R' ? 0 : 1] = true;
	for (r = 0; r < K && i+r < N && j+r < N; r++) if (tab[i+r][j+r] != color) break;
	if (r == K) won[tab[i][j] == 'R' ? 0 : 1] = true;
	for (r = 0; r < K && i+r < N && j-r >= 0; r++) if (tab[i+r][j-r] != color) break;
	if (r == K) won[tab[i][j] == 'R' ? 0 : 1] = true;
      }

    string res;

    if (won[0] && won[1]) res = "Both";
    else if (won[0]) res = "Red";
    else if (won[1]) res = "Blue";
    else res = "Neither";

    printf("Case #%d: %s\n", cases++, res.c_str());

  }



  return 0;
}
