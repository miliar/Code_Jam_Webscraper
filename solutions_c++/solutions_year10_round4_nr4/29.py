#include<iostream>
#include<vector>
#include<cstring>
#include<stdio.h>
#include<string>
#include<cassert>
#include<algorithm>
#include<cmath>
using namespace std;

#define forn(i,n) for (int i=0;i<(n);i++)
#define init(a,v) memset(a,v,sizeof(a))
#define gi(t) scanf("%d",&(t))
#define sz 50

int n; int m;
pair <int, int> p[sz];
pair <int, int> q[sz];
double ans[sz];

double dotProduct(pair <int, int> a, pair <int, int> b, pair <int, int> c)
{ return ((double)(b.first-a.first)*(c.first-a.first) + (b.second-a.second)*(c.second-a.second)); }

double len(pair <int, int> a, pair <int, int> b)
{ return sqrt((double)(b.first-a.first)*(b.first-a.first) + (b.second-a.second)*(b.second-a.second)); }

double area(double rad, double angle)
{
    double PI = 4.0*atan(1.0);
    double ret = rad*rad*angle/2.0;
    ret -= 0.5*rad*rad*sin(angle);
    return ret; 
}

void compute(int index)
{
    double dot;
    dot = dotProduct(p[0], p[1], q[index]);
    double angle = acos(dot/((len(p[1], p[0])*len(q[index], p[0]))));
    ans[index] = area(len(q[index], p[0]), 2.0*angle);
    
    dot = dotProduct(p[1], p[0], q[index]);
    angle = acos(dot/((len(p[1], p[0])*len(q[index], p[1]))));
    ans[index] += area(len(q[index], p[1]), 2.0*angle);
}

int main ()
{
    int nTest; gi(nTest);
    forn(test, nTest)
    {
        gi(n); gi(m);
        forn(i,n) { gi(p[i].first); gi(p[i].second); }
        forn(i,m) { gi(q[i].first); gi(q[i].second); }
        forn(i,m) compute(i);
        printf("Case #%d: ", test+1);
        forn(i,m) printf("%.8lf ", ans[i]);
        printf("\n"); 
    }
    return 0;
}