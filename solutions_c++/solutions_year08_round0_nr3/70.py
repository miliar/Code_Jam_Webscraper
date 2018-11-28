#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <string>
#include <algorithm>
#include <boost/math/constants/constants.hpp>
#include <iomanip>
#include <math.h>
#include <stdexcept>

using namespace std;

    ifstream in("input.in");
    ofstream out("out");

long double disk(long double radius)
{
    return radius*radius*boost::math::constants::pi<long double>();
}

long double f, R, t, r, g;

bool inside(long double x, long double y)
{
    return ((x*x+y*y)<=((R-t-f)*(R-t-f)));
}

long double sliver(long double x, long double y)
{
//    cout << "sliver: " << x << " " << y << endl;
    
    long double radius = R - t - f;
//    cout << "radius: " << radius << endl;
    long double a1 = asin(y/radius);
    long double a2 = acos(x/radius);
    long double a = a2 - a1;
//    cout << "angles:" << a1 << " " << a2 << endl;
    if(a < 0)
        throw (std::runtime_error("angle is negative!"));
    
    long double pie = radius*radius*a/2;
//    cout << "pie:" << pie << endl;
    
    long double br_triangle = ((cos(a1)*radius-x)*y)/2;
    long double tl_triangle = (x*(sin(a2)*radius-y))/2;
    
//    cout << "triangles: " << br_triangle << " " << tl_triangle << endl;
    
    long double area = pie - br_triangle - tl_triangle;
    if(area < 0)
        throw (std::runtime_error("sliver area is negative!"));
//    cout << "area: " << area << endl;
    return area;
}

long double one_corner(long double left, long double right, long double bottom)
{
    long double radius = R - t - f, area=0;

    long double lifted_bottom = sin(acos(right/radius))*radius;
    area += sliver(left, lifted_bottom);
    area += (right - left) * (lifted_bottom - bottom);
    return area;
}

void do_case(int c)
{
    
    in >> f >> R >> t >> r >> g;
    
    long double radius = R - t - f;

    long double total=disk(R);
    long double safe=0;
    
    long double complete;
    if(g > 2*f)
    {
        complete = (g - 2*f)*(g - 2*f);
    
        for(long double x=0; x<R; x+=g+2*r)
        {
            for(long double y=0; y<R; y+=g+2*r)
            {
                // corners
                long double
                    bottom = y + r,
                    top = bottom + g,
                    left = x + r,
                    right = left + g;
                
                right -= f;
                top -= f;
                bottom += f;
                left += f;
                
                // completely inside
                if(inside(right,top))
                {
                    safe += complete;
                    continue;
                }
                
                // completely outside
                if(!inside(left, bottom))
                    continue;
                    
                // only bottom left corner inside
                if(!inside(left, top) && !inside(right, bottom))
                {
                    safe += sliver(left, bottom);
                    continue;
                }
                
                // bottom corners inside
                if(!inside(left, top) && inside(right, bottom))
                {
                    safe += one_corner(left, right, bottom);
                    continue;
                }

                // left corners inside
                if(inside(left, top) && !inside(right, bottom))
                {
                    safe += one_corner(bottom, top, left);
                    continue;
                }
                
                // both corners inside
                if(inside(left, top) && inside(right, bottom))
                {
                    long double lifted_bottom = sin(acos(right/radius))*radius;
                    long double shifted_left = cos(asin(top/radius))*radius;
                    safe += sliver(shifted_left, lifted_bottom);
                    safe += (shifted_left - left) * (top - bottom);
                    safe += (lifted_bottom - bottom) * (right - left);
                    safe -= (lifted_bottom - bottom) * (shifted_left - left);
                    continue;
                }
            }
        }
    }
    
    ostream &output(out);
    output.setf(ios::fixed);
    output << setprecision(8);
    output << "Case #" << c+1 << ": " << 1 - (safe*4 / total) << endl;
}

int main (int argc, char * const argv[]) {

    
    unsigned N;
    
    in >> N;
    
    for(unsigned c=0; c<N; c++)
        do_case(c);
        
    return 0;
}
