#include <cstdio>
#include <cmath>
using namespace std;

int		robot_trust(int);

int		main(void)
{
  int		T, Tb;

  scanf("%d", &T);
  for (int Ti = 1; Ti <= T; ++Ti)
  {
    scanf("%d ", &Tb);
    printf("Case #%d: %d\n", Ti, robot_trust(Tb));
  }
  return 0;
}

int		robot_trust(int Tb)
{
  int		pos[2] = {1, 1};
  int		res = 0, time_acc = 0, button, tmp;
  char		robot, last_robot = '#';

  while (Tb --> 0)
  {
    scanf("%c %d ", &robot, &button);
    tmp = abs(button - pos[robot == 'O' ? 0 : 1]) + 1;
    pos[robot == 'O' ? 0 : 1] = button;
    if (last_robot == '#' || last_robot == robot)
    {
      time_acc += tmp;
      res += tmp;
    }
    else
    {
      tmp -= time_acc;
      if (tmp <= 0)
      {
	time_acc = 1;
	tmp = 1;
      }
      else time_acc = tmp;
      res += tmp;
    }
    last_robot = robot;
  }
  return res;
}
