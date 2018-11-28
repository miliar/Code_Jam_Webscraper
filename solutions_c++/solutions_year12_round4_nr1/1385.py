#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<iostream>
#include<string>
#include<sstream>
#include<ctype.h>
#include<vector>
#include<map>
#include<queue>
#include<math.h>
#include<algorithm>
#include<set>

#define pb push_back
#define PI acos(-1.0)
#define SZ(a) (int)a.size()
#define csprnt printf("Case #%d: ", cas++);
#define EPS 1e-9
#define MAX 10010
#define ll long long
#define INF (1<<30)
#define pii pair<int, int>
#define MOD 1000000007

using namespace std;

struct pq
{
    int cost, node;
    pq(int n, int c)
    {
    	node=n, cost=c;
    }
    bool operator<(const pq &b)const
    {
        return (cost<b.cost);
    }
};

vector<pq>arr;
int dist[MAX];

bool cmp(pq a, pq b)
{
    if(a.node==b.node) return (a.cost>b.cost);
    return (a.node<b.node);
}

int dijk(int n, int dest)
{
    int i, now, end, cc, cur, dd;
    dist[0] = min(arr[0].node, arr[0].cost);
    priority_queue<pq>Q;
    Q.push(pq(0, dist[0]));
    while(!Q.empty())
    {
        now = Q.top().node, cur = Q.top().cost;
        Q.pop();
        dd = cur+arr[now].node;
//        cout<<"dijk "<<now<<" "<<cur<<" "<<dd<<endl;
        if(dd>=dest) return true;
        for(i=now+1;i<n;i++)
        {
            dd = arr[i].node - arr[now].node;
            if(dd>cur) break;
            cc = min(dd, arr[i].cost);
            if(dist[i]<cc)
            {
                dist[i]=cc;
                Q.push(pq(i, cc));
            }
        }
    }
    return 0;
}

int main()
{
    freopen("small.in", "r", stdin);
    freopen("small.out", "w", stdout);
    int t, cas=1;
    scanf("%d", &t);
    while(t--)
    {
        arr.clear();
        int d, i, j, n, dis, len;
        scanf("%d", &n);
        for(i=0;i<n;i++)
        {
            scanf("%d%d", &dis, &len);
            arr.pb(pq(dis, len));
        }
        scanf("%d", &d);
        sort(arr.begin(), arr.end(), cmp);
        memset(dist, -1, sizeof dist);
        int ans = dijk(n, d);
        csprnt;
        if(ans) printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}
