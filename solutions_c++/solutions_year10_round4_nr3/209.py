# include <iostream>
# include <string.h>
using namespace std;
int map[400][400];
int vmap[400][400];

bool step()
{
  int found=0;
  for(int i = 1; i < 400; i++)
    for(int j = 1; j < 400; j++)
    {
      if(map[i-1][j] && map[i][j-1])
        vmap[i][j] = 1;
      else if(!map[i-1][j] && !map[i][j-1])
        vmap[i][j] = 0;
      else
        vmap[i][j] = map[i][j];
      if(vmap[i][j])
        found++;
    }
  cerr << "found: " << found << "\n";
  return found;
}

int solve()
{
  int count = 0;

  while(step())
  {
    memcpy(map, vmap, sizeof map);
    count++;
  }

  return count + 1;
}

void fill(int x1, int y1, int x2, int y2)
{
  for(int i = x1; i <= x2; i++)
    for(int j = y1; j <= y2; j++)
      map[i][j] = 1;
}

void process(int cid)
{
  memset(map, 0, sizeof map);
  int r;
  cin >> r;
  while(r--)
  {
    int x1, y1, x2, y2;
    cin >> x1 >> y1 >> x2 >> y2;
    fill(x1, y1, x2, y2);
  }
  cout << "Case #" << cid << ": " << solve() << "\n";
}

int main()
{
  int cid=0;
  int n;
  cin >> n;
  while(n--)
    process(++cid);
}
