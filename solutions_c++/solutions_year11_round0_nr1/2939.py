# include <stdio.h>
# include <algorithm>
# include <iostream>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    int cas,t,n,b,time;
    char r;
    int pos[128],tm[128];
    cin>>t;
    for(cas=1;cas<=t;cas++)
    {
        pos['O'] = pos['B'] = 1;
        tm['O'] = tm['B'] = 0;
        time = 0;
        cin>>n;
        for(int i=0;i<n;i++)
        {
            cin>>r>>b;
            time = tm[r] = max( tm[r] + abs ( b - pos[r] ) , time ) + 1;
            pos[r] = b;
        }
        printf("Case #%d: %d\n",cas,time);
    }
    return 0;
}
