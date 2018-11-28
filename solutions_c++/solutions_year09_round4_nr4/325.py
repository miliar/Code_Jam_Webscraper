#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <bitset>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cfloat>

#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()

#define eps 1e-8
#define pi acos(-1)

using namespace std;

vector <int> X, Y, R;

double f(int a, int b, int c)
{
    return max( (sqrt((X[a]-X[b])*(X[a]-X[b]) + (Y[a]-Y[b])*(Y[a]-Y[b])) + R[a] + R[b])/2.0, 1.0*R[c]);
}

int main()
{
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
        
    int nCasos;
    cin>>nCasos;
    
    for(int caso=1; caso<=nCasos; caso++)
    {
        int N;
        cin>>N;
        
        X = vector <int> (N);
        Y = vector <int> (N);
        R = vector <int> (N);
        
        for(int i=0; i<N; i++)
            cin>>X[i]>>Y[i]>>R[i];
        
        double minR;
        if(N==1) minR = R[0];
        else if(N==2) minR = max(R[0], R[1]);
        else
        {
            minR = min(f(0, 1, 2), min(f(0, 2, 1), f(1, 2, 0)));
        }
        printf("Case #%d: %.7lf\n", caso, minR);
    }

    return 0;
}
