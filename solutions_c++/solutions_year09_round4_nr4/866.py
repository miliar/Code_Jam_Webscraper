#include <cstdio>
#include <iostream>
#include <sstream>

#include <cstring>
#include <cstdlib>

#include <list>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <string>

#include <complex>
#include <cmath>

#include <algorithm>
#include <numeric>
#include <utility>

using namespace std;

typedef pair<int, int> pxy;
typedef pair<pxy, int> pxyz;

char buffer[1000];

#ifdef DEBUG
#define PRINT(s, x...) \
fprintf(stderr, "Line %d: ", __LINE__); \
fprintf(stderr, s, x);
#define VAR(x) cerr << "Line " << __LINE__ << ": " << #x << " = " << (x) << "\n";
#define PRINTARR(x, a, b) for(int __ = (a); __ < (b); ++__) cerr << "Line " << __LINE__ << ": " <<  #x << "[" << __ << "] = " << (x)[__] << endl;
#else
#define PRINT(s, x...)
#define VAR(x)
#define PRINTARR(x, n)
#endif

double dist(int* A, int* B)
{
    double dx = A[0] - B[0];
    double dy = A[1] - B[1];
    
    return sqrt(dx*dx + dy*dy);
}

double solve3(int* A, int* B, int* C)
{
    double dists[3][3];
    dists[0][0] = dist(A, A);
    dists[0][1] = dist(A, B);
    dists[0][2] = dist(A, C);
    
    dists[1][0] = dist(B, A);
    dists[1][1] = dist(B, B);
    dists[1][2] = dist(B, C);
    
    dists[2][0] = dist(C, A);
    dists[2][1] = dist(C, B);
    dists[2][2] = dist(C, C);
    
    /// pair a,b
    double ans_A = max(double(C[2]), 0.5*(dists[0][1] + A[2] + B[2]));
    
    /// pair b,c
    double ans_B = max(double(A[2]), 0.5*(dists[1][2] + B[2] + C[2]));
    
    /// pair a,c
    double ans_C = max(double(B[2]), 0.5*(dists[0][2] + A[2] + C[2]));
    
    return min(min(ans_A, ans_B), ans_C);
}

int main(int argc, char** argv)
{
    int T;
    
    scanf("%d", &T);
    
    for(int t = 1; t <= T; ++t)
    {
        int n;
        
        scanf("%d", &n);
        
        if(n == 1)
        {
            int A[3];
            scanf("%d %d %d", A, A+1, A+2);
            printf("Case #%d: %d\n", t, A[2]);
        }
        else if(n == 2)
        {
            int A[3], B[3];
            scanf("%d %d %d", A, A+1, A+2);
            scanf("%d %d %d", B, B+1, B+2);
            printf("Case #%d: %d\n", t, max(A[2], B[2]));
        }
        else if(n == 3)
        {
            int A[3], B[3], C[3];
            scanf("%d %d %d", A, A+1, A+2);
            scanf("%d %d %d", B, B+1, B+2);
            scanf("%d %d %d", C, C+1, C+2);
            printf("Case #%d: %lf\n", t, solve3(A, B, C));
        }
    }
    
    return 0;
}