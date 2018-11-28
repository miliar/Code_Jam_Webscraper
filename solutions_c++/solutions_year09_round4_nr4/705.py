#include <fstream>
#include <iomanip>
#include <string>
#include <algorithm>
#include <cmath>

using namespace std;

ifstream fin("D.in");
ofstream fout("D.out");

double dist(double x1,double y1,double x2,double y2)
{
    return sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
}

double Max(double a,double b)
{
    if (a > b)  return a;
    return b;
}

int tst;

double x[54], y[54], r[54];

void solve()
{
    int n;
    
    fin >> n;
    
    for (int i=1;i<=n;++i)
        fin >> x[i] >> y[i] >> r[i];

        
    if (n == 1)
    {
        fout << "Case #" << ++tst << ": " << setprecision(6) << fixed << r[1] << "\n";
        return;
    }
    
    if (n == 2)
    {
        double ret = r[1];
        if (r[2] > ret)
            ret = r[2];

        fout << "Case #" << ++tst << ": " << setprecision(6) << fixed << ret << "\n";
        return;
    }
    
    if (n == 3)
    {
        double tmp;
        
        tmp = r[3];

        tmp = Max(tmp,( dist(x[1],y[1],x[2],y[2])+r[1]+r[2] )/2);

        double ret = tmp;
        
        tmp = r[2];

        tmp = Max(tmp,( dist(x[1],y[1],x[3],y[3])+r[1]+r[3] )/2);

        if (tmp < ret)
            ret = tmp;

        tmp = r[1];

        tmp = Max(tmp,( dist(x[2],y[2],x[3],y[3])+r[2]+r[3] )/2);

        if (tmp < ret)
            ret = tmp;

        fout << "Case #" << ++tst << ": " << setprecision(6) << fixed << ret << "\n";
        return;
    }
}
    

int main()
{
    int t;
    
    fin >> t;
    
    while (t--)
        solve();
        
        
    return 0;
}
