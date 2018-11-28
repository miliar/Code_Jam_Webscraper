#include <iostream>
#include <vector>
#include <assert.h>
#include <stdlib.h>

#define DEBUG 0

using namespace std;

typedef vector<vector<int> > map_t;


struct Point
{
  Point() : x(0), y(0)
  { }

  Point(int _x, int _y) : x(_x), y(_y)
  { }

  bool operator==(const Point& p)
  {
    return x == p.x && y == p.y;
  }

  int x, y;
};

inline std::ostream& operator <<(std::ostream& os, const Point& p)
{
	os << "(" << p.x << ", " << p.y << ")";
	return os;
}

template<class T> inline std::ostream& operator <<(std::ostream& os, const std::vector<T>& v)
{
	os << '[';
	for(int i = 0; i < int(v.size())-1; i++) {
		os << v[i] << ", ";
	}
	if(!v.empty())
		os << v.back();
	os << ']';
	return os;
}

int width(const map_t& map)
{
  return map.size();
}

int height(const map_t& map)
{
  return map[0].size();
}

map_t create_map(int w, int h)
{
     return vector<vector<int> >(w, vector<int>(h));
}

vector<Point> find_sinks(const map_t& map)
{
  vector<Point> ret;
  for(int y = height(map)-1; y >= 0; y--) {
    for(int x = 0; x < width(map); x++) {
      if(0 <= x-1 && map[x-1][y] < map[x][y])
	continue;

      if(x+1 < width(map) && map[x+1][y] < map[x][y])
	continue;

      if(0 <= y-1 && map[x][y-1] < map[x][y])
	continue;

      if(y+1 < height(map) && map[x][y+1] < map[x][y])
	continue;
      
      Point p(x, y);
      ret.push_back(p);
    }
  }

  //  assert(ret.size() <= 26);
  return ret;
}

bool legal(const map_t& map, int x, int y)
{
  return 0 <= x && x < width(map) && 0 <= y && y < height(map);
}

// If true, then water flows from (fx, fy) to (*tx, *ty).
bool flow_to(const map_t& map, int fx, int fy, int* tx, int* ty)
{
  if(!legal(map, fx, fy))
    return false;

  int minx = -1, miny = -1;
  int mina = 1000000;

  if(legal(map, fx, fy+1) && map[fx][fy+1] < mina) {
    minx = fx;
    miny = fy+1;
    mina = map[fx][fy+1];
  }

  if(legal(map, fx-1, fy) && map[fx-1][fy] < mina) {
    minx = fx-1;
    miny = fy;
    mina = map[fx-1][fy];
  }

  if(legal(map, fx+1, fy) && map[fx+1][fy] < mina) {
    minx = fx+1;
    miny = fy;
    mina = map[fx+1][fy];
  }

  if(legal(map, fx, fy-1) && map[fx][fy-1] < mina) {
    minx = fx;
    miny = fy-1;
    mina = map[fx][fy-1];
  }

  if(mina < map[fx][fy]) {
    *tx = minx;
    *ty = miny;
    return true;
  } else {
    return false;
  }
}

map_t label_map(const map_t& alts)
{
  vector<Point> ps(find_sinks(alts));

  map_t ret(create_map(width(alts), height(alts)));

  for(int x = 0; x < width(ret); x++) {
    for(int y = 0; y < height(ret); y++) {
      ret[x][y] = -1;
    }
  }

  for(int i = 0; i < ps.size(); i++) {
    Point p(ps[i]);
    ret[p.x][p.y] = i;
  }

  while(!ps.empty()) {
    if(DEBUG)
      cout << ps << endl;

    int x = ps.back().x;
    int y = ps.back().y;
    ps.pop_back();


    assert(ret[x][y] != -1);
    int tx, ty;
    if(flow_to(alts, x+1, y, &tx, &ty) && x == tx && y == ty) {
      ret[x+1][y] = ret[x][y];

      //      cout << "Adding " << x+1 << ' ' << y << endl;
      ps.push_back(Point(x+1, y));
    }
    if(flow_to(alts, x-1, y, &tx, &ty) && x == tx && y == ty) {
      ret[x-1][y] = ret[x][y];

      //      cout << "Adding " << x-1 << ' ' << y << endl;
      ps.push_back(Point(x-1, y));
    }
    if(flow_to(alts, x, y+1, &tx, &ty) && x == tx && y == ty) {
      ret[x][y+1] = ret[x][y];

      //      cout << "Adding " << x << ' ' << y+1 << endl;
      ps.push_back(Point(x, y+1));
    }
    if(flow_to(alts, x, y-1, &tx, &ty) && x == tx && y == ty) {
      ret[x][y-1] = ret[x][y];

      //      cout << "Adding " << x << ' ' << y-1 << endl;
      ps.push_back(Point(x, y-1));
    }
  }

  return ret;
}

void print_map(const map_t& map)
{
  for(int y = height(map)-1; y >= 0; y--) {
    for(int x = 0; x < width(map); x++) {
      cout << map[x][y] << ' ';
    }
    cout << endl;
  }
}

void print_map_c(const map_t& map)
{
  vector<int> cm(27, -1);

  int cur = 0;
  for(int y = height(map)-1; y >= 0; y--) {
    for(int x = 0; x < width(map); x++) {
      if(cm[map[x][y]] == -1) {
	cm[map[x][y]] = cur;
	cur++;
      }
    }
  }

  for(int y = height(map)-1; y >= 0; y--) {
    for(int x = 0; x < width(map); x++) {
      cout << char('a'+cm[map[x][y]]) << ' ';
    }
    cout << endl;
  }
}

int main(int argc, char** argv)
{
  int startT = 0;
  if(argc > 1)
    startT = atoi(argv[1]);

  int T;
  cin >> T;
  for(int i = 0; i < T; i++) {
    int H, W;
    cin >> H;
    cin >> W;

    if(DEBUG)
      cout << "Got W: " << W << " H: " << H << endl;

    map_t alts(create_map(W, H));

    for(int y = H-1; y >= 0; y--) {
      for(int x = 0; x < W; x++) {
	cin >> alts[x][y];
      }
    }

    if(DEBUG) {
      cout << "alts:\n";
      print_map(alts);
      cout << endl;
    }

    if(i < startT)
      continue;
    map_t res(label_map(alts));

    cout << "Case #" << i+1 << ':' << endl;
    print_map_c(res);
  }
}
