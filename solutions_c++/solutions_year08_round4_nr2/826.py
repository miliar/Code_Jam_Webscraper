#include <string>
#include <vector>
#include <map>
#include <set>
#include <iostream>
#include <sstream>
#include <list>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>

using namespace std;

typedef long long LL;
typedef vector <int> VI;
typedef vector <double> VD;
typedef vector <vector<int > > VVI;
typedef pair <int,int> PII;
typedef vector <LL> VL;
typedef vector <string> VS;

VS split(string s, string t=" ") {
    VS ret;
    int a,b=0;
    while ((a=s.find_first_not_of(t,b))!=-1) {
        b=s.find_first_of(t,a);
        ret.push_back(s.substr(a,b-a));
    }
    return ret;
}
    //Compute the dot product AB ⋅ BC
    int dot(int *A, int* B, int* C){
        int AB[2];
        int BC[2];
        AB[0] = B[0]-A[0];
        AB[1] = B[1]-A[1];
        BC[0] = C[0]-B[0];
        BC[1] = C[1]-B[1];
        int dot = AB[0] * BC[0] + AB[1] * BC[1];
        return dot;
    }
    //Compute the cross product AB x AC
    int cross(int* A, int* B, int* C){
        int AB[2];
        int AC[2];
        AB[0] = B[0]-A[0];
        AB[1] = B[1]-A[1];
        AC[0] = C[0]-A[0];
        AC[1] = C[1]-A[1];
        int cross = AB[0] * AC[1] - AB[1] * AC[0];
        return cross;
    }
    //Compute the distance from A to B
    double distance(int* A, int* B){
        int d1 = A[0] - B[0];
        int d2 = A[1] - B[1];
        return sqrt(d1*d1+d2*d2);
    }

    //Compute the distance from AB to C
    //if isSegment is true, AB is a segment, not a line.
    double linePointDist(int* A, int* B, int* C, bool isSegment=false){
        double dist = cross(A,B,C) / distance(A,B);
        if(isSegment){
            int dot1 = dot(A,B,C);
            if(dot1 > 0)return distance(B,C);
            int dot2 = dot(B,A,C);
            if(dot2 > 0)return distance(A,C);
        }
        return abs(dist);
    }

int main()
{
    int _nn;
    scanf("%d\n", &_nn);
    for (int tr=0; tr<_nn; tr++) {
        int n,m,area;
        cin >> n >> m >> area;
        int a[2], b[2], c[2];
        bool ok = false;

        c[0]=c[1]=0;
        for (a[0]=0;a[0]<=n;a[0]++) for (a[1]=0;a[1]<=m;a[1]++)  {
            for (b[0]=a[0]+1;b[0]<=n;b[0]++) for (b[1]=0;b[1]<=m;b[1]++)  {
                if (abs(area - distance(a,c)*linePointDist(c,a,b,false)) < 1e-6) {
                    ok = true;
                    printf("Case #%d: %d %d %d %d %d %d\n", tr+1, c[0], c[1], b[0], b[1], a[0], a[1]);
                    goto label;
                }

            }
        }


label:
        if (!ok) 
            printf("Case #%d: IMPOSSIBLE\n", tr+1);
    }
    return 0;
}

