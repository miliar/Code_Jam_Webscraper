#include<algorithm>
#include<cmath>
#include<fstream>
#include<iomanip>
#include<iostream>
#include<map>
#include<queue>
#include<set>
#include<sstream>
#include<stack>
#include<vector>

using namespace std;

#define forn(i,n) for(int i = 0; i < (n); i++)
#define dforn(i,n) for(int i = ((int)n)-1; i >= 0; i--)
#define all(v) v.begin(), v.end()
#define pb push_back


class Circulo
{
    public:
    pair<long double, long double> centro;
    long double radio;
};

pair<long double, long double> p[2];
pair<long double, long double> baldes[10];
Circulo circ[2];

double calc()
{
    long double d = sqrt((p[0].first-p[1].first)*(p[0].first-p[1].first)+(p[0].second-p[1].second)*(p[0].second-p[1].second));
    long double s = (circ[0].radio+circ[1].radio+d)/2;
    long double ta = sqrt(s*(s-circ[0].radio)*(s-circ[1].radio)*(s-d));
    long double a1 = acos((d*d+circ[0].radio*circ[0].radio-circ[1].radio*circ[1].radio)/(2*d*circ[0].radio));
    long double a2 = acos((d*d-circ[0].radio*circ[0].radio+circ[1].radio*circ[1].radio)/(2*d*circ[1].radio));
    return circ[0].radio*circ[0].radio*a1+circ[1].radio*circ[1].radio*a2-2*ta;
}

int main()
{
    freopen("D-small.in","r",stdin);
    freopen("D-small.out","w",stdout);
    int casos;
    cin >> casos;
    forn(casito,casos)
    {
        int n,m;
        cin >> n >> m;
        forn(i,n)
        cin >> p[i].first >> p[i].second;
        forn(i,m)
            cin >> baldes[i].first >> baldes[i].second;
        cout << "Case #" << casito+1 << ": ";
        forn(i,m)
        {
            circ[0].centro = p[0];
            circ[1].centro = p[1];
            circ[0].radio = sqrt((p[0].first-baldes[i].first)*(p[0].first-baldes[i].first)+(p[0].second-baldes[i].second)*(p[0].second-baldes[i].second));
            circ[1].radio = sqrt((p[1].first-baldes[i].first)*(p[1].first-baldes[i].first)+(p[1].second-baldes[i].second)*(p[1].second-baldes[i].second));
            printf("%.8f",calc());
            if(i!=m-1)
                cout << " ";
        }
        cout << endl;
    }
}
