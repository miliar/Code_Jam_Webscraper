#include <map>
#include <list>
#include <algorithm>
#include <iostream>
#include <math.h>

struct point_t {
  inline point_t() {}
  inline point_t(double x, double y): x(x), y(y) {}
  double x, y;
};

point_t intersect(point_t a1, point_t a2, point_t b1, point_t b2)
{
  point_t da = a2;
  da.x -= a1.x; da.y -= a1.y;

  point_t nb;
  nb.x = b2.y - b1.y;
  nb.y = b1.x - b2.x;

  double t = (nb.x * (b1.x - a1.x) + nb.y * (b1.y - a1.y))
    / (da.x * nb.x + da.y * nb.y);

  return point_t(a1.x + t * da.x, a1.y + t * da.y);
}

point_t intersect_rect(point_t a1, point_t a2, point_t b1, point_t b2)
{
  point_t da;
  da.x = a2.y - a1.y;
  da.y = a1.x - a2.x;

  point_t nb = b2;
  nb.x -= b1.x; nb.y -= b1.y;

  double t = (nb.x * (b1.x - a1.x) + nb.y * (b1.y - a1.y))
    / (da.x * nb.x + da.y * nb.y);

  return point_t(a1.x + t * da.x, a1.y + t * da.y);
}

void calc()
{
  int ax1, ax2, ax3;
  int ay1, ay2, ay3;
  int bx1, bx2, bx3;
  int by1, by2, by3;
  std::cin >> ax1 >> ay1 >> ax2 >> ay2 >> ax3 >> ay3;
  std::cin >> bx1 >> by1 >> bx2 >> by2 >> bx3 >> by3;
  if (ax1 == bx1 && ay1 == by1) {
    std::cout << ax1 << " " << ay1 << std::endl;
    return;
  }
  if (ax2 == bx2 && ay2 == by2) {
    std::cout << ax2 << " " << ay2 << std::endl;
    return;
  }
  if (ax3 == bx3 && ay3 == by3) {
    std::cout << ax3 << " " << ay3 << std::endl;
    return;
  }

  point_t a1(ax1, ay1);
  point_t a2(ax2, ay2);
  point_t b1(bx1, by1);
  point_t b2(bx2, by2);

  point_t inter = intersect(a1, b1, a2, b2);
  point_t r1 = intersect_rect(a1, b1, a2, b2);
  point_t r2 = intersect_rect(b1, a1, b2, a2);

  //std::cerr << "inter = (" << inter.x << ", " << inter.y << ")" << std::endl;
  //std::cerr << "r1 = (" << r1.x << ", " << r1.y << ")" << std::endl;
  //std::cerr << "r2 = (" << r2.x << ", " << r2.y << ")" << std::endl;

  r1.x -= inter.x;
  r1.y -= inter.y;
  r2.x -= inter.x;
  r2.y -= inter.y;
  r1.x /= 2;
  r1.y /= 2;
  r2.x /= 2;
  r2.y /= 2;
  point_t s = r1;
  r1.x += inter.x;
  r1.y += inter.y;
  r2.x += inter.x;
  r2.y += inter.y;

  point_t n;
  n.x = r2.y - r1.y;
  n.y = r1.x - r2.x;
  double scale = sqrt(n.x * n.x + n.y * n.y);
  n.x /= scale;
  n.y /= scale;

  //std::cerr << "s = (" << s.x << ", " << s.y << ")" << std::endl;
  //std::cerr << "n = (" << n.x << ", " << n.y << ")" << std::endl;

  double f =  (n.x * s.x + n.y * s.y);
  
  //std::cerr << "f= " << f << std::endl;

  point_t con = inter;
  con.x += n.x * f * 2;
  con.y += n.y * f * 2;
    
  std::cout << con.x << " " << con.y << std::endl;
}

int main()
{ 
  std::cout.setf ( std::ios::fixed, std::ios::floatfield );
  std::cout.precision(6);
  size_t count;
  std::cin >> count;
  for (size_t i = 0; i < count; i++) {
    std::cout << "Case #" << (i + 1) << ": ";
    calc();
  }
}

