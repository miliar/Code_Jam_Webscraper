#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <math.h>
#include <set>
using namespace std;

double p[1000010];
int main()
{
    freopen("testA.in","r",stdin);
    freopen("testA.out","w",stdout);

    int T;
    cin >> T;

    for(int tc=1; tc<=T; tc++)
    {
        double A, B;
        cin >> A >> B;
        for(int i=0; i<A; i++)
        cin >> p[i];

        double tp=1.0, bp=B+2.0;
        for(int i=0; i<=A; i++)
        {
            double j=i;
            double ep=A+B-2.0*j+1.0+(1.0-tp)*(B+1.0);
            bp=min(ep,bp);
            tp*=p[i];
        }

        printf("Case #%i: %llf\n",tc,bp);
    }
    return 0;
}
