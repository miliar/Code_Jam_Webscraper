#include <iostream>
#include <vector>


int W, H;

int data[102][102];
int map[102][102];
const int MINT = 200000;
int curcol;
void Clear()
{
  for (int i = 0; i < H+2; ++i)
    for (int j = 0; j < W+2; ++j)
    {
      data[i][j] = 0;
    }
  for (int i = 0; i < H+2; ++i)
    for (int j = 0; j < W+2; ++j)
    {
      map[i][j] = MINT;
    }
}

bool Decide(int x, int y, int &nx, int &ny)//true = sink
{
  int val = map[x][y];
  int min = val;
  if (map[x-1][y] < min)
  {
    min = map[x-1][y];
    nx = x-1;
    ny = y;
  }
  if (map[x][y-1] < min)
  {
    min = map[x][y-1];
    nx = x;
    ny = y-1;
  }
  if (map[x][y+1] < min)
  {
    min = map[x][y+1];
    nx = x;
    ny = y+1;
  }
  if (map[x+1][y] < min)
  {
    min = map[x+1][y];
    nx = x+1;
    ny = y;
  }
  return min==val;
}

void Paint(int x, int y)
{
  if (data[x][y])
    return;
  int nx, ny;
  std::vector<int> points;
  int col;
  do{
    points.push_back(x);
    points.push_back(y);
    data[x][y] = -1;
    bool exit = Decide(x, y, nx, ny);
    if (exit)
    {
      col = curcol++;
      break;
    }
    if (data[nx][ny]>0)
    {
      col = data[nx][ny];
      break;
    }
    x = nx;
    y = ny;
  }while(true);
  for (int i = 0; i < points.size(); i+=2)
  {
    data[points[i]][points[i+1]] = col;
  }    
}

void Color()
{
  curcol = 1;
  for (int i = 1; i <=H; ++i)
    for (int j = 1; j <=W; ++j)
      Paint(i,j);
  //  std::cout << curcol -1 << " colors" <<  std::endl;
}

void Output()
{
  for (int i = 0; i < H; ++i)
  {
    for(int j = 0; j < W; ++j)
      std::cout << char('a'-1 + data[i+1][j+1]) << " ";
    std::cout << std::endl;
  }
}

int main()
{
  int T;
  std::cin >> T;
  for (int t = 0; t < T; ++t)
  {
    std::cin >>H >> W;
    Clear();
    for (int i = 0; i < H; ++i)
      for (int j = 0; j < W; ++j)
	std::cin >> map[i+1][j+1];
    Color();
    std::cout << "Case #" << (t+1) << ":\n";
    Output();
  }
}
