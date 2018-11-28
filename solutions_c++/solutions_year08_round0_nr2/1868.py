#include <cstdio>
#include <algorithm>
using namespace std;

#define maxn 100

struct route{
    int start, end;
    bool used;
    route(){
        start = 0; end = 0; used = false;
    }
    route(int a, int b){
        start = a; end = b; used = false;
    }
};

bool operator < (const route &a, const route &b){
    if (a.start < b.start) return true;
    if (a.start == b.start && a.end < b.end) return true;
    return false;
}
route routes[2][maxn];
route routest[maxn];

void go(int start, int n[2], int ctime, int turnaround){
    for (int i = 0; i < n[start]; i++){
        if (routes[start][i].start >= ctime && !routes[start][i].used){
            routes[start][i].used = true;
            go((start+1)%2, n, routes[start][i].end+turnaround, turnaround);
            break;
        }
    }
}

int main(){
    freopen("train.in", "r", stdin);
    int cases;
    scanf("%d\n", &cases);
    for (int casenr = 0; casenr < cases; casenr++){
        int turnaround;
        scanf("%d\n", &turnaround);
        int n[2];
        scanf("%d %d\n", &n[0], &n[1]);
        for (int i = 0; i < n[0]; i++){
            int th1, tm1, th2, tm2;
            scanf("%d:%d %d:%d", &th1, &tm1, &th2, &tm2);
            routest[i] = route(th1*60+tm1, th2*60+tm2);
        }
        sort(routest, routest+n[0]);
        for (int i = 0; i < n[0]; i++)
            routes[0][i] = routest[i];
        for (int i = 0; i < n[1]; i++){
            int th1, tm1, th2, tm2;
            scanf("%d:%d %d:%d", &th1, &tm1, &th2, &tm2);
            routest[i] = route(th1*60+tm1, th2*60+tm2);
        }
        sort(routest, routest+n[1]);
        for (int i = 0; i < n[1]; i++)
            routes[1][i] = routest[i];

        int used[2] = {0};
        while (true){
            int point[2]={0};
            for (int start = 0; start < 2; start++){
                while (routes[start][point[start]].used == true && point[start] < n[start]){
                    point[start]++;
                }
            }
            int start;
            if (point[0] >= n[0] && point[1] >= n[1])
                break;
            if (point[0] >= n[0])
                start = 1;
            if (point[1] >= n[1])
                start = 0;
            if (point[0] < n[0] && point[1] < n[1]){
                if (routes[0][point[0]].start < routes[1][point[1]].start)
                    start = 0;
                else
                    start = 1;
            }
            used[start]++;
            go(start, n, routes[start][point[start]].start, turnaround); 
        }
        printf("Case #%d: %d %d\n", casenr+1, used[0], used[1]);
    }
}
