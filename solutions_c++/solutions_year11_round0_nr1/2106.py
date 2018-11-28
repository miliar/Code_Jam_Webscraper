#include <stdio.h>
#include <queue>

using namespace std;

struct Task
{
  int dest;
  int nr;
  Task(int _dest, int _nr) { dest=_dest; nr=_nr; }
};

// 0 - koniec
// 1 - wcisnieto
// cokolwiek innego: ruch lub czekanie
int makemove(queue<Task>& t, int& pos, const int turn)
{
  if (t.empty())
    return 0;
  const Task curr = t.front();
  if (curr.dest==pos)
    {
      if (turn==curr.nr)
        {
          t.pop();
          return 1;
        }
    }
  else if (curr.dest<pos)
    pos--;
  else
    pos++;
  return 0;
}

int main()
{
  int d;
  scanf("%d",&d);
  for (int p=1; p<=d; p++)
    {
      int n;
      scanf("%d",&n);
      queue<Task> tasko,taskb;
      for (int i=1; i<=n; i++)
        {
          char c[2];
          int dest;
          scanf("%s%d",c,&dest);
          if (c[0]=='O')
            tasko.push(Task(dest,i));
          else
            taskb.push(Task(dest,i));
        }
      int poso = 1;
      int posb = 1;
      int time=0;
      int turn=1;
      int ret1,ret2;
      do
        {
          time++;
          ret1 = makemove(tasko, poso, turn);
          ret2 = makemove(taskb, posb, turn);
          if (ret1 || ret2)
            turn++;
        }
      while(!tasko.empty() || !taskb.empty());
      printf("Case #%d: %d\n",p,time);
    }
  return 0;
}
