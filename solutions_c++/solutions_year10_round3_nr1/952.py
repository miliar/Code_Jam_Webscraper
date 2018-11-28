#include <cstdio>

using namespace std;

struct point
{
    int x, y;
    char c;

    point()
    {
    }

    point(int x, int y)
    {
        this->x = x;
        this->y = y;
    }
};

struct line
{
    point p1, p2;

    line()
    {
    }

    line(point p1, point p2)
    {
        this->p1 = p1;
        this->p2 = p2;
    }
};

int ccw(point p0, point p1, point p2)
{
    int dx1, dx2, dy1, dy2;
    dx1 = p1.x - p0.x; 
    dy1 = p1.y - p0.y;
    dx2 = p2.x - p0.x;
    dy2 = p2.y - p0.y;

    if (dx1 * dy2 > dy1 * dx2) return 1;
    if (dx1 * dy2 < dy1 * dx2) return -1;
    if ((dx1 * dx2 < 0) || (dy1 * dy2 < 0)) return -1;
    if ((dx1 * dx1 + dy1 * dy1) < (dx2 * dx2 + dy2 * dy2))
        return 1;

    return 0;
}

int intersect(line l1, line l2)
{
    return ((ccw(l1.p1, l1.p2, l2.p1) * ccw(l1.p1, l1.p2, l2.p2)) <= 0)
    && ((ccw(l2.p1, l2.p2, l1.p1) * ccw(l2.p1, l2.p2, l1.p2)) <= 0);
}

line lines[1100];
int T, N, yy, ii, jj;
long long count;

int main(void)
{
    scanf("%d\n", &T);

    for (yy = 1; yy <= T; yy++)
    {
        scanf("%d\n", &N);
        for (ii = 0; ii < N; ii++)
        {
            scanf("%d ", &lines[ii].p1.y);
            lines[ii].p1.x = 0;
            scanf("%d\n", &lines[ii].p2.y);
            lines[ii].p2.x = 10;
        }

        count = 0;
        for (ii = 0; ii < N; ii++)
            for (jj = ii + 1; jj < N; jj++)
            {
                if (intersect(lines[ii], lines[jj]))
                    count++;
            }
        printf("Case #%d: %lld\n", yy, count);
    }

    return 0;
}
