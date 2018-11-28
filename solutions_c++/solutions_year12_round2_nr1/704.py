#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <math.h>
#include <cmath>
#include <stdio.h>

using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin >> t;
    cout.precision(9);
    for (int o=1;o<=t;o++){
        cout << "Case #" << o << ": ";
        int n;
        cin >> n;
        vector<int> a(201,0);
        int x=0;
        for (int i=0;i<n;i++){
            cin >> a[i];
            x+=a[i];
        }
        for (int i=0;i<n;i++){
            double l=0,r=1;
            for (;r-l>0.00000000001;){
                double m=(l+r)/2.0;
                double sc=a[i]+x*m;
                bool f=true;
                double y=1-m;
                for (int j=0;j<n;j++){
                    if ((i!=j)&&(a[j] < sc)){
                        y-=(sc-a[j])*1.0/x;
                    }
                    if (y < 0)
                        f=false;
                }
                if (f) l=m;
                else r=m;
            }
            cout << l*100 << ' ';
        }
        cout << '\n';
    }
}
