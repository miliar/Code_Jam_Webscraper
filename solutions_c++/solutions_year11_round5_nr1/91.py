#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <sstream>
#include <queue>
#include <set>
#include <map>
#include <vector>
#include <complex>

#define mp make_pair
#define pb push_back
#define sqr(x) ((x)*(x))
#define foreach(it,c) for(typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)
#define BIT(x) (1LL<<(x))

using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int,int> PII;
typedef long long LL;
typedef complex<int> Point;

template<typename T> inline int size(const T &a) { return a.size(); }
template<typename T> inline bool operator<(const int &a,const vector<T> &b) { return a<b.size(); }

vector<Point> Upper, Lower;
int W,L,U,G;

double calc(const vector<Point> &V, double x)
{
    int cur = V[0].imag();

    double tot = 0;
    for(int i=1;i<size(V);i++)
    {
        double a,b,c,d;
        a = V[i-1].real();
        b = V[i-1].imag();
        c = V[i].real();
        d = V[i].imag();
        if(c >= x - 1e-6)
        {
            double ptr = (double)((d-b)/(c-a)) * (x-a) + b;
            return tot + (ptr + b) * (x - a) / 2;
        }
        tot += (double)(d + b) * (c - a) / 2;
    }
    return tot;
}

double calcarea(double xx)
{
    return calc(Upper, xx) - calc(Lower, xx);
}

void process(void)
{
    scanf("%d %d %d %d",&W,&L,&U,&G);
    Upper.resize(U);
    Lower.resize(L);

    for(int i=0;i<L;i++)
    {
        int a,b;
        scanf("%d %d",&a,&b);
        Lower[i] = Point(a,b);
    }

    for(int i=0;i<U;i++)
    {
        int a,b;
        scanf("%d %d",&a,&b);
        Upper[i] = Point(a,b);
    }

    double tot = calcarea(W);
    double accum = 0;
    printf("\n");
    for(int i=0;i<G-1;i++)
    {
        accum += tot / G;
        double s = 0, e = W;
        for(int j=0;j<500;j++)
        {
            double m = (s+e)/2;
            if(calcarea(m) > accum)
                e = m;
            else
                s = m;
        }
        printf("%.9lf\n", s);
    }

}

int main(void)
{
    int T;
    cin >> T;
    for(int i=0;i<T;i++)
    {
        cout << "Case #" << i+1 << ": ";
        process();
        cerr << i << endl;
    }
	return 0;
}

