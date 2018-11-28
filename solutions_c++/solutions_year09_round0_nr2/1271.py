#include<stdio.h>
#include<string.h>
#include<vector>
#include<algorithm>
using namespace std;

#define MAXN 200
#define MAXN2 (MAXN*MAXN)

int heights[MAXN][MAXN];
int h, w;
int ncases;

int label[MAXN][MAXN];
vector<pair<int, int> > labels[MAXN2];


int dx[] = {-1, 0, 0, 1};
int dy[] = {0, -1, 1, 0};
char labelling[MAXN2];


int main(){
  scanf("%d\n", &ncases);
  for(int ncase = 1; ncase <= ncases; ncase++){
    printf("Case #%d:\n", ncase);
    scanf("%d %d\n", &h, &w);
    int clabel = 1;
    for(int i = 0; i < h; i++){
      for(int j = 0; j < w; j++){
        scanf("%d", &heights[i][j]);
        labels[clabel].clear();
        labels[clabel].push_back(make_pair(i, j));
        label[i][j] = clabel++;
      }
    }

    for(int i = 0; i < h; i++){
      for(int j = 0; j < w; j++){
        int newlab;
        int bestval = 1000000;
        for(int k = 0; k < 4; k++){
          int nx = i + dx[k];
          int ny = j + dy[k];
          if (nx < 0 || ny < 0 || nx >= h || ny >= w)
            continue;
          if (heights[nx][ny] < bestval){
            bestval = heights[nx][ny];
            newlab = label[nx][ny];
          }
        }
        if (bestval >= heights[i][j])
          continue;
        int oldlab = label[i][j];
        if (labels[newlab].size() > labels[oldlab].size())
          std::swap(newlab, oldlab);
        for(int i = 0; i < labels[oldlab].size(); i++){
          labels[newlab].push_back(labels[oldlab][i]);
          pair<int,int> p = labels[oldlab][i];
          label[p.first][p.second] = newlab;
        }
      }
    }

    char curlabel = 'a';
    memset(labelling, 0, sizeof(labelling));
    for(int i = 0; i < h; i++){
      for(int j = 0; j < w; j++){
        if (!labelling[label[i][j]])
          labelling[label[i][j]] = curlabel++;
        if (j)
          printf(" ");
        printf("%c", labelling[label[i][j]]);
      }
      printf("\n");
    }
  }
}
