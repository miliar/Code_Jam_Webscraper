#include <cstdio>
#include <vector>
#include <string>
#include <numeric>
#include <cstring>
#include <cassert>
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <algorithm>
using namespace std;

typedef pair<int,int> PII;
typedef long long LL;
const int INF = 1000000007;

int main(){
    int cs,no=0;
    scanf("%d",&cs);
    while(cs--){
        int n,m;
        PII a[10000];
        scanf("%d",&n);
        for(int i=0;i<n;i++)
            scanf("%d%d",&a[i].first,&a[i].second);
        scanf("%d",&m);
        queue<PII> q;
        set<PII> mov;
        q.push({0,a[0].first});
        mov.insert(q.front());
        while(q.size()){
            int t=q.front().first;
            int h=q.front().second;
            int x=a[t].first;
            if(x+h>=m) break;
            q.pop();
            //printf("x = %d, h = %d\n",x,h);
            for(int i=t-1;~i;i--){
                if(a[i].first<x-h) break;
                PII u={i,min(x-a[i].first,a[i].second)};
                if(!mov.count(u)){
                    mov.insert(u);
                    q.push(u);
                }
            }
            for(int i=t+1;i<n;i++){
                if(a[i].first>x+h) break;
                PII u={i,min(a[i].first-x,a[i].second)};
                if(!mov.count(u)){
                    mov.insert(u);
                    q.push(u);
                }
            }
        }
        printf("Case #%d: ",++no);
        if(q.size()) puts("YES"); else puts("NO");
    }
}
