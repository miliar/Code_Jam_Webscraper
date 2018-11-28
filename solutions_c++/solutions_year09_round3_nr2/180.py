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

#define SZ(a) ((int)(a).size())
#define MOD 1000000000
#define MODL 9

using namespace std;

typedef unsigned long long LL;
typedef vector <int> VI;
typedef vector <double> VD;
typedef vector <vector<unsigned long long> > VVI;
typedef pair <int,int> PII;
typedef vector <LL> VL;
typedef vector <string> VS;

VI split(string s, string t=" ") {
    VI ret;
    int a,b=0;
    while ((a=s.find_first_not_of(t,b))!=-1) {
        b=s.find_first_of(t,a);
        ret.push_back(atol(s.substr(a,b-a).c_str()));
    }
    return ret;
}

#define INF 0x7fffffff
#define SQR(x) (x)*(x)
unsigned long long pow1(unsigned long long a, int b) {
    unsigned long long ret = 1;
    for (int i=0; i<b; i++) {
        ret *= a;
    }
    return ret;
}

main()
{
    int t;
    scanf("%d\n", &t);
    for (int tt =0; tt < t; tt++) {
        double ret = 0;
        int n = 0;
        scanf("%d\n", &n);
        vector<double> x(3,0);
        vector<double> vx(3,0);
        for (int i=0; i<n; i++) {
            VI vec(6);
            scanf("%d %d %d %d %d %d\n", &vec[0], &vec[1], &vec[2], &vec[3], &vec[4], &vec[5]);
            for (int i=0; i<3; i++) {
                x[i] += vec[i];
            }
            for (int i=0; i<3; i++) {
                vx[i] += vec[i+3];
            }
        }
        for (int i=0; i<3; i++) x[i] /= n;
        for (int i=0; i<3; i++) vx[i] /= n;
        double denom = (vx[0]*vx[0] + vx[1]*vx[1] + vx[2]*vx[2]);
        if (denom < 1e-10) ret = 0;
        else ret = -(vx[0]*x[0] + vx[1]*x[1] + vx[2]*x[2])/denom;
        if (ret < 1e-10) {
            ret = 0;
        }
        double sum = 0;
        for (int i=0; i<3; i++) {
            sum += SQR(x[i]+vx[i]*ret);
        }
        double dmin = sqrt(sum);
        printf("Case #%d: %.8lf %.8lf\n", tt+1, dmin, ret);
    }
}
