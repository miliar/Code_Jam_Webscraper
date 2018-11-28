#include <algorithm>
#include <cstdio>
#include <cmath>
#include <iostream>
#include <list>
#include <string>
#include <vector>
using namespace std;
#define PI 3.14159265358979323846264338327950288
typedef long long lld;

bool check(lld n, int pd, int pg)
{
    int count;
    if(pg == 100)
        {
         if (pd < 100)
         return false;
        }
    if(pg == 0)
    {
        if(pd> 0)
        return false;
    }
    count = 0;


        for(lld i = n; i>0 ; i--)
        {
            if(((i*pd)%100) == 0)
            {
                count ++;
                break;
            }
            }

    if (count == 0) return false;
    else return true;
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out5.txt","w",stdout);
    int T,pd, pg;
    lld n;
    cin >> T;
    for(int tt=0;tt<T;tt++)
    {
        cout << "Case #" << tt+1 << ": ";
        cin >> n >> pd >> pg;
        if(check(n,pd,pg))
            cout << "Possible" << endl;
        else
            cout << "Broken" << endl;
    }
    return 0;
}
