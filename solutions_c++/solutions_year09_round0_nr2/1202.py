#include <cstdio>
#include <utility>
#include <map>

using namespace std;

typedef pair<int, int> Point; // First is y, second is x
const Point InvalidPoint = make_pair(-1, -1);

const int MAXW = 150;
const int MAXH = 150;

typedef map<Point, char> SinkNames;
typedef int Landscape[MAXH][MAXW];
typedef Point Sinks[MAXH][MAXW];

void fall(const Landscape &land, Sinks &sinks, int w, int h, int x, int y)
{
  if (sinks[y][x] != InvalidPoint)
    return; // have already been here

  // Offsets: South, East, West, North
  static const int dx[4] = { 0, 1, -1, 0};
  static const int dy[4] = { 1, 0, 0, -1};

  Point fall_to = InvalidPoint;
  int next_alt = land[y][x]-1;
  for (int i=0; i<4; i++)
  {
    if (x+dx[i]<0 || x+dx[i]>=w || y+dy[i]<0 || y+dy[i]>=h)
      continue; // Edge here
    if (land[y+dy[i]][x+dx[i]]<=next_alt)
    {
      fall_to = make_pair(y+dy[i], x+dx[i]);
      next_alt = land[y+dy[i]][x+dx[i]];
    }
  }
  if (fall_to == InvalidPoint)
    sinks[y][x] = make_pair(y, x); // A new sink
  else
  {
    fall(land, sinks, w, h, fall_to.second, fall_to.first);
    sinks[y][x] = sinks[fall_to.first][fall_to.second];
  }
}

int main()
{
  Sinks sinks;
  Landscape landscape;
  SinkNames sink_names;
  int t;
  scanf("%d", &t);
  for (int test_case=0; test_case<t; test_case++)
  {
    int h, w;
    scanf("%d %d", &h, &w);
    for (int y=0; y<h; y++)
      for (int x=0; x<w; x++)
      {
        int alt;
        scanf("%d", &alt);
        landscape[y][x] = alt;
        sinks[y][x] = InvalidPoint;
      }
    for (int y=0; y<h; y++)
      for (int x=0; x<w; x++)
        fall(landscape, sinks, w, h, x, y);

    // Mark sinks
    sink_names.clear();
    char letter = 'a';
    for (int y=0; y<h; y++)
      for (int x=0; x<w; x++)
      {
        Point p = sinks[y][x];
        if (sink_names.count(p)==0)
          sink_names[p] = letter++;
      }

    printf("Case #%d:\n", test_case+1);
    for (int y=0; y<h; y++)
    {
      for (int x=0; x<w; x++)
        printf("%c ", sink_names[sinks[y][x]]);
      printf("\n");
    }
  }
}

