#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
using namespace std;

void tst()
{
    long long n,m,a;
    cin >> n >> m >> a;
    map<int,pair<int,int> > ma;
    for(int i=0;i<=n;i++)
        for(int j=0;j<=m;j++)
        {
            int c = i*j;
            if(ma.find(c) == ma.end())
                ma[c] = make_pair(i,j);
        }

    for(map<int,pair<int,int> >::iterator it = ma.begin(); it != ma.end(); ++it)
    {
        if(ma.find(it->first+a) != ma.end())
        {
            int x = it->second.first;
            int v = it->second.second;
            it = ma.find(it->first+a);
            int u = it->second.first;
            int y = it->second.second;
            cout << "0 0 " << x << ' ' << y << ' ' << u << ' ' << v;
            return;
        }
    }
    cout << "IMPOSSIBLE";
}

int main()
{
    int n;
    cin >> n;
    for(int i=1;i<=n;i++)
    {
        cout << "Case #"<<i<<": ";tst();cout<<endl;
    }
}
