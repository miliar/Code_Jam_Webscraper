#include <cstdio>
#include <algorithm>
#include <cassert>
#include <vector>

using namespace std;

int get() { int x; scanf("%d",&x); return x;}

void go() {
    int n = get();
    int k = get();
    int b = get();
    int t = get();
    vector<int> xs(n);
    for(int i=0;i<n;i++) {
        xs[i] = get();
    }
    vector<int> vs(n);
    for(int i=0;i<n;i++) {
        vs[i] = get();
    }
#define x first
#define y second
    vector<int> dist(n);
    for(int i=0;i<n;i++) {
        dist[i] = b - xs[i];
    }
    vector<bool> isBadLine(n);
    int badLines=0;
    for(int i=0;i<n;i++) {
        isBadLine[i]=(dist[i] > t*vs[i]);
        if(isBadLine[i])badLines++;
    }
    if(n - badLines<k) {
        printf("IMPOSSIBLE\n");
        return;
    }
    vector<int> cost(n);
    for(int i=0;i<n;i++) {
        if(isBadLine[i])cost[i]=200;
        for(int j=0;j<n;j++) {
            if(i!=j) {
                if(isBadLine[j]&&dist[i]>dist[j])cost[i]++;
            }
        }
    }
    int answer=0;
    sort(cost.begin(),cost.end());
    for(int i=0;i<k;i++) {
        assert(cost[i]<200);
        answer+=cost[i];
    }
    printf("%d\n",answer);
}

int main() {
    int n = get();
    for(int i =0;i<n;i++) {
        printf("Case #%d: ",i+1);
        go();
    }
}
