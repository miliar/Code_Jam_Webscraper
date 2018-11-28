#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <cstdlib>
#include <vector>
#include <list>
#include <queue>
#include <algorithm>

using namespace std;


struct Point
{
    int at;
    int num;

    bool operator < (const Point a) const
    {
        return this->at < a.at;
    }
};

Point points[205];
int c, d;


bool canPut(double mid)
{
    double left = points[0].at - mid;
    for(int i = 0; i < c; ++i)
    {
        left = max(left, points[i].at - mid);
        double right = left + (points[i].num - 1) * d;
        if(right > points[i].at + mid)
            return false;
        left = right + d;
    }
    return true;
}


int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    cin >> t;
    for(int ti = 0; ti < t; ++ti)
    {
        cin >> c >> d;
        for(int i = 0; i < c; ++i)
            cin >> points[i].at >> points[i].num;
        sort(points, points + c);

        __int64 dd = d;
        dd *= 1000000;
        double st = 0, ed = dd;
        while(ed - st > 1e-8)
        {
            double mid = (st + ed) / 2;
            if(canPut(mid))
                ed = mid;
            else
                st = mid;
        }
        printf("Case #%d: %.8lf\n", ti + 1, st);
    }

    return 0;
}
