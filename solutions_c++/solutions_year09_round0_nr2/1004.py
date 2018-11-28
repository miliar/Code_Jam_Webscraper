
#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
#include <cstring>
using namespace std;

// N, W, E, S
int d[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

int terrain[102][102];
int labeling[100][100];
int H, W;

int nsinks = 0;
pair<int, int> sinks[100];
vector<pair<int, int> > graph[100][100];

#define ID(i, j) ((i)*W + (j))

void expand(pair<int, int> sink, int label)
{
  if (labeling[sink.first][sink.second] >= 0)
    return;

  //printf("labeling %d, %d as %d\n", sink.first, sink.second, label);
  labeling[sink.first][sink.second] = label;
  for (unsigned int i = 0; i < graph[sink.first][sink.second].size(); i++)
    expand(graph[sink.first][sink.second][i], label);
}

void solve(int T)
{
  cin >> H >> W;
  nsinks = 0;
  memset(labeling, -1, sizeof labeling);

  // frame it
  for (int i = 0; i < H+2; i++)
    for (int j = 0; j < W+2; j++)
      terrain[i][j] = 10000;

  for (int i = 0; i < H; i++)
    for (int j = 0; j < W; j++)
    {
      graph[i][j].clear();
      cin >> terrain[i+1][j+1];
    }

  for (int i = 0; i < H; i++)
    for (int j = 0; j < W; j++)
    {
      int minimum = terrain[i+1][j+1];
      int minima = -1;
      for (int k = 0; k < 4; k++)
      {
        int i2 = i+d[k][0], j2 = j+d[k][1];
        if (terrain[i2+1][j2+1] < minimum)
        {
          minimum = terrain[i2+1][j2+1];
          minima = k;
        }
      }

      if (minima < 0)
      {
        sinks[nsinks++] = make_pair(i, j);
        //printf("%d, %d is a sink\n", i, j);
      }
      else
      {
        graph[i + d[minima][0]][j + d[minima][1]].push_back(make_pair(i, j));
        //printf("flow from %d, %d to %d, %d\n", i, j, i+d[minima][0], j+d[minima][1]);
      }
    }

  //cout << "sinks: " << nsinks << endl;

  for (int i = 0; i < nsinks; i++)
    expand(sinks[i], i);

  int label = 0;
  map<int, char> labels;

  printf("Case #%d:\n", T);
  for (int i = 0; i < H; i++)
    for (int j = 0; j < W; j++)
    {
      if (!labels[labeling[i][j]])
        labels[labeling[i][j]] = 'a' + label++;
      printf("%c%c", labels[labeling[i][j]], j+1==W?'\n':' ');
    }
}

int main()
{
  int T;
  cin >> T;

  for (int i = 0; i < T; i++)
    solve(i+1);

  return 0;
}
