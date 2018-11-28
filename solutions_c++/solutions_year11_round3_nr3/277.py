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
#include <cstring>

using namespace std;

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    //freopen("inp.txt","r",stdin);
    //freopen("B-small-attempt1.in","r",stdin);
    //freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int cases,inp[110],cs,n,i,j,ans,l,h;
    cin>>cases;
    for(cs=1;cs<=cases;cs++)
    {
        cin>>n>>l>>h;
        for(i=0;i<n;i++)
            cin>>inp[i];
        ans=-1;
        for(i=l;i<=h;i++)
        {
            for(j=0;j<n;j++)
                if(inp[j]%i!=0 && i%inp[j]!=0)
                    break;
            if(j==n)
            {
                ans=i;
                break;
            }
        }
        if(ans!=-1)
            cout<<"Case #"<<cs<<": "<<ans<<endl;
        else
        cout<<"Case #"<<cs<<": NO"<<endl;
    }
    return 0;
}
