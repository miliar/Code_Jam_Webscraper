#include <stack>
#include <vector>
#include <string>
#include <iostream>
#include <fstream>
#include <limits>
using namespace std;



int mapCount;

struct POSITION { int x, y; };
typedef vector< vector<int> > MAP;
typedef vector< vector<char> > VISITED_MAP;
vector<MAP> mapList;


int Visit(const MAP &map, VISITED_MAP &visited, char Char, int x, int y)
{
  if (visited[y][x] != 0)
    return visited[y][x];


  const int INF_HEIGHT = numeric_limits<int>::max();
  const int W = (int)map[0].size();
  const int H = (int)map.size();

  const int n = (y > 0)     ? map[y-1][x] : INF_HEIGHT;
  const int w = (x > 0)     ? map[y][x-1] : INF_HEIGHT;
  const int e = (x < W - 1) ? map[y][x+1] : INF_HEIGHT;
  const int s = (y < H - 1) ? map[y+1][x] : INF_HEIGHT;
  const int X = map[y][x];

  int dx, dy;
  dx = dy = 0;

  const int lowest = min(n, min(w, min(e, s)));
  if (lowest >= X)
    ;
  else if (lowest == n) dy--;
  else if (lowest == w) dx--;
  else if (lowest == e) dx++;
  else if (lowest == s) dy++;

  if (dx || dy)
  {
    const char v = Visit(map, visited, Char, x + dx, y + dy);
    visited[y][x] = v;
  }
  else
  {
    visited[y][x] = Char;
  }

  return visited[y][x];
}



void Divide(ostream &output, const MAP &map)
{
  static int num = 0;

  VISITED_MAP visited;
  visited.resize(map.size());
  for (unsigned h = 0; h < visited.size(); h++)
    visited[h].resize(map[0].size());


  char Char = 'a';

  for (unsigned y = 0; y < map.size(); y++)
  {
    for (unsigned x = 0; x < map[0].size(); x++)
    {
      if (visited[y][x] == 0)
      {
        Char = 1 + Visit(map, visited, Char, x, y);
      }
    }
  }

  if (num++ > 0) output << "\n";
  output << "Case #" << num << ":";

  for (unsigned i = 0; i < map.size(); i++)
  {
    output << "\n";
    for (unsigned j = 0; j < map[0].size(); j++)
    {
      if (j > 0) output << " ";
      output << visited[i][j];
    }
  }

}



int main(int argc, char *argv[])
{
  if (argc != 3) return 1;

  ifstream inFile(argv[1]);
  ofstream outFile(argv[2]);

  if (inFile.fail() || outFile.fail()) return 1;


  string buf;

  // Get count of maps.
  {
    int T;
    inFile >> T;
    mapList.resize(T);
  }

  // Initialize maps.
  for (unsigned i = 0; i < mapList.size(); i++)
  {
    int H, W;
    inFile >> H >> W;

    MAP &map = mapList[i];
    map.resize(H);
    for (int h = 0; h < H; h++)
    {
      for (int w = 0; w < W; w++)
      {
        int a;
        inFile >> a;
        map[h].push_back(a);
      }
    }

    map.begin();
  }

  // Divide into regions. (Do output internal)
  for (unsigned m = 0; m < mapList.size(); m++)
  {
    Divide(outFile, mapList[m]);
  }

}