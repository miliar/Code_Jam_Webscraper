#include <cstdio>
#include <cmath>
#include <utility>
using namespace std;

const double EPS = 1e-6;
typedef pair<double, double> Point;
const Point origin(0.0, 0.0);
const double PI = acos(-1);

inline
double dis(const Point& a, const Point& b)
{
    double dx = a.first - b.first;
    double dy = a.second - b.second;
    
    return sqrt(dx * dx + dy * dy); 
}

typedef double Point::*M;

template<M member>
Point inter(double range, const Point& p)
{
    double q = sqrt(range * range - p.*member * p.*member);
    Point ret(q, q);
    
    ret.*member = p.*member;

    return ret;
}

inline
double areaTriangle(const Point& a, const Point& b, const Point& c)
{
    double dx1 = b.first - a.first;
    double dy1 = b.second - a.second;
    double dx2 = c.first - a.first;
    double dy2 = c.second - a.second;
    return fabs(dx1 * dy2 - dy1 * dx2) / 2.0;
}


inline
double areaCircle(double r, const Point& a, const Point& b)
{
    double la = dis(origin, a);
    double lb = dis(origin, b);
    double lc = dis(a, b);
    //printf("%lf %lf %lf\n", la, lb, lc);
    double angle = acos((la * la + lb * lb - lc * lc) / (2 * la * lb));
//    printf("##%lf %lf %lf\n", angle, angle * r * r / 2, areaTriangle(a, b, origin));
    return angle * r * r / 2 - areaTriangle(a, b, origin);
}

void print(Point p)
{
    //printf("(%lf, %lf)", p.first, p.second);     
}

int main()
{
   
    
   int N;
   scanf("%d", &N);
   
   for(int times = 0; times < N; times++)
   {
       double f, R, t, r, g;
       scanf("%lf%lf%lf%lf%lf", &f, &R, &t, &r, &g);
       
       double range = R - t - f;
       double ans = 0.0;
       
       if(fabs(f * 2 - g) < EPS || range < EPS)
           ans = 1.0;
       else
       {
    //       printf("!");
           
           g -= 2 * f;
           r += f;
  //         printf("%lf %lf %lf %lf %lf %lf\n", f, R, t, r, g, range);
           
           for(int i = 0, finish = 1; finish; i++)
           {
               finish = 0;
               for(int j = 0; ; j++)
               {
                   
                   Point lb = make_pair(i * (g + 2 * r) + r, j * (g + 2 * r) + r);
                   if(dis(lb, origin) >= range)
                       break;
                   else
                   {
//                       printf("(%d, %d)", i, j);
                       finish = 1;
                       Point lt = make_pair(lb.first, lb.second + g);
                       Point rb = make_pair(lb.first + g, lb.second);
                       Point rt = make_pair(lb.first + g, lb.second + g);
                   
                       if(dis(rt, origin) <= range)
                           ans += g * g;
                       else
                       {
                           bool ilt = dis(lt, origin) < range;
                           bool irb = dis(rb, origin) < range;
                           
                           if(ilt && irb)
                           {
            //                   printf("1");
                               Point pt = inter<&Point::second>(range, lt);
                               Point pb = inter<&Point::first>(range, rb);
                               
                               ans += g * g - areaTriangle(pt, pb, rt) + areaCircle(range, pt, pb);
                           }
                           else if(!(ilt || irb))
                           {
          //                     printf("2");
                               //print(lt);print(rb);printf("%lf %lf %d %d\n", dis(lt, origin), dis(rb, origin), ilt + 1, irb + 1);
                               Point pt = inter<&Point::first>(range, lt);
                               Point pb = inter<&Point::second>(range, rb);                                
                               print(pt);print(pb);
        //                       printf("%lf %lf\n", areaTriangle(pt, pb, lb), areaCircle(range, pt, pb));
                               ans += areaTriangle(pt, pb, lb) + areaCircle(range, pt, pb);
                           }
                           else if(ilt)
                           {
              //                 printf("3");
                               Point pt = inter<&Point::second>(range, lt);
                               Point pb = inter<&Point::second>(range, rb);                                                                
                               
                               ans += areaCircle(range, pt, pb) + (dis(lt, pt) + dis(lb, pb)) * g / 2;
                           }
                           else
                           {
                //               printf("4");
                               Point pt = inter<&Point::first>(range, lt);
                               Point pb = inter<&Point::first>(range, rb);                                                                
                               
                               ans += areaCircle(range, pt, pb) + (dis(lb, pt) + dis(rb, pb)) * g / 2;
                           }
                       }
                   }
               }        
               
               
               
           }
           
           
           ans = 1.0 - ans * 4 / (R * R * PI);
       }   
       
       printf("Case #%d: %.6lf\n", times + 1, ans);
   }
    
   return 0;   
}
