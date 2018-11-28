#include <cstdio>
#include <assert.h>

typedef int Map[100][100];
typedef char BasinsMap[100][100];

static const int EVEREST = 1000000;

void read(int& h, int& w, Map& map) {
  scanf("%d %d\n", &h, &w);
  for (int i = 0 ; i < h; ++i) {
    for(int j = 0; j < w; ++j) {
      scanf("%d", &map[i][j]);
    }
    scanf("\n");
  }
}

void emptyBasins(int h, int w, BasinsMap& basins) {
  for (int i = 0 ; i < h; ++i) {
    for(int j = 0; j < w; ++j) {
      basins[i][j] = '_';
    }
  }
}

void printBasins(int h, int w, BasinsMap& basins) {
  for (int i = 0 ; i < h; ++i) {
    for(int j = 0; j < w; ++j) {
      printf("%c", basins[i][j]);
      printf("%c", j == w - 1 ? '\n' : ' ');
    }
  }
}

typedef enum {N, W, E, S, SINK} Direction;

bool flow(int h, int w, const Map& map, int& i, int& j) {
  int myAlt = map[i][j];
  int nAlt = i > 0 ? map[i-1][j] : EVEREST;
  int wAlt = j > 0 ? map[i][j-1] : EVEREST;
  int eAlt = j < w - 1 ? map[i][j+1] : EVEREST;
  int sAlt = i < h - 1 ? map[i+1][j] : EVEREST;

  if (nAlt >= myAlt && wAlt >= myAlt && eAlt >= myAlt && sAlt >= myAlt) {
    return false;
  }
  Direction direction = SINK;
  int minAlt = myAlt;
  if (sAlt <= minAlt) {
    direction = S;
    minAlt = sAlt;
  }
  if (eAlt <= minAlt) {
    direction = E;
    minAlt = eAlt;
  }
  if (wAlt <= minAlt) {
    direction = W;
    minAlt = wAlt;
  }
  if (nAlt <= minAlt) {
    direction = N;
    minAlt = nAlt;
  }
  assert (direction != SINK);
  switch (direction) {
    case S: i++; break;
    case E: j++; break;
    case W: j--; break;
    case N: i--; break ;
  }
  return true;
}

void findSink(int h, int w, const Map& map, BasinsMap& basins, int i, int j, char& nextBasin) {
  if (basins[i][j] != '_') {
    return;
  }

  int ti = i;
  int tj = j;
  while (basins[ti][tj] == '_' && flow(h, w, map, ti, tj)) {}
  if (basins[ti][tj] == '_') {
    basins[ti][tj] = nextBasin;
    nextBasin++;
  }
  basins[i][j] = basins[ti][tj];
}

void solve(int n) {
  int h;
  int w;
  Map map;
  BasinsMap basins;
  read(h, w, map);
  emptyBasins(h, w, basins);
  char nextBasin = 'a';
  for (int i = 0 ; i < h; ++i) {
    for(int j = 0; j < w; ++j) {
      findSink(h, w, map, basins, i, j, nextBasin);
    }
  }
  printf("Case #%d:\n", n + 1);
  printBasins(h, w, basins);
}


int main() {
  int t;
  scanf("%d\n", &t);

  for (int i = 0; i < t; ++i) {
    solve(i);
  }
}
