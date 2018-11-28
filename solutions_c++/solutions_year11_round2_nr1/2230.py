#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <bitset>
#include <list>
#include <set>
#include <map>

using namespace std;

#define MP(A, B) make_pair(A, B)


const int N = 200;


typedef pair<int, int> PII;
#define x first
#define y second


double r1[N]; 
PII pr[N]; 
double a[N], b[N];
string ready[N];
int n;


PII pre(string S)
{
    double p = 0; int q = 0;
    for(int i=0;i<n;i++)
    {
        if (S[i]=='.') continue; ++q;
        if (S[i] == '1') p++;
    }
    return MP(p, q);
}

double work1(string S){
    double p = 0; int q = 0;
    for(int i=0;i<n;i++)
    {
        if (S[i] == '.') 
            continue; ++q;
        if (S[i] == '1') p += double(pr[i].x) / (pr[i].y - 1);
        else p += double(pr[i].x - 1) / (pr[i].y - 1);
    }
    return p / q;
}

double work2(string S)
{
    double p = 0; int q = 0;
    for(int i=0;i<n;i++)
    {
        if (S[i] == '.') 
            continue;
        ++q, p += a[i];
    }
    return p / q;
}

int main()
{
    int T; cin >> T;
    for(int t=1;t<=T;t++)
    {
        cin >> n;
        for(int i=0;i<n;i++)
        {
            cin >> ready[i];
            pr[i] = pre(ready[i]);
        }
        for(int i=0;i<n;i++)
            a[i] = work1(ready[i]);
        for(int i=0;i<n;i++)
            b[i] = work2(ready[i]);
        for(int i=0;i<n;i++)
            r1[i] = double( double(pr[i].x) / pr[i].y + 2 * a[i] + b[i]) / 4;    
        printf("Case #%d:\n", t);
        for(int i=0;i<n;i++)
            cout << r1[i] << endl;
    }
    return 0;
}

