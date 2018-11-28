#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define MAX_NODES 110
#define WHITE 0
#define GRAY 1
#define BLACK 2
#define oo 1000000000
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("ans.txt","w",stdout);

    int Case;
    int d[10009],l[10009],cc,n,fin,i,j,flag,ald[10009];
    long long lim,range;
    cin>>Case;
    for(cc=1;cc<=Case;cc++)
    {
        cin>>n;
        for(i=0;i<n;i++)
        {
            cin>>d[i]>>l[i];
            ald[i]=0;
        }
        cin>>fin;
        flag=0;
        lim=2*d[0];
        for(j=1;j<n;j++)
        {
            if(d[j]>d[0]+d[0])
                    break;
                if(!ald[j])
                    ald[j]=d[0];
        }
        for(i=1;i<n;i++)
        {
            if(ald[i]==0)
            {
                flag=1;
                break;
            }
            range=min(l[i],d[i]-ald[i]);
            lim=max(lim,d[i]+range);

            for(j=i+1;j<n;j++)
            {
                if(d[j]>d[i]+range)
                    break;
                if(!ald[j])
                    ald[j]=d[i];
            }
        }
        if(lim<fin)
            flag=1;

        if(flag)
            cout<<"Case #"<<cc<<": NO\n";
        else    cout<<"Case #"<<cc<<": YES\n";

    }

    return 0;
}
