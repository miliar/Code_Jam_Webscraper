#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int t, n, xr;
vector<int> ci;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin>>t;
    for(int test = 1; test <= t; test++)
    {
        ci.clear();
        cin>>n;
        ci.resize(n);
        for(int i = 0; i < n; i++)
            cin>>ci[i];
        sort(ci.begin(), ci.end());
        xr = 0;
        for(int i = 0; i < ci.size(); i++)
            xr ^= ci[i];
        cout<<"Case #"<<test<<": ";
        if(xr != 0)
        {
            cout<<"NO"<<endl;
            continue;
        }
        xr = 0;
        for(int i = 1; i < ci.size(); i++)
            xr += ci[i];
        cout<<xr<<endl;
    }
    return 0;
}