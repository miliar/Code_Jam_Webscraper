#include<cstdio>
#include<cstring>
#include<algorithm>

using namespace std;

typedef long long ll;

ll M[512][512], S[512][512];
ll Mu[512][512], Md[512][512], Su[512][512], Sd[512][512];
ll Mr[512][512], Ml[512][512], Sr[512][512], Sl[512][512];

inline ll sum(ll X[512][512], int x1, int y1, int x2, int y2)
{
  return X[y2][x2] - X[y1-1][x2] - X[y2][x1-1] + X[y1-1][x1-1];
}

bool ok(int R, int C, int K)
{
  for(int r=1; r+K-1<=R; ++r) {
    for(int c=1; c+K-1<=C; ++c) {
      ll X = 0, Y = 0;
      int T = K % 2;

      int rc = r+K/2, cc = c+K/2;
      X += sum(Sr, cc+T, r, c+K-1, r+K-1) - Mr[r][c+K-1] - Mr[r+K-1][c+K-1];
      X -= (sum(S, cc+T, r, c+K-1, r+K-1) - M[r][c+K-1] - M[r+K-1][c+K-1]) * (cc-(1-T));
      X -= sum(Sl, c, r, cc-1, r+K-1) - Ml[r][c] - Ml[r+K-1][c];
      X += (sum(S, c, r, cc-1, r+K-1) - M[r][c] - M[r+K-1][c]) * (C-cc+1);
      
      Y += sum(Su, c, r, c+K-1, rc-1) - Mu[r][c] - Mu[r][c+K-1];
      Y -= (sum(S, c, r, c+K-1, rc-1) - M[r][c] - M[r][c+K-1]) * (R-rc+1);
      Y -= sum(Sd, c, rc+T, c+K-1, r+K-1) - Md[r+K-1][c] - Md[r+K-1][c+K-1];
      Y += (sum(S, c, rc+T, c+K-1, r+K-1) - M[r+K-1][c] - M[r+K-1][c+K-1]) * (rc-(1-T));
      
      if(X == 0 && Y == 0)
	return true;
    }
  }
  return false;
}

int main()
{
  int T;
  scanf("%d", &T);

  for(int CN=1; CN<=T; ++CN) {
    int R, C, D;

    memset(M, 0, sizeof(M));
    memset(Mu, 0, sizeof(Mu));
    memset(Md, 0, sizeof(Md));
    memset(Mr, 0, sizeof(Mr));
    memset(Ml, 0, sizeof(Ml));
    
    scanf("%d%d%d", &R, &C, &D);
    for(int i=1; i<=R; ++i) {
      char S[512];
      scanf("%s", S);
      for(int j=1; j<=C; ++j)
	M[i][j] = D + S[j-1] - '0';
    }

    for(int i=1; i<=R; ++i) {
      for(int j=1; j<=C; ++j) {
	Mu[i][j] = M[i][j] * (R-i+1);
	Md[i][j] = M[i][j] * i;
	Mr[i][j] = M[i][j] * j;
	Ml[i][j] = M[i][j] * (C-j+1);
      }
    }

    for(int i=1; i<=R; ++i) {
      for(int j=1; j<=C; ++j) {
	S[i][j] = S[i-1][j] + S[i][j-1] - S[i-1][j-1] + M[i][j];
	Su[i][j] = Su[i-1][j] + Su[i][j-1] - Su[i-1][j-1] + Mu[i][j];
	Sd[i][j] = Sd[i-1][j] + Sd[i][j-1] - Sd[i-1][j-1] + Md[i][j];
	Sr[i][j] = Sr[i-1][j] + Sr[i][j-1] - Sr[i-1][j-1] + Mr[i][j];
	Sl[i][j] = Sl[i-1][j] + Sl[i][j-1] - Sl[i-1][j-1] + Ml[i][j];
      }
    }

    printf("Case #%d: ", CN);
    for(int K=min(R, C); K >= 3; --K) {
      if(ok(R, C, K)) {
	printf("%d\n", K);
	break;
      }
      if(K == 3)
	puts("IMPOSSIBLE");
    }
  }
}
