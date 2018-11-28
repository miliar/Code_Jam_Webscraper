#include <iostream>
#include <fstream>
#include <sstream>
#include <cmath>
#include <string.h>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#define For(i, a, b) for(int i = a; i <= b; i++)
#define ForL(i, a, b) for(int i = a; i >= b; i--)
#define pb push_back
#define fi first
#define se second
#define MAXN 1000100
#define INF 1000000000000.0
#define EPS 1e-7

using namespace std;

struct Point{
    double p, v;
    Point(){}
    Point(double _p, double _v){
        p = _p;
        v = _v;   
    }  
};

int n, C, D;
Point P[210];
double A[MAXN];

bool cmp(Point a, Point b)
{
    return (a.p < b.p);
}   

bool check(double mid)
{
    double start = A[1] - mid;
    For(i, 2, n){
        start += D;
        if (A[i] < start && start-A[i] > mid+EPS){
            return false;   
        }
        if (A[i] > start && A[i]-start > mid+EPS){
            start = A[i] - mid;   
        }
    }
    
    return true;
}

double cp()
{
    double l = 0.0;
    double r = INF;
    double mid;
    double res = 0;
    while (l+EPS < r || abs(r-l) < EPS){
        mid = (l+r) / 2;
        if (check(mid)){
            res = mid;
            r = mid - EPS;   
        }else{
            l = mid + EPS;   
        }
    }
    if (abs(res-0) < EPS){
        res = 0.0;
    }   
    return res;
}

int main()
{
    int nTest;
    ifstream fin("B.inp");
    fin >> nTest;
    For(k, 1, nTest){
        fin >> C >> D;
        n = 0;
        For(i, 1, C){
            fin >> P[i].p >> P[i].v;
        }   
        sort(P+1, P+C+1, cmp);
        For(i, 1, C){
            For(j, 1, P[i].v){
                n++;
                A[n] = P[i].p;   
            }
        }
        cout.setf(ios::fixed);
        cout.precision(7);
        cout << "Case #" << k << ": " << cp() << endl;
    }
    fin.close();
   // system("pause");
    return 0;
}

