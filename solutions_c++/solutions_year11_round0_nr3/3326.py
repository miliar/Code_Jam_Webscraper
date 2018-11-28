#include<iostream>
#include<vector>
#include<cstdio>
#include<map>

#define sz(c) (int)c.size()

using namespace std;

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int T;
    cin>>T;
    for(int t = 0; t < T; t++)
    {
        int n;
        cin>>n;
        vector<int> v(n);
        int sum = 0, xsum = 0;
        int vmin = 100000000;
        for(int i = 0; i < n; i++)
        {
            cin>>v[i];
            sum += v[i];
            xsum ^= v[i];
            vmin = min(v[i],vmin);
        }

        if(xsum == 0)
            cout<<"Case #"<<(t+1)<<": "<<(sum - vmin)<<endl;
        else
            cout<<"Case #"<<(t+1)<<": NO"<<endl;
    }
}

