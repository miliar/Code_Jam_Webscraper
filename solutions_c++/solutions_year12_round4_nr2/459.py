#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <climits>
#include <ctime>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
#include <deque>
#include <list>
#include <queue>
#include <set>
#include <map>
#include <limits>
#include <cstring>

using namespace std;

struct Point {
    Point(int index, int x, int y) : index(index), x(x), y(y) {}
    int index;
    int x, y;
};

struct Circle {
    int index;
    int radius;
    bool operator<(const Circle& c) const {
        return c.radius < radius;
    }
};

Circle circles[1005];
int rankOfCircle[1005];
int n;

void circlesInRect(int& i, int width, int height, vector<Point>& points, int xMin, int xMax) {
    int x = 0;
    vector<Point> pRev;
    points.clear();
    while (i < n) {
        int r = circles[i].radius;
        int xCenter = max(xMin, x + r);
        if (xCenter + r > width || xCenter > xMax) break;
        int nextX = xCenter + r;

        points.push_back(Point(i, xCenter, r));
        i++;

        if (r * 4 <= height) {
            int x1 = max(x, xMin);
            int x2 = min(x + r * 2, xMax);
            int ii = i;
            circlesInRect(ii, height - r, x2 - x1, pRev, INT_MIN, INT_MAX);
            for (int j = 0; j < (int) pRev.size(); j++) {
                points.push_back(Point(pRev[j].index, x + pRev[j].y, pRev[j].x + r * 2));
            }
            i = ii;
        }

        x = nextX;
    }
}

int main() {
    int nCases;
    int width, height, w0, h0;
    bool reversed = false;
    
    scanf("%d", &nCases);
    for (int iCase = 1; iCase <= nCases; iCase++) {
        scanf("%d%d%d", &n, &width, &height);
        w0 = width;
        h0 = height;
        
        reversed = false;
        if (width > height) {
            swap(width, height);
            reversed = true;
        }

        for (int i = 0; i < n; i++) {
            circles[i].index = i;
            scanf("%d", &circles[i].radius);
        }
        sort(circles, circles + n);

        for (int i = 0; i < n; i++) {
            rankOfCircle[circles[i].index] = i;
        }

        int delta = circles[0].radius;
        int i = 0, y = 0;
        vector<Point> points, pY;

        while (i < n) {
            int ii = i;
            circlesInRect(ii, width + delta * 2, circles[i].radius * 2, pY, delta, width + delta);
            for (int j = 0; j < (int) pY.size(); j++) {
                points.push_back(Point(pY[j].index, pY[j].x - delta, pY[j].y + y));
            }
            y += circles[i].radius * 2;
            assert(ii > i);
            i = ii;
        }
        
        assert((int) points.size() == n);

        printf("Case #%i:", iCase);
        for (int idx = 0; idx < n; idx++) {
            for (int i = 0; i < n; i++) {
                if (circles[i].index == idx) {
                    assert(points[i].index == i);
                    for (int k = 0; k < n; k++) {
                        if (k == i) break;
                        int dx = points[i].x - points[k].x;
                        int dy = points[i].y - points[k].y;
                        double dist = sqrt((double) dx * (double) dx + (double) dy * (double) dy);
                        double minDist = circles[i].radius + circles[k].radius;
                        /*cout << "i=" << i << " k=" << k << endl;
                        cout << endl
                            << "index_" << i << " (x=" << points[i].x << ",y=" << points[i].y << ",r=" << circles[i].radius << ")\n"
                            << "index_" << k << " (x=" << points[k].x << ",y=" << points[k].y << ",r=" << circles[k].radius << ")\n"
                            << "dx=" << dx << " dy=" << dy << " dist=" << dist << " minDist=" << minDist << endl;*/
                        assert(dist >= minDist);
                    }
                    int xx, yy;
                    if (!reversed) {
                        xx = points[i].x;
                        yy = points[i].y;
                    } else {
                        xx = points[i].y;
                        yy = points[i].x;
                    }
                    assert(xx >= 0 && xx <= w0);
                    assert(yy >= 0 && yy <= h0);
                    printf(" %i %i", xx, yy);
                }
            }
        }
        printf("\n");
    }
    return 0;
}
