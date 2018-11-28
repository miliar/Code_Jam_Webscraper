#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <queue>
#include <string>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

const double eps=1e-8;

#define MEM(a) memset(a,0,sizeof(a));
#define FOR(i,n) for(int i=0;i<n;i++)

int a[501],sum,n,len;
string tem;
bool flag;
struct an
{
    vector<int>num;
    int sum;
} ans[2<<20+1];
vector<int>v;

void dfs(int pos)
{
    if(flag)
        return ;

    sum+=a[pos];
    v.push_back(pos);

    FOR(i,len)
    {
        if(ans[i].sum==sum)
        {
            flag=true;
            FOR(j,ans[i].num.size())
            {
                cout<<a[ans[i].num[j]]<<" ";
            }
            cout<<endl;
            FOR(j,v.size())
            {
                cout<<a[v[j]]<<" ";
            }
            cout<<endl;
            return;
        }
    }
    ans[len].sum=sum;
    ans[len].num.clear();
    FOR(i,v.size())
    {
        ans[len].num.push_back(v[i]);
    }
    len++;

    for(int i=pos+1; i<n; i++)
    {
        dfs(i);
        sum-=a[i];
        v.pop_back();
    }
}

int main()
{
    //freopen("C-small-attempt1.in","r",stdin);
    //freopen("out.txt","w",stdout);
    int t,cnt=0;
    scanf("%d",&t);
    while(t--)
    {
        flag=false;
        cnt++;
        len=1;
        v.clear();
        scanf("%d",&n);
        FOR(i,n)
        {
            scanf("%d",&a[i]);
        }
        printf("Case #%d:\n",cnt);
        FOR(i,n)
        {
            sum=0;
            tem.clear();
            dfs(i);
        }
        if(!flag)
        {
            cout<<"Impossible"<<endl;
        }
    }
    return 0;
}
