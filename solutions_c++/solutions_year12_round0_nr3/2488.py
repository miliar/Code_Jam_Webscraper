#include <iostream>
#include <vector>
#include <stdio.h>
#include <cmath>
#include <math.h>
#include <set>

using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin >> t;
    vector <int> f;
    for (int i=0;i<9;i++) f.push_back((int)pow(10,i));
    for (int i=1;i<=t;i++){
        cout << "Case #" << i<< ": ";
        int a,b;
        cin >> a >> b;
        long long ans=0;
        for (int j=a;j<b;j++){
            set <int> can;
            can.clear();
            int l=0;
            while (pow(10,l) <= j) l++;
            for (int k=0;k<l;k++){
                int r=j;
                r=(j%f[l-k])*f[k];
                r+=j/f[l-k];
                if ((r > j)&&(r<=b)&&(can.count(r)==0)){
                    ans++;
                    can.insert(r);
                }
            }
        }
        cout << ans << endl;
    }
}
