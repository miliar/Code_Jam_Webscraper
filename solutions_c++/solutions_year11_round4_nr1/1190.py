#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
#include <cstring>
#include <vector>
#include <map>
#include <set>

using namespace std;

const int MAXN = 1100;
const double eps = 1e-8;
int cases;
struct node{
       int x, y, add;
}p[MAXN];
struct node2{ 
       int L, v, a;
}rec[MAXN];

bool cmp(const node &p, const node &q) {
    if (p.x < q.x) return true;
    return false; 
}

bool cmp2(const node2 &p, const node2 &q) {
     if (p.v < q.v) return true;
     return false;
}

int L, walkV, runV, runT, n;

int main() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    
    scanf("%d",&cases);
    for (int rep = 0; rep < cases; ++rep) { 
        scanf("%d%d%d%d%d",&L, &walkV, &runV, &runT, &n);
        for (int i = 0; i < n; ++i) {
            scanf("%d%d%d",&p[i].x, &p[i].y, &p[i].add);
        }
        sort(p + 0, p + n, cmp);
        int totNotAddL = 0;
        int start = 0;
        for (int i = 0; i < n; ++i) {
            int nowx = p[i].x;
            int nowy = p[i].y;
            totNotAddL += abs(nowx - start);
            start = nowy;
        }
        totNotAddL += abs(L - start);
        for (int i = 0; i < n; ++i) {
            rec[i].L = p[i].y - p[i].x;
            rec[i].v = walkV + p[i].add;
            rec[i].a = p[i].add;
        }
        rec[n].L = totNotAddL;
        rec[n].v = walkV;
        rec[n].a = 0;
        ++n;
        sort(rec + 0, rec + n, cmp2);
        double ret = 0;
        double leftT = runT;
        for (int i = 0; i < n; ++i) {
            if (leftT < eps) {
               ret += rec[i].L * 1.0 / rec[i].v;
            }else {
               double needT = 0;
               needT = rec[i].L * 1.0 / (runV + rec[i].a);  
               if (needT > leftT) {
                   ret += (rec[i].L * 1.0 - leftT * (runV + rec[i].a)) / (rec[i].v) + leftT;
                   leftT = 0;
               }else {
                   leftT -= needT;
                   ret += needT;
               }
            }
            //printf("ret = %lf i = %d, leftT = %lf\n",ret, i, leftT);
        }
        printf("Case #%d: %.8lf\n",rep + 1, ret);
    }
    
    fclose(stdin);
    fclose(stdout);
    return 0;
}
