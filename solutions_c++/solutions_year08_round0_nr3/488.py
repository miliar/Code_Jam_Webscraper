#include <iostream>
#include <sstream>
#include <cmath>
#include <vector>
#include <iomanip>

const double PI = std::atan(1.)*4.;

template<class T>
struct Point
{
  T x, y;
};

template<class T>
struct Line
{
  Point<T> p1, p2;
};

template<class T>
T Sqr(const T &a)
{
  return a*a;
}

template<class T>
void Read(T &a)
{
  std::string s;
  std::getline(std::cin, s);
  std::istringstream i(s);
  i >> a;
}
template<class T>
void Read(T &a0, T&a1, T&a2, T&a3, T&a4 )
{
  std::string s;
  std::getline(std::cin, s);
  std::istringstream i(s);
  i >> a0 >> a1 >> a2 >> a3 >> a4;
}

template<class T>
bool Intersect(Line<T> &l, T R, Point<T> &r)
{
  const double eps = 1e-8;
  T RR = Sqr(R);
  bool b1 = (Sqr(l.p1.x) + Sqr(l.p1.y)) <RR;
  bool b2 = (Sqr(l.p2.x) + Sqr(l.p2.y)) <RR;
  if (! (b1^b2))
    return false;
  if (fabs(l.p1.x - l.p2.x)<eps)
  {
    r.x = l.p1.x;
    r.y = std::sqrt(Sqr(R) - Sqr(r.x));
  }else
  {
    r.y = l.p1.y;
    r.x = std::sqrt(Sqr(R) - Sqr(r.y));
  }
}
template<class T>
T Length2(const Point<T> &a, const Point<T> &b)
{
  return Sqr(a.x - b.x) + Sqr(a.y - b.y);
}

template<class T>
T Length(const Point<T> &a, const Point<T> &b)
{
  return std::sqrt(Length2(a,b));
}

double S(std::vector<Point<double> >&v)
{
  int size = v.size();
  v.push_back(v[0]);
  double s = .0;
  for (int i = 0; i < size; ++i)
  {
    s += v[i].x*v[i+1].y - v[i+1].x*v[i].y;
  }
  s = std::fabs(s/2);
  return s;
}



template<class T>
T AS(Point<T> &p1, Point<T> &p2, T R)
{
  static std::vector<Point<T> > v;
  Point<T> z;
  z.x = 0;
  z.y = 0;
  v.clear();
  v.push_back(z);
  v.push_back(p1);
  v.push_back(p2);
  T ts = S(v);
  T l1, l2, l3;
  l1 = R;
  l2 = R;
  l3 = Length(p1, p2);

  T cosf = (-Sqr(l3) + Sqr(l2) + Sqr(l1))/(2.*l1*l2);
  T angle = std::acos(cosf);
  T ta = angle *  R *R/2.;
  return ta - ts;
}


double DS(double x, double y, double s, double R)
{
  if (Sqr(x+s)+Sqr(y+s) < Sqr(R))
    return s*s;
  
  if (Sqr(x)+Sqr(y)>Sqr(R))
    return .0;
  Point<double> p1, p2, p3, p4;
  p1.x = x;   p1.y = y;
  p2.x = x+s; p2.y = y;
  p3.x = x+s; p3.y = y+s;
  p4.x = x;   p4.y = y+s;
  Line<double> l1, l2, l3, l4;
  l1.p1 = p4; l1.p2 = p1;
  l2.p1 = p1; l2.p2 = p2;
  l3.p1 = p2; l3.p2 = p3;
  l4.p1 = p3; l4.p2 = p4;

  Point<double> r1, r2;
  static std::vector<Point<double> > v;
  v.clear();
  if (Intersect(l4, R, r1))
  {
    if(Intersect(l3, R, r2))
    {
      //      std::cerr << "variant 1" << std::endl;
      // 1
      v.push_back(p4);
      v.push_back(p1);
      v.push_back(p2);
      v.push_back(r2);
      v.push_back(r1);
      return S(v) + AS(r1, r2, R);
    }
    if (Intersect(l2, R, r2))
    {
      //2
      //      std::cerr << "variant 2" << std::endl;
      v.push_back(p4);
      v.push_back(p1);
      v.push_back(r2);
      v.push_back(r1);
      return S(v) + AS(r1, r2, R);
    }
  }
  if (Intersect(l1, R, r1))
  {
    if (Intersect(l3, R, r2))
    {
      //      std::cerr << "variant 3" << std::endl;
      //3
      v.push_back(p1);
      v.push_back(p2);
      v.push_back(r2);
      v.push_back(r1);
      return S(v) + AS(r1, r2, R);
    }
    if (Intersect(l2, R, r2))
    {
      //      std::cerr << "variant 4" << std::endl;
      //4
      v.push_back(p1);
      v.push_back(r2);
      v.push_back(r1);
      return S(v) + AS(r1, r2, R);
    }
  }

  return s*s;
}
double Solve()
{
  double f, R, t, r, g;
  double HoleS = 0;
  Read(f, R, t, r, g);
  double TotalArea = R*R*PI;
  if (g < (2*f))        // 100 probability
    return 1.;
  R -= f+t;               //exturde * inner radius
  
  double of = r+f;
  double inc = g+2*r;
  double ix, iy;
  for (iy = of; iy < R; iy += inc)
    for(ix = of; ix <R; ix += inc)
    {
      double d;
      HoleS += d =  DS(ix, iy, g-2*f, R);
    }
  HoleS *=4;
  return 1. - HoleS/TotalArea;
}

int main()
{
  int N;
  Read(N);
  std::cout.precision(6);
  for(int i = 1; i <=N; ++i)
  {
    std::cout << "Case #" << i << ": " <<std::fixed<< Solve() << std::endl;
  }
}
