#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cctype>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <stack>
#include <queue>
#include <deque>
#include <vector>
#include <map>
#include <set>
using namespace std;
int cmp(pair<int,int> a,pair<int,int> b)
{
    return a.first < b.first;
}
struct state
{
    int pos;
    int len;
    int n;
    state()
    {

    }
    state(int p,int l,int nn)
    {
        pos = p;len = l; n =nn;
    }
};
state mk(int p,int l,int n)
{
    state r(p,l,n);
    return r;
}
int main()
{
    //freopen("input","r",stdin);
    //freopen("output","r",stdout);
    int tt;
    cin >> tt;
    for(int ii=1;ii<=tt;ii++)
    {
        int nline;
        cin >> nline;
        pair<int,int> line[nline];
        for(int k=0;k<nline;k++) cin >> line[k].first >> line[k].second;
        int dis;
        cin >> dis;
        queue<state> q; //pos, len
        if(line[0].first - line[0].second <=0) q.push(mk(line[0].first,line[0].first,1));
        int ans = 0;
        while(!q.empty())
        {
            state v;
            v = q.front();
            //cout << "travel to " << v.pos <<  "len " << v.len << endl;
            q.pop();
            if(v.pos + v.len >= dis)
            {
                ans = 1;
                break;
            }
            for(int k=v.n;k<nline && v.pos + v.len >= line[k].first;k++)
            {
                q.push(mk(line[k].first,min(line[k].first - v.pos,line[k].second),k+1));
            }
        }
        printf("Case #%d: ",ii);
        if(ans == 1) cout << "YES" << endl;
        else cout << "NO" << endl;
    }
    return 0;
}
