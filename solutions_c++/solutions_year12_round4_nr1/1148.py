#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

int d[10001];
int l[10001];
int v[10001];

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t;
    cin>>t;
    for (int no = 1; no <= t; no++)
    {
        int n;
        cin>>n;
        for (int i = 0; i < n; i++)
            cin>>d[i]>>l[i];
        int D;
        cin>>D;
        memset(v, 0, sizeof(v));
        bool flag = false;
        v[0] = 2 * min (d[0], l[0]);
        if (v[0] >= D) flag = true;
        for (int i = 0; i < n; i++)
        {
            if (flag == true) break;
            for (int j = i+1; j < n; j++)
            {
                if (d[j] <= v[i]) // can
                {
                    v[j] = max (v[j], d[j]+min(l[j], d[j]-d[i]));
                    if (v[j] >= D)
                    {
                        flag = true;
                        break;
                    }
                }
            }
        }

        if (flag) cout<<"Case #"<<no<<": "<<"YES"<<endl;
        else cout<<"Case #"<<no<<": "<<"NO"<<endl;
        cerr << no << endl;
    }
}
