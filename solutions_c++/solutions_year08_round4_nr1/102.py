#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

void tst()
{
    int m,v;
    cin >> m >>v;
    int wew = (m-1)/2;
    vector<int> val(m+1);
    vector<bool> chang(wew+1);
    vector<bool> typ(wew+1);

    for(int i=1;i<=wew;i++)
    {
        int g,c;
        cin >> g >> c;
        typ[i]=g;
        chang[i]=c;
    }
    for(int i=wew+1;i<=m;i++)
    {
        cin >> val[i];
    }

    vector<long long> cost(m+1,1000000000);
    for(int i=wew;i>=1;i--)
    {
        if(typ[i])
            val[i] = val[2*i] && val[2*i+1];
        else
            val[i] = val[2*i] || val[2*i+1];

        if(val[i])
        {
            if(typ[i])
            {
                cost[i] = min(cost[2*i],cost[2*i+1]);
            }
            else
            {
                cost[i] = (val[2*i]?cost[2*i]:0) + (val[2*i+1]?cost[2*i+1]:0);
                if(chang[i])
                {
                    if(val[2*i] && val[2*i+1])
                        cost[i] = min(cost[i],1+min(cost[2*i],cost[2*i+1]));
                    else
                        cost[i] = min(cost[i],1ll);
                }
            }
        }
        else
        {
            if(typ[i])
            {
                cost[i] = (val[2*i]?0:cost[2*i]) + (val[2*i+1]?0:cost[2*i+1]);
                if(chang[i])
                {
                    if(!val[2*i] && !val[2*i+1])
                        cost[i] = min(cost[i],1+min(cost[2*i],cost[2*i+1]));
                    else
                        cost[i] = min(cost[i],1ll);
                }
            }
            else
            {
                cost[i] = min(cost[2*i],cost[2*i+1]);
            }

        }

        //cout << i << ' ' << val[i] << ' ' << cost[i] << endl;


    }
    if(val[1]==v)
    {
        cout << 0;
        return;
    }
    if(cost[1] < 1000000000)
    cout << cost[1];
    else
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
