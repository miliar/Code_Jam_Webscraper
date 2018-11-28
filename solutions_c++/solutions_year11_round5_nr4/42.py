#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <sstream>
#include <cstdlib>
#include <cstdio>
#include <cmath>
using namespace std;
#define pb push_back
#define mp make_pair
#define tr(i,v) for(typeof((v).begin()) i = (v).begin(); i != (v).end(); ++i)
#define all(x) x.begin(),x.end()

void tst()
{
    string inp;
    cin >> inp;
    vector<int> pos;
    long long val=0;
    for(int i=0;i<inp.size();i++)
        if(inp[i]=='1')
        {
            val += (1ll<<(inp.size()-1-i));
        }
        else if(inp[i]=='?')
        {
            pos.pb(inp.size()-1-i);
        }

    for(int mask=0;mask<(1<<(pos.size()));mask++)
    {
        long long vv=val;
        for(int i=0;i<pos.size();i++)
            if(mask & (1<<i))
                vv += (1ll<<pos[i]);
        long long sqsq = sqrt(vv);
        if(sqsq*sqsq == vv)
        {
            for(int i=inp.size()-1;i>=0;i--)
                if(vv & (1ll<<i))
                    cout << '1';
                else
                    cout << '0';
            cout << endl;
            return;
        }
    }

}

int main()
{
    int t;
    cin >> t;
    for(int i=1;i<=t;i++)
    {
        printf("Case #%d: ",i);
        tst();
    }
}
