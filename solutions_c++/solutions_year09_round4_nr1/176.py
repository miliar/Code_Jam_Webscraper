#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int tst()
{
    int r;
    scanf("%d ",&r);
    vector<int> y(r);
    for(int i=0;i<r;i++)
    {
        for(int j=0;j<r;j++)
        {
            char u;
            scanf(" %c",&u);
            u -= '0';
            if(u==1)
                y[i] = max(y[i],j);
        }
        
    }
    int ans=0;

    vector<int> pos(r);
    vector<bool> used(r);
    for(int val=0;val<r;val++)
    {
        int i;
        int cnt=0;
        for(i=0;;i++)
        {
            if(!used[i] && y[i]<=val)
                break;
            if(!used[i])
                cnt++;
        }
        used[i] = true;
        ans += cnt;
    }
    return ans;
}
int main()
{
    int n;
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
    {
        cout << "Case #" << i << ": " << tst() << endl;
    }
}
