#include <cstdio>
#include <cmath>
using namespace std;

void fun(int casenr)
{
  int n;
  scanf("%d", &n);
  double sx = 0, 
         svx = 0, 
         sy = 0, 
         svy = 0, 
         sz = 0, 
         svz = 0;
  int x, y, z, vx, vy, vz;
  for(int i=0;i<n;++i)
  {
    scanf("%d%d%d%d%d%d", &x, &y, &z, &vx, &vy, &vz);
    sx += x;
    sy += y;
    sz += z;
    svx += vx;
    svz += vz;
    svy += vy;
  }

  sx /= n;
  sy /= n;
  sz /= n;
  svx /= n;
  svy /= n;
  svz /= n;
  
  double t = 0.0;
  //printf("dane: %lf %lf %lf\n", svx, svy, svz);

  if(svx != 0 || svy != 0 || svz != 0)
    t = -(sx * svx + sy * svy + sz * svz)/(svx*svx + svy*svy + svz*svz);

  if(t <= 0.0)
    t = 0.0;

  double d = sqrt((sx + t*svx)*(sx + t*svx) 
    + (sy + t*svy)*(sy + t*svy)
    + (sz + t*svz)*(sz + t*svz));

  printf("Case #%d: %.8lf %.8lf\n", casenr, d, t);
}

int main()
{
  int t;
  scanf("%d", &t);
  for(int i=0;i<t;++i)
    fun(i + 1);
  return 0;
}

