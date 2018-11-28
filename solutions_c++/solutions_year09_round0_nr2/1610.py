#include <cstdio>
#include <vector>
#define MAX 101

using namespace std;

int m[MAX][MAX];
int usado[MAX][MAX];
char r[MAX][MAX];
int H, W, T;

/*int xx[] = {0, -1, 1, 0};
int yy[] = {-1, 0, 0, 1};*/
int xx[] = {-1, 0, 0, 1};
int yy[] = {0, -1, 1, 0};

void fill(int i, int j, char& atual) {
  vector<pair<int, int> > cor;
  cor.push_back(make_pair(i, j));
  char colorir = atual;
  while(true) {
    int iatual = cor.back().first, jatual = cor.back().second;
    if(r[iatual][jatual] != '-') {
      colorir = r[iatual][jatual];
      break;
    }
    int menor = m[iatual][jatual], posusar = -1;
    for(int pos = 0; pos < 4; ++pos) {
      int xatual = iatual + xx[pos], yatual = jatual + yy[pos];
      if(xatual >= 0 && xatual < H && yatual >= 0 && yatual < W) {
        if(m[xatual][yatual] < menor) {
          posusar = pos;
          menor = m[xatual][yatual];
        }
      }
    }
    if(posusar == -1)
      break;
    cor.push_back(make_pair(iatual+xx[posusar], jatual+yy[posusar]));
  }
  int iatual = cor.back().first, jatual = cor.back().second;
  if(r[iatual][jatual] == '-') {
    ++atual;
  } else {
    colorir = r[iatual][jatual];
  }
  for(int i = 0; i < (int) cor.size(); ++i)
    r[cor[i].first][cor[i].second] = colorir;
}

int main() {
  scanf("%d", &T);
  for(int caso = 1; caso <= T; ++caso) {
    scanf("%d %d", &H, &W);
    for(int i = 0; i < H; ++i)
      for(int j = 0; j < W; ++j) {
        scanf("%d", &m[i][j]);
        r[i][j] = '-';
      }
    char atual = 'a';
    for(int i = 0; i < H; ++i)
      for(int j = 0; j < W; ++j) {
        if(r[i][j] == '-') {
          fill(i, j, atual);
        }
      }
    printf("Case #%d:\n", caso);
    for(int i = 0; i < H; ++i)
      for(int j = 0; j < W; ++j) {
        printf("%c", r[i][j]);
        if(j < W-1) printf(" ");
        else printf("\n");
      }
    
  }
  return 0;
}
