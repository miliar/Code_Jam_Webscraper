#include<iostream>
#include<map>
#include<vector>

struct basin
{
  int x,y;
  bool operator<(const basin& b)const
  {
    if(x!=b.x)return x<b.x;
    return y<b.y;
  }
};

int map[100][100];
basin memo[100][100];
int callcount = 0;

int H,W;
int ca = 1;

basin solve(int,int);
void solve_map()
{
  std::cin>>H>>W;
  for(int i=0;i<H;i++)
  {
    for(int j=0;j<W;j++)
    {
      std::cin>>map[i][j];
      memo[i][j].x = -1;
    }
  }
  for(int i=0;i<H;i++)
  {
    for(int j=0;j<W;j++)
    {
      solve(j,i);
    }
  }
  char current_char = 'a';
  std::map<basin,char> bm;
  std::cout<<"Case #"<<ca<<":\n";
  for(int i=0;i<H;i++)
  {
    for(int j=0;j<W;j++)
    {
      basin b = memo[i][j];
      if(bm.count(b)==0)
        bm[b] = current_char++;
      std::cout<<bm[b]<<" ";
    }
    std::cout<<"\n";
  }
  ca++;
}

basin solve(int x,int y)
{
  int lowest = map[y][x];
  callcount++;
  if(memo[y][x].x!=-1)return memo[y][x];
  basin t;
  t.x = x;
  t.y = y;
  if(y!=0)
  {
    if(map[y-1][x]<lowest)
    {
      lowest = map[y-1][x];
      t = solve(x,y-1);
    }
  }
  if(x!=0)
  {
    if(map[y][x-1]<lowest)
    {
      lowest = map[y][x-1];
      t = solve(x-1,y);
    }
  }
  if(x!=W-1)
  {
    if(map[y][x+1]<lowest)
    {
      lowest = map[y][x+1];
      t = solve(x+1,y);
    }
  }
  if(y!=H-1)
  {
    if(map[y+1][x]<lowest)
    {
      lowest = map[y+1][x];
      t = solve(x,y+1);
    }
  }
  memo[y][x] = t;
  return t;

}

int main()
{
  int T;
  std::cin>>T;
  for(int i=0;i<T;i++)
    solve_map();
}




