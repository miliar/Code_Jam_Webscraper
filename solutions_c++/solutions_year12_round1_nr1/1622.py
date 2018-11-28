#include<iostream>
#include<fstream>
#include<string>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<algorithm>
using namespace std;

double p[110000];
int main()
{
    freopen("A-small-attempt2.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    int nt;
    cin>>nt;
    for(int i=1; i<=nt; i++)
    {
        int a,b;
        cin>>a>>b;
        double ans = 2.0+b;
        cout<<"Case #" << i<<": ";
        for(int i=1; i<=a; i++)
            cin >> p[i];
        double ratio;
        for(int i=0; i<a; i++)
        {
            ratio = 1;
            for(int j=1; j<=(a-i); j++)
            {
                ratio *= p[j];
            }
            double tmp = (b-a+2*i+1)*ratio+(1-ratio)*(b-a+2*i+1+b+1);
            ans = min(ans, tmp);
        }
        ans = min(ans, a+b+1.0);
        printf("%.6f\n", ans);
    }
}
