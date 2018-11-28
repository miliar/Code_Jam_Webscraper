#include <iostream>
#include <queue>
#include <algorithm>
#include <deque>
#include <vector>
#include <cmath>
#include <map>
#include <string>
#include <set>
#include <numeric>
#include <cassert>

using namespace std;
  
const int maxW = 100;

int T,H,W;
  
int heights[maxW][maxW];
bool visited[maxW][maxW];
char letters[maxW][maxW];

char next_letter;

int dx[] = {0,-1, 1, 0};
int dy[] = {-1,0, 0, 1};

char dfs(int y, int x) {
  if (visited[y][x])
    return letters[y][x];
  int lowest = heights[y][x];
  int lowest_d = -1;
  for (int d = 0 ; d < 4 ; d++) {
    int ny = y + dy[d];
    int nx = x + dx[d];
    if (ny >= 0 && nx >= 0 && ny < H && nx < W) {
      if (heights[ny][nx] < lowest) {
	lowest = heights[ny][nx];
	lowest_d = d;
      }
    }
  }
  char l;
  if (lowest_d == -1) {
    l = next_letter++;
  } else {
    l = dfs(y + dy[lowest_d], x + dx[lowest_d]);
  }
  visited[y][x] = true;
  letters[y][x] = l;  
  return l;
}

int main() {

  cin>>T;
  for (int tt = 1 ; tt <= T ; tt++) {
    next_letter = 'a';
    cin>>H>>W;
    for (int i = 0 ; i < H  ; i++) {
      for (int j = 0 ; j < W ; j++) {
	cin>>heights[i][j];
      }
    }
    fill(*visited, *visited+maxW*maxW, false);	 
    cout << "Case #" << tt << ":\n";
    for (int i = 0 ; i < H ; i++) {
      for (int j = 0 ; j < W ; j++) {
	if (j) cout << " ";
	cout << dfs(i,j);
      }
      cout << endl;
    }    
  }
}
