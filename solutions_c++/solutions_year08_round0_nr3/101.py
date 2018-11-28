#include <iostream>
#include <math.h>

using namespace std;

const double eps = 1e-8;
const double pi = acos(-1.0);

int N;
double f, R, t, r, g;
double top;

double total_area;

double
AreaCon(double left, double right)
{
  if (right > top)
  {
    right = top;
  }

  double ang1 = acos(left / R);
  double ang2 = acos(right / R);
  double delta = ang1 - ang2;
  double area_plus = (delta - sin(delta)) * R * R / 2.0;
  double a = left * tan(ang1) - left;
  if (left < eps)
  {
    a = R;
  }
  double b = right * tan(ang2) - right;
  return (a + b) * (right - left) / 2.0 + area_plus;
}

double
AreaDis(double left, double right)
{
  if (right > top)
  {
    right = top;
  }

  double ang1 = acos(left / R);
  double ang2 = acos(right / R);
  double delta = ang1 - ang2;
  double area_plus = (delta - sin(delta)) * R * R / 2.0;
  double a = left * tan(ang1) - left;
  double b = right * tan(ang2) - right;

  double y1 = left * tan(ang1);
  double y2 = right * tan(ang2);
  double step = 2 * r + g;
  int k = (int)floor((y2 - r) / step);
  int cnt = k - (int)floor((right - r) / step);

  double lower = r + step * k + g;
  double upper = lower + 2 * r;
  double addition;
  if (lower + eps < y1 && y1 <= upper && lower + eps < y2 && y2 <= upper)
  {
    double t1 = y1 - lower;
    double t2 = y2 - lower;
    addition = area_plus + (t1 + t2) * (right - left) / 2.0;
  }
  else
  {
    addition = 0.0;
  }
  return cnt * (right - left) * 2 * r + addition;
}

int main()
{
  double sum, area_plus;
  cin >> N;
  for (int e = 1; e <= N; ++e)
  {
    cout << "Case #" << e << ": ";
    cin >> f >> R >> t >> r >> g;
    
    if (2.0 * f >= g - eps)
    {
      cout << 1.0 << endl;
      continue;
    }
    total_area = pi * R * R;
    g -= 2 * f;
    R -= t + f;
    r += f;
    area_plus = total_area - pi * R * R;

    double head, tail, step;
    top = R / sqrt(2.0);
    step = 2 * r + g;

    /*
    cout << endl << "total: " << total_area << endl;
    cout << "plus: " << area_plus << endl;
    cout << "top: " << top << endl;
    */
    //cout << f << ' ' << R << ' ' << t << ' ' << r << ' ' << g << endl;

    sum = AreaCon(0, r);
    //printf("[%lf %lf] %lf\n", 0.0, r, sum);

    head = r + g;
    tail = head + 2 * r;
    //printf("%lf %lf %lf\n", head, tail, top);
    for (; head < top; head += step, tail += step)
    {
      sum += AreaCon(head, tail);
      //printf("[%lf %lf] %lf\n", head, tail, sum);
    }

    head = r;
    tail = head + g;
    for (; head < top; head += step, tail += step)
    {
      if (tail > top)
      {
	tail = top;
      }
      double u, v;
      double delta = g / 4096;
      for (u = head, v = head + delta; v <= tail; u += delta, v += delta)
      {
	sum += AreaDis(u, v);
	//printf("[%lf %lf] %lf\n", u, v, sum);
      }
      sum += AreaDis(u, tail);
    }

    printf("%lf\n", (8 * sum + area_plus) / total_area);
  }
}

