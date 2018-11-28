using namespace std;
#include <iostream>
#include <map>



int di[] = {-1, +0, +0, +1};
int dj[] = {+0, -1, +1, +0};

const int MAXN = 105;
int rows, cols;
int mat[MAXN][MAXN];
int inbas[MAXN][MAXN];
int current_inbas;
map<int, char> cara;

inline bool inside(int i, int j){
  return 0 <= i && i < rows && 0 <= j && j < cols;
}

bool hundir(int i, int j){
  if (!inside(i, j)) return false;
  for (int k=0; k<4; ++k){
    int ni = i + di[k], nj = j + dj[k];
    if (inside(ni, nj) && mat[ni][nj] < mat[i][j]) return false;
  }
  return true;
}

int find_inbas(int i, int j){
  if (inbas[i][j] != -1) return inbas[i][j];
  if (hundir(i, j)){
    if (inbas[i][j] == -1) inbas[i][j] = current_inbas++;
    return inbas[i][j];
  }
  int best = INT_MAX;
  int bi = -1, bj = -1;
  for (int k=0; k<4; ++k){
    int ni = i + di[k], nj = j + dj[k];
    if (inside(ni, nj) && mat[ni][nj] < best){
      best = mat[ni][nj];
      bi = ni, bj = nj;
    }
  }
  return inbas[i][j] = find_inbas(bi, bj);
}
int main(){
  int T;
  cin >> T;
  for (int Caso=1; Caso<=T; ++Caso){
    cin >> rows >> cols;
    current_inbas = 0;
    cara.clear();
    for (int i=0; i<rows; ++i){
      for (int j=0; j<cols; ++j){
        cin >> mat[i][j];
        inbas[i][j] = -1;
      }
    }
    for (int i=0; i<rows; ++i){
      for (int j=0; j<cols; ++j){
        find_inbas(i, j);
      }
    }

    char current_cara = 'a';

    printf("Case #%d:\n", Caso);
    for (int i=0; i<rows; ++i){
      for (int j=0; j<cols; ++j){
        if (cara.count(inbas[i][j]) == 0){
          cara[inbas[i][j]] = current_cara++;
        }
        printf("%c", cara[inbas[i][j]]);
        if (j < cols - 1) printf(" ");
      }
      printf("\n");
    }

  }
  return 0;
}
