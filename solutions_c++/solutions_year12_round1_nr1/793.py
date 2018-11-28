#include <iostream>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <cmath>
#include <math.h>


using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin >> t;
    cout.precision(20);
    for (int o=1;o<=t;o++){
        cout << "Case #" << o << ": ";
        int a,b;
        cin >> a >> b;
        double  *p=new double [100001];
        double  *pr=new double [100001];
        double t=1;
        for (int i=0;i<a;i++){
            cin >> p[i];
            t*=p[i];
            pr[i]=t;
        }
        double ans=b+2;
        for (int i=0;i<a;i++){
            double e=pr[a-i-1];
            double tmp=e*(2*i+b-a+1)+(1-e)*(2*i+b-a+1+b+1);
            ans=min(ans,tmp);
        }
        cout << ans << endl;
    }
}
