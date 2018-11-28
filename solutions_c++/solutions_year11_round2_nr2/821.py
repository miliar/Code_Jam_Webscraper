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

vector <long long> pos;
int N;
double diff;
bool ispossible(double val)
{
    int i;
    double prev=pos[0]-val;
    for(i=1;i<N;i++)
    {
    if(prev+diff-pos[i] > val)
    return false;
    prev=max(pos[i]-val,prev+diff);
    }
    return true;
}
int main()
{
    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int cases,cs,i,a,b,j;
    cin>>cases;
    long long c,d;
    double min,max,mid,ans;
    for(cs=1;cs<=cases;cs++)
    {
        cin>>c>>d;
        diff=d;
        pos.clear();
        for(i=0;i<c;i++)
        {
            cin>>a>>b;
            for(j=0;j<b;j++)
                pos.push_back(a);

        }
        int len=pos.size();
        N=len;
        sort(pos.begin(),pos.end());
        min=0, max=100000;
        while(max-min>= 1e-8)
        {
            mid=(min+max)/2.00000;
            if(ispossible(mid))
                max=mid , ans=mid;
            else min=mid;
        }
        cout<<"Case #"<<cs<<": ";
        printf("%0.8lf\n",ans);

    }
    return 0;
}
