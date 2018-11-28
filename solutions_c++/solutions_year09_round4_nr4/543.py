/*************************************************************************
Author: aMR
Created Time: 2009/9/27 0:51:43
File Name: d.cpp
Description: 
************************************************************************/
#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <sstream>
#include <queue>
using namespace std;
#define out(x) (cout<<#x<<": "<<x<<endl)
const int inf=0x7FFFFFFF;
const int maxn = 110;
struct P {
    int x, y, r;
    void input() {
        scanf("%d%d%d", &x, &y, &r);
    }
}pt[maxn];
double dist(int i, int j) {
    double x = (pt[i].x - pt[j].x) * (pt[i].x - pt[j].x);
    double y = (pt[i].y - pt[j].y) * (pt[i].y - pt[j].y);
    return sqrt(x + y);
}
int main()
{
    int z, n, ca=0;
    freopen("d.txt", "w", stdout);
    scanf("%d", &z);
    while(z--) {
        scanf("%d", &n);
        for(int i=0; i<n; ++i)
            pt[i].input();
        double ans = inf;
        for(int i=0; i<n; ++i) {
            for(int j=i+1; j<n; ++j) {
                double t = dist(i, j);
                t += pt[i].r + pt[j].r;
                ans = min(ans, t/2.0);
            }
        }
        for(int i=0; i<n; ++i) {
            ans = max(ans, (double)pt[i].r);
        }
        if(1 == n) ans = pt[0].r;
        if(2 == n) ans = max(pt[0].r, pt[1].r);
        printf("Case #%d: %.10lf\n", ++ca, ans);
    }
    return 0;
}

