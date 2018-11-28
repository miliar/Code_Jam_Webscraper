#include <cstdio>
#include <cstring>

int h, w;

struct point
{
  int x, y;
  point(int x=0, int y=0) : x(x), y(y) {}
  point operator+(const point &p) const { return point(x + p.x, y + p.y); }
  bool operator==(const point &p) const { return x == p.x && y == p.y; }
  bool operator!=(const point &p) const { return !(*this == p); }
  bool isvalid() const { return x >= 0 && y >= 0 && x < w && y < h; }
};

//          X    Y
int height[110][110];
point sink[110][110];
char chr[110][110];
char map[110][110];

point desl[4] = { point(0, -1), point(-1, 0), point(1, 0), point(0, 1) };

point getsink(int x, int y)
{
  if(sink[x][y] != point(-1, -1))
    return sink[x][y];

  point p(x, y);
  point nextpoint = p;
  int bestheight = height[p.x][p.y];

  for(int i=0; i<4; ++i)
    {
      point np = p + desl[i];
      if(np.isvalid() && height[np.x][np.y] < bestheight)
	{
	  bestheight = height[np.x][np.y];
	  nextpoint = np;
	}
    }

  if(bestheight == height[p.x][p.y])
    return point(x, y);

  return sink[x][y] = getsink(nextpoint.x, nextpoint.y);
}

int main()
{
  int ntests;
  scanf(" %d", &ntests);
  for(int test = 1; test <= ntests; ++test)
    {
      for(int i=0; i<110; ++i)
	for(int j=0; j<110; ++j)
	  sink[i][j] = point(-1, -1);

      scanf(" %d %d", &h, &w);
      for(int r = 0; r < h; ++r)
	for(int c = 0; c < w; ++c)
	  scanf(" %d", &height[c][r]);

      memset(chr, -1, sizeof(chr));

      char now = 'a';
      for(int j=0; j<h; ++j)
	for(int i=0; i<w; ++i)
	  {
	    point p = getsink(i, j);
	    if(chr[p.x][p.y] == -1)
	      chr[p.x][p.y] = now++;
	    map[i][j] = chr[p.x][p.y];
	  }

      printf("Case #%d:\n", test);
      for(int r=0; r<h; ++r)
	{
	  char *spc = "";
	  for(int c=0; c<w; ++c)
	    {
	      printf("%s%c", spc, map[c][r]);
	      spc = " ";
	    }
	  printf("\n");
	}
    }
  return 0;
}
