#include <iostream>
#include <vector>
#include <queue>
#include <cstring>
#include <cstdio>

using namespace std;

const int maxn = 100005;
long long dis[maxn],b[1000];

class cmp{
public:
    bool operator() (int i,int j){
       if (dis[i] == -1 || dis[i] > dis[j]) return true;
       return false;
    }
};

priority_queue<int,vector<int>,cmp>  q;

int main()
{
    freopen("B.in","r",stdin); freopen("B.out","w",stdout);
    int t; scanf("%d",&t);
    for (int casenum=1; casenum <= t; ++casenum){
        long long l; cin >> l;
        int n, m = 0;
        scanf("%d",&n);
        for (int i=1; i<=n; ++i){
            cin >> b[i]; if (b[i] > m) m = b[i];
        }
        for (int i=0; i<m; ++i)
            dis[i] = -1;
        int k = (m-l%m)%m;
        dis[k] = 0;
        while (!q.empty()) q.pop();
        q.push(k);
        while (!q.empty()){
            int k = q.top(); q.pop();
            for (int i=1; i<=n; ++i){
                int y = (k + b[i]) % m;
                long long cost = dis[k]+1;
                if (k+b[i]>=m) cost--;
                if (dis[y] == -1 || cost < dis[y]) {
                    dis[y] = cost; q.push(y);
                }
            }
        }
        printf("Case #%d: ",casenum);
        if (dis[0] != -1) cout << dis[0]+(l-1)/m+1;
            else printf("IMPOSSIBLE");
        printf("\n");
    }
    return 0;
}
