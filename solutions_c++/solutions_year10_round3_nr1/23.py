#include <cstdio>
#include <algorithm>
using namespace std;

int main(int argc, char **argv) {
    int tc; scanf("%d", &tc);
    for(int tci = 0; tci < tc; tci++) {
        int n; scanf("%d", &n);
        static pair<int,int> aas[1000],bbs[1000];
        for(int i = 0; i < n; i++) {
            int a,b; scanf("%d%d", &a, &b);
            aas[i]=make_pair(a,i);
            bbs[i]=make_pair(b,i);
        }
        sort(aas, aas+n);
        sort(bbs, bbs+n);
        static int as[1000],bs[1000];
        for(int i = 0; i < n; i++) {
            as[aas[i].second]=i;
            bs[bbs[i].second]=i;
        }
        static int cs[1000];
        for(int i = 0; i < n; i++) {
            cs[as[i]]=bs[i];
            //printf("cs[%d]=%d\n",i,cs[i]);
        }
        int count = 0;
        for(int i = 0; i < n; i++) {
            for(int j = 0; j+1 < n; j++) {
                if(cs[j]>cs[j+1]) {
                    swap(cs[j],cs[j+1]);
                    count++;
                }
            }
        }
        printf("Case #%d: %d\n", tci+1, count);
    }
    return 0;
}
