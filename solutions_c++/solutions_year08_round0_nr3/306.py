#include <iostream>
#include <math.h>

double cut_x(double x, double d)
{
  if (x >= d)
    return 0.0;
  return sqrt(d * d - x * x);
}

double cut_y(double y, double d)
{
  if (y >= d)
    return 0.0;
  return sqrt(d * d - y * y);
}

double sector(double x1, double y1, double x2, double y2)
{
  double cos_factor = (x1 * x2 + y1 * y2) / (x1 * x1 + y1 * y1);
  double angle = acos(cos_factor);
  //std::cerr << "sector((" << x1 << ", " << y1 << "), (" << x2 << ", " << y2 << ")) cos=" << cos_factor << " angle=" << acos(cos_factor) / M_PI * 180;
  return (x1 * x1 + y1 * y1) * M_PI * (angle / (2 * M_PI)) - (x2 * y1 - x1 * y2) / 2;
}

void calc()
{
  double f, R, t, r, g;
  std::cin >> f >> R >> t >> r >> g;

  const double scale = 2 * r + g;
  const double a = (g / 2 - f) / scale;
  const double d = (R - t - f) / scale;
  const double D = R / scale;

  if (a <= 0) {
    std::cerr << "Sure hit" << std::endl;
    std::cout << "1.000000" << std::endl;
    return;
  }
  std::cerr << "a=" << a << ", d=" << d << ", D=" << D << std::endl;

  double sum = 0.0, last = 0.0;

  int x = 0;
  int y = D;
  while (true) {
    sum += last;
    std::cerr << " area=" << last << " (sum=" << sum << ")" << std::endl;
    std::cerr << "x=" << x << ", y=" << y << ": ";
    const double left = x + 0.5 - a;
    const double right = x + 0.5 + a;
    const double top = y + 0.5 + a;
    const double bottom = y + 0.5 - a;
    double top_cut = cut_y(top, d);
    if (top_cut >= right) {
      std::cerr << "All";
      last = (2 * a) * (2 * a);
      if (x == y)
        break;
      x++;
      continue;
    }
    double bottom_cut = cut_y(bottom, d);
    if (bottom_cut <= left) {
      std::cerr << "None";
      last = 0;
      if (x == y)
        break;
      sum += x * (2 * a) * (2 * a);
      y--;
      continue;
    }
    if (top_cut > left) {
      std::cerr << "All except upper right triangle";
      double right_cut = cut_x(right, d);
      if (right_cut < bottom)
        abort();
      last = (2 * a) * (2 * a)
        - (right - top_cut) * (top - right_cut) / 2
        + sector(top_cut, top, right, right_cut);
      if (x == y)
        break;
      x++;
      continue;
    }
    if (bottom_cut >= right) {
      std::cerr << "Bottom half";
      double left_cut = cut_x(left, d);
      double right_cut = cut_x(right, d);
      last = a * ((left_cut - bottom) + (right_cut - bottom))
        + sector(left, left_cut, right, right_cut);
      if (x == y)
        break;
      x++;
      continue;
    }
    std::cerr << "Bottom left triangle";
    double left_cut = cut_x(left, d);
    last = (bottom_cut - left) * (left_cut - bottom) / 2
      + sector(left, left_cut, bottom_cut, bottom);
    if (x == y)
      break;
    sum += x * (2 * a) * (2 * a);
    y--;
    continue;
  }
  sum += last / 2;
  std::cerr << " area=" << last << " / 2 (sum=" << sum << ")" << std::endl;
  std::cerr << "Bottom area " << ((y * y) / 2.0) * (2 * a) * (2 * a) << std::endl;
  sum += ((y * y) / 2.0) * (2 * a) * (2 * a);
  std::cerr << "sum=" << sum << " total=" << (D * D / 8.0 * M_PI) << std::endl;
  std::cout << (1 - sum / (D * D / 8.0 * M_PI)) << std::endl;
}

int main()
{
  std::cout.precision(6);
  std::cout.setf ( std::ios::fixed, std::ios::floatfield );
  size_t count;
  std::cin >> count;
  for (size_t i = 0; i < count; i++) {
    std::cout << "Case #" << (i + 1) << ": ";
    calc();
  }
}
