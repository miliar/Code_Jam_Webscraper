#include <iostream>
#include <string>
#include <fstream>
#include <cmath>
#include <iomanip>

using namespace std;

ofstream outs ("output.txt");
#define cout outs

ifstream ins ("input.txt");
#define cin ins
#define FOR(i,n) for(int i = 0; i<n; i++);

double fs [500][6];


typedef struct {double x, y, z;} Point;    // exclude z for 2D
typedef struct {double x, y, z;} Vector;
typedef struct {Point P0, P1;} Line;
typedef struct {Point P0; double a;} Ret;

Point operator+(const Point &a, const Vector &b)
{
    Point c;
    c.x = a.x + b.x;
    c.y = a.y + b.y;
    c.z = a.z + b.z;
    return c;
}

Vector operator-(const Point &a, const Point &b)
{
    Vector c;
    c.x = a.x - b.x;
    c.y = a.y - b.y;
    c.z = a.z - b.z;
    return c;
}

Vector operator*(const double &a, const Vector &b)
{
    Vector c = b;
    c.x *= a;
    c.y *= a;
    c.z *= a;
    return c;
}

// Copyright 2001, softSurfer (www.softsurfer.com)
// This code may be freely used and modified for any purpose
// providing that this copyright notice is included with it.
// SoftSurfer makes no warranty for this code, and cannot be held
// liable for any real or imagined damage resulting from its use.
// Users of this code must verify correctness for their application.

// Assume that classes are already given for the objects:
//    Point and Vector with
//        coordinates {double x, y, z;} (z=0 for 2D)
//        appropriate operators for:
//            Point  = Point ± Vector
//            Vector = Point - Point
//            Vector = Scalar * Vector
//    Line with defining endpoints {Point P0, P1;}
//    Segment with defining endpoints {Point P0, P1;}
//===================================================================

// dot product (3D) which allows vector operations in arguments
#define dot(u,v)   ((u).x * (v).x + (u).y * (v).y + (u).z * (v).z)
#define norm(v)    sqrt(dot(v,v))  // norm = length of vector
#define d(u,v)     norm(u-v)       // distance = norm of difference

// dist_Point_to_Line(): get the distance of a point to a line.
//    Input:  a Point P and a Line L (in any dimension)
//    Return: the shortest distance from P to L
Ret
dist_Point_to_Line( Point P, Line L)
{
    Ret a;
    Vector v = L.P1 - L.P0;
    Vector w = P - L.P0;

    double c1 = dot(w,v);
    double c2 = dot(v,v);
    double b = c1 / c2;

    Point Pb = L.P0 + b * v;
    a.P0 = Pb;
    a.a = d(P, Pb);
    return a;
}


int main()
{
    int n;
    int f;
    int s = 6;
    double t [6];
    double fs [6];
    Point p;
    Line l;

    p.x = 0;p.y = 0; p.z=0;

    cin >> n;

    for (int N= 0; N < n; N++)
    {
        cin >> f;
        for (int i=0; i< s; i++)
            fs[i] = 0;
        for (int i= 0; i < f; i++)
            for (int j=0; j< s; j++)
            {
                cin >> t[j];
                if (j < 3)
                    fs[j] += t[j];
                else
                    fs[j] += t[j];
            }
         for (int i=0; i< 6; i++)
            fs[i] /= f;

        l.P0.x = fs[0];
        l.P0.y = fs[1];
        l.P0.z = fs[2];
        l.P1.x = fs[3]+fs[0];
        l.P1.y = fs[4]+fs[1];
        l.P1.z = fs[5]+fs[2];

        Ret a;

        //cout << fs[0] << " " << fs[1] << " " << fs[2] << " " << fs[3] << " " << fs[4] << " " << fs[5] <<endl;

        if (fs[3] != 0 || fs[4] != 0  || fs[5] != 0)
            a = dist_Point_to_Line(p,l);
        else
            a.a = norm(l.P0);

        double ans;

        if (fs[3] != 0)
            ans = (a.P0.x - fs[0])/fs[3];
        else if (fs[4] != 0)
            ans = (a.P0.y - fs[1])/fs[4];
        else if (fs[5] != 0)
            ans = (a.P0.z - fs[2])/fs[5];
        else
            ans = 0;

        if (ans < 0)
        {
            ans = 0;
            a.a = norm(l.P0);
        }

        cout << fixed << setprecision(8) << "Case #" << N+1 << ": " <<  a.a << " " << ans << endl;
    }

    return 0;
}
