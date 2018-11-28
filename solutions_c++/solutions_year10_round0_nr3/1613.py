#include <iostream>
using namespace std;

#define MAX_GROUP 1010
int main()
{
    int t, c;
    freopen("C-large.in", "r", stdin);
    freopen("c-large.out", "w", stdout);
    cin>>t;
    for(c=1;c<=t;c++)
    {
        int r, k, n, i, j;
        long long group[MAX_GROUP];
        long long now_fare[MAX_GROUP];
        memset(now_fare, -1, sizeof(now_fare));
        int now_end[MAX_GROUP];
        cin>>r>>k>>n;
        for(i=0;i<n;i++) cin>>group[i];
        int now=0;
        long long fare=0;
        for(j=0;j<r;j++)
        {
            int total=0;
            if(now_fare[now] != -1)
            {
                total=now_fare[now];
                now=now_end[now];
            }
            else
            {
                int pre=now;
                int taken=0;
                while(taken < n)
                {
                    if(total+group[now] > k) break;
                    taken++;
                    total+=group[now];
                    now=(now+1)%n;
                }
                now_fare[pre]=total;
                now_end[pre]=now;
            }
            //if(taken >= n) break;
            fare+=total;
            //assert(fare>=0);
        }
        cout<<"Case #"<<c<<": "<<fare<<endl;
    }
    return 0;
}
