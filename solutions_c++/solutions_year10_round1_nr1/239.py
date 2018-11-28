#include <cstdio>
#include <string>
#include <vector>

using namespace std;

const int Max = 64;

vector<string> rev;
int dr[4] = {+1, +1, +1, 0};
int dc[4] = {+1, -1, 0, +1};
bool isR, isB;

int N, K;
void check(int r, int c, int d)
{
  bool allSame = true;
  for (int k = 0; k < K; k++) {
    int rr = r + dr[d]*k;
    int cc = c + dc[d]*k;

    bool same = true;
    if (rr >= N || rr < 0 || cc >= N || cc < 0)
      same = false; else
      if (rev[rr][cc] != rev[r][c])
	same = false;

    if (!same) {
      allSame = false;
      break;
    }
  }
  if (allSame && rev[r][c] == 'R')
    isR = true;
  if (allSame && rev[r][c] == 'B')
    isB = true;
}

const char* solve()
{
  scanf("%d %d\n", &N, &K);
  rev = vector<string>(N, "");

  for (int i = 0; i < N; i++) {
    static char stg[Max];
    gets(stg);
    string S;
    for (int j = 0; stg[j]; j++)
      if (stg[j] != '.')
	S += stg[j];
    S = string(N-S.size(), '.') + S;

    for (int j = 0; j < N; j++)
      rev[j] = S[j] + rev[j];
  }


  isR = isB = false;
  for (int r = 0; r < N; r++)
    for (int c = 0; c < N; c++)
      if (rev[r][c] != '.')
	for (int d = 0; d < 4; d++) 
	  check(r, c, d);

  if (isR && isB)   return "Both";
  if (isR && !isB)  return "Red";
  if (!isR && !isB) return "Neither";
  if (!isR && isB)  return "Blue";
}

int main()
{
  int nTest;
  scanf("%d", &nTest);
  for (int iTest = 0; iTest < nTest; iTest++)
    printf("Case #%d: %s\n", iTest+1, solve());
  return 0;
}
