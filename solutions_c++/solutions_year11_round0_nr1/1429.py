#include <cstdio>
#include <cstring>
#include <vector>

#define abs(n) (n > 0 ? n : -(n))

using namespace std;

typedef pair<int,int> ii;

int T,C=1;
int n;
vector<ii> po, pb;
char robo[12];

int main() {

    for (scanf("%d",&T);T--;) {
        scanf("%d",&n);
        po.clear();
        pb.clear();
        for (int i=0;i<n;i++) {
            int p;
            scanf("%s %d",robo,&p);
            if (robo[0]=='O')
                po.push_back(ii(p,i));
            else
                pb.push_back(ii(p,i));
        }
        int t=0, to =0, tb = 0;
        int o,b;
        o=b=1;
        int oks=0;
        while (to < (int)po.size() and tb<(int)pb.size()) {
            bool merda=false;
            if (po[to].first > o) {
                o++;
            } else if (po[to].first < o) {
                o--;
            } else if (oks == po[to].second) {
                oks++;
                to++;
                merda=true;
            }
            if (pb[tb].first > b) {
                b++;
            } else if (pb[tb].first < b) {
                b--;
            } else  if (oks == pb[tb].second and !merda) {
                tb++;
                oks++;
            }
            t++;
        }
        while (to < (int)po.size()) { t += abs(po[to].first - o) + 1; o =
            po[to].first; to++; }
        while (tb < (int)pb.size()) { t += abs(pb[tb].first - b) + 1; b =
            pb[tb].first; tb++; }
        printf("Case #%d: %d\n",C++,t);
    }

    return 0;
}
