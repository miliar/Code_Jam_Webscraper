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
        cout << "Case #" << o << ": "<< '\n';
        int n;
        cin >> n;
        vector <int> a(20);
        for (int i=0;i<n;i++){
            cin >> a[i];
        }
        bool ff=false;
        for (int i=1;i<(1<<20);i++){
            for (int j=1;j<(1<<20);j++){
                if (((i)&(j))==0){
                    int s=0,s2=0;
                    for (int k=0;k<20;k++){
                        if (((i) & (1 << k)) == (1 << k))
                            s+=a[k];
                        if (((j) & (1 << k)) == (1 << k))
                            s2+=a[k];
                    }
                    if (s==s2){
                        for (int k=0;k<20;k++)
                            if (((i) & (1 << k)) == (1 << k))
                                cout << a[k] << ' ';
                        cout << '\n';
                        for (int k=0;k<20;k++)
                            if (((j) & (1 << k)) == (1 << k))
                                cout << a[k] << ' ';
                        cout << '\n';
                        ff=true;
                        break;
                    }
                }
            }
            if (ff)
                break;
        }
        if (!(ff)){
            cout << "Impossible" << '\n';
        }
    }
}
