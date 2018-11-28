#include <cstdio>
#include <vector>
#include <cstring>
#include <queue>
#include <algorithm>

struct coord {
  int x, y, alt;
  coord() {x=y=alt=1000000;}
  coord(int _x, int _y, int _alt) {x = _x; y = _y; alt = _alt;}
  bool operator<(struct coord const &o) const {
    if(alt!=o.alt) return alt<o.alt;
    if(y!=o.y) return y<o.y;
    return x<o.x;
  }
};

int main()
{
  int T;
  int array[100][100];
  char map[100][100];
  scanf("%d", &T);
  for(int t=1; t<=T; ++t) {
    int H, W;
    std::vector<std::pair<int, int> > connections[100][100];
    scanf("%d%d", &H, &W);
    for(int i=0; i<H; ++i)
      for(int j=0; j<W; ++j)
	scanf("%d", &array[i][j]);
    for(int i=0; i<H; ++i)
      for(int j=0; j<W; ++j) {
	coord best;
	if(i)
	  best = std::min(best, coord(j, i-1, array[i-1][j]));
	if(j)
	  best = std::min(best, coord(j-1, i, array[i][j-1]));
	if(i<H-1)
	  best = std::min(best, coord(j, i+1, array[i+1][j]));
	if(j<W-1)
	  best = std::min(best, coord(j+1, i, array[i][j+1]));
	if(best.alt < array[i][j]) {
	  connections[i][j].push_back(std::make_pair(best.y, best.x));
	  connections[best.y][best.x].push_back(std::make_pair(i, j));
	}
      }
    memset(map, 0, sizeof(map));
    char c = 'a';
    for(int i=0; i<H; ++i)
      for(int j=0; j<W; ++j)
	if(!map[i][j]) {
	  std::queue<std::pair<int, int> > q;
	  q.push(std::make_pair(i, j));
	  while(!q.empty()) {
	    int const x = q.front().second, y = q.front().first;
	    char &rc = map[y][x];
	    std::vector<std::pair<int, int> > &rv = connections[y][x];
	    if(!rc) {
	      rc = c;
	      for(std::vector<std::pair<int, int> >::const_iterator
		    it = rv.begin(); it != rv.end(); ++it)
		q.push(*it);
	    }
	    q.pop();
	  }
	  ++c;
	}
    printf("Case #%d:\n", t);
    for(int i=0; i<H; ++i) {
      printf("%c", map[i][0]);
      for(int j=1; j<W; ++j)
	printf(" %c", map[i][j]);
      putchar('\n');
    }
  }
  return 0;
}
