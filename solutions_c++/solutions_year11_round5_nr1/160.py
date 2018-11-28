#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <cmath>
#include <algorithm>

using namespace std;

const int maxn = 202;
const double eps = 1e-9;

struct Node
{
    double x, y;
};

struct Line
{
    double x, y1, y2;
    Line() {}
    Line(double _x, double _y1, double _y2 )
        : x(_x), y1(_y1), y2(_y2) {}
};

Node low[maxn], up[maxn];
double setX[maxn];
Line line[maxn];

int cas, run, W, L, U, G, tot;
double Area[maxn];
double totArea, aveArea;

bool equal(double a, double b )
{
    return fabs(a-b)<eps;
}

void init()
{
    scanf("%d%d%d%d",&W,&L,&U,&G);
    for (int i = 0; i<L; i++ )
    {
        scanf("%lf%lf",&low[i].x,&low[i].y);
        setX[i] = low[i].x;
    }
    for (int i = 0; i<U; i++ )
    {
        scanf("%lf%lf",&up[i].x,&up[i].y);
        setX[L+i] = up[i].x;
    }
}

double calcY(double x1, double y1, double x2, double y2, double x)
{
    return y1 + (x-x1)*(y2-y1)/(x2-x1);
}

double findY(Node data[maxn], int L, double x )
{
    for (int i = 0; i<L; i++ )
    {
        if (equal(data[i].x, x)) return data[i].y;
        double x1 = data[i].x, y1 = data[i].y;
        double x2 = data[i+1].x, y2 = data[i+1].y;
        if (x2 > x) return calcY(x1, y1, x2, y2, x);
    }
}

double calcArea(Line a, Line b )
{
    return (a.y2 - a.y1 + b.y2 - b.y1)*(b.x - a.x)/2.0;
}

void prepare()
{
    sort(setX, setX+L+U);
    tot = 0;
    for (int i = 0; i<L+U; i++ )
        if (i == 0 || !equal(setX[i], setX[i-1]))
            setX[tot++] = setX[i];
            
    totArea = 0;
    Area[0] = 0;
    for (int i = 0; i<tot; i++ )
    {
        line[i].x = setX[i];
        line[i].y1 = findY(low, L, setX[i]);
        line[i].y2 = findY(up, U, setX[i]);
        if (i) Area[i] = calcArea(line[i-1], line[i]);
        //cout<<line[i].x<<' '<<line[i].y1<<' '<<line[i].y2<<' '<<Area[i]<<endl;
        totArea += Area[i];
    }
    aveArea = totArea / (double)G;
}

void work()
{
    printf("Case #%d:\n", run);
    int p = 1;
    double preX = 0;
    for (int k = 0; k<G-1; k++ )
    {
        double curArea = 0;
        while (1)
        {
            if (curArea + Area[p] < aveArea + eps)
            {
                curArea += Area[p];
                preX = line[p].x;
                p++;
                continue;
            }
            Line leftLine(preX, calcY(line[p-1].x, line[p-1].y1, line[p].x, line[p].y1, preX),
                                calcY(line[p-1].x, line[p-1].y2, line[p].x, line[p].y2, preX));
            double x1 = line[p-1].x, y1 = line[p-1].y1, y2 = line[p-1].y2;
            double k1 = (line[p].y1 - y1) / (line[p].x - x1);
            double k2 = (line[p].y2 - y2) / (line[p].x - x1);
            double xL = line[p-1].x, xR = line[p].x, midX;
            while (xL + eps < xR)
            {
                midX = (xL + xR)/2.0;
                double S = calcArea(leftLine, Line(midX, y1 + (midX-x1)*k1, y2 + (midX-x1)*k2));
                if (curArea + S <= aveArea) xL = midX; else xR = midX;
            }
            printf("%.8lf\n",midX);
            preX = midX;
            Area[p] = calcArea(Line(midX, y1 + (midX-x1)*k1, y2 + (midX-x1)*k2), line[p]);
            break;
        }
    }
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    scanf("%d",&cas);
    for (run = 1; run<=cas; run++ )
    {
        init();
        prepare();
        work();
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
