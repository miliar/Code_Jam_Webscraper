#include <vector>
#include <iostream>
#include <map>
#include <functional>
#include <algorithm>
#include <list>
#include <string>
#include <sstream>
#include <bitset>
#include <cmath>
#include <iomanip>
#include <queue>
#include <set>
#include <stack>
#include <cassert>
using namespace std;

#define rep(i, size) \
    for (int i = 0; i < size; ++ i)


struct Square
{
    Square(double l, double t, double r, double b){
        left = l;
        top = t;
        right = r;
        bottom = b;
    }

    int count(double R){
        int ret = 0;
        if (R * R < right * right + top * top)
            ret ++;
        if (R * R < left * left + top * top)
            ret ++;
        if (R * R < right * right + bottom * bottom)
            ret ++;
        if (R * R < left * left + bottom * bottom)
            ret ++;

        return ret;
    }

    double left;
    double top;
    double right;
    double bottom;
};


double getXY(double R, double y){
    return sqrt(R * R - y * y);
}


//#define formula1(x)\
//    (-(double)1.0 / 3 * pow((double)radius * radius - (x) * (x), (double)1.5f) - (double)0.5 * s.bottom * x * x)

#define PI 3.1415926f

#define EF 1e-7

struct Point
{
    Point(double x, double y){
        this->x = x;
        this->y = y;
    }
    double x;
    double y;
};

void solve(){
    cout.setf(ios::fixed);
    cout.precision(6);
    int N;
    cin >> N;
    for (int n = 0; n < N; ++ n) {
        double f, R, t, r, g;

        cin >> f >> R >> t >> r >> g;

        double x, y;
        vector<Square> squares;

        for (x = r;x < R - t - f + EF; x += (g + 2 * r)){
            for (y = r; y < R - t -f + EF;y += (g + 2 * r)){
                squares.push_back(Square(x + f, y + g - f, x + g - f, y + f));
            }
        }
        
        double area = 0.0f;
        if (g < 2 * f || abs(g - 2 * f) < EF){
            double a = 1.0f;
            cout << "Case #" << (n+1) << ": " << a << '\n';
            continue;
        }
        double radius = R - t - f;
        rep(i, squares.size()){
            Square s = squares[i];
            int c = s.count(radius);
          
            switch(c){
            case 0:
                area += (g - 2 * f) * (g - 2 * f);
                break;
            case 1:
                {
                    if (s.bottom / s.left > 1 || abs(s.bottom - s.left) < EF){
                        Point i1(getXY(radius, s.top), s.top);
                        Point i2(s.right, getXY(radius, s.right));
                        Point i3(s.left, s.left * i1.y / i1.x);
                        Point i4(s.bottom  * i2.x / i2.y, s.bottom);
                        double size = abs(atan(i1.y / i1.x) - atan(i2.y / i2.x)) /2 * radius * radius;
                        if (i3.y > s.bottom) {
                            size -= (i3.y - s.bottom) * s.left / 2;
                            size -= (i4.x - s.left) * s.bottom / 2;
                            size += (i1.x - s.left) * (s.top - i3.y) / 2;
                            size += (i2.y - s.bottom) * (s.right - i4.x) / 2;
                        } else{
                            Point i3(s.bottom  * i1.x / i1.y, s.bottom);
                            size -= (i4.x - i3.x) * s.bottom / 2;
                            size += (i2.y - s.bottom) * (s.right - i4.x) / 2;
                            size += (i3.x - s.left + i1.x - s.left) * (s.top - s.bottom) / 2;
                        }
                        /*size -= (i3.y - s.bottom) * s.left / 2;
                        size -= (i4.x - s.left) * s.bottom / 2;*/
                        if (abs(s.bottom - s.left) > EF) {
                            area += 2 * size;
 
                        }
                        else
                            area += size;
                        break;
                    }
                }
            case 2:
                {
                    if (s.bottom / s.left > 1){
                        Point i1(s.left, getXY(radius, s.left));
                        Point i2(s.right, getXY(radius, s.right));
                        double size = abs(atan(i1.y / i1.x) - atan(i2.y / i2.x)) /2 * radius * radius;
                        
                        Point i3(s.bottom * i2.x / i2.y, s.bottom);
                        size -= (i1.y - s.bottom) * s.left / 2;
                        size -= (i3.x - s.left) * s.bottom / 2;
                        size += (i2.y - s.bottom) * (s.right - i3.x) / 2;
                        area += size * 2;
                    }
                    break;
                }
            case 3:
                {
                    double size;
                    Point i1(s.left, getXY(radius, s.left));
                    Point i2(getXY(radius, s.bottom), s.bottom);
                    size = abs(atan(i1.y / i1.x) - atan(i2.y / i2.x)) /2 * radius * radius;
                    size -= (i1.y - s.bottom) * s.left / 2;
                    size -= (i2.x - s.left) * s.bottom / 2;
                    area += size;
                }
                break;
            case 4:
                // ignore
                break;
            }
        }

        double total = R * R * PI;
        cout << "Case #" << (n+1) << ": "<<(1 - area * 4/ total) << '\n';



    }

}