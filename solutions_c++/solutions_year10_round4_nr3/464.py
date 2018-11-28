#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <cstring>
#include <map>
#include <queue>
using namespace std;

#define REP(i,n) for (int _n=(n),i=0;i!=_n;++i)
#define SZ(v) (int)(v).size()
#define CL(v,x) memset((v),(x),sizeof(v))
#define MP make_pair

typedef long long ll;
typedef pair<int, int> pii;
typedef map<pii, int>::iterator mpit;

map<pii, int> tab;
ll ret, tot;
int x1[2000], y1[2000], x2[2000], y2[2000];

int main() {
    freopen("input.in", "r", stdin);
    int T;
    scanf("%d", &T);
    REP(t,T) {
        printf("Case #%d: ", t+1);
        int R;
        scanf("%d", &R);
        ret = tot = 0;
        tab.clear();
        REP(i,R) {
            scanf("%d%d%d%d", &x1[i], &y1[i], &x2[i], &y2[i]);
            for (int x=x1[i];x<=x2[i];++x) {
                for (int y=y1[i];y<=y2[i];++y) {
                    pii z = MP(x, y);
                    if (tab.find(z)==tab.end()) {
                        tab[z] = 1;
                        ++tot;
                    }
                }
            }
        }

        queue<pair<int, int> > Q, nQ;
        for (typeof(tab.begin()) it=tab.begin();it!=tab.end();++it) {
            mpit lf = tab.find(MP(it->first.first-1, it->first.second));
            mpit rt = tab.find(MP(it->first.first, it->first.second-1));

            if (((lf==tab.end()) || (lf->second==0)) &&
                ((rt==tab.end()) || (rt->second==0))) 
            {
                Q.push(it->first);
            }

            int i = it->first.first;
            int j = it->first.second + 1;
            if (tab.find(MP(i,j))==tab.end()) {
                mpit another = tab.find(MP(i-1,j));
                if (another!=tab.end()) {
                    nQ.push(MP(i,j));
                }
            }
        }

        while (tot!=0) {
            ++ret;
            int len = Q.size();
            while (len>0) {
                pii now = Q.front();
                Q.pop();
                tab.erase(now);
                --tot;
                --len;

                int i = now.first;
                int j = now.second + 1;
                mpit another = tab.find(MP(i,j));
                if (another!=tab.end()) {
                    if (tab.find(MP(i-1,j))==tab.end()) {
                        Q.push(another->first);
                    }
                }

                i = now.first + 1;
                j = now.second;
                another = tab.find(MP(i,j));
                if (another!=tab.end()) {
                    if (tab.find(MP(i,j-1))==tab.end()) {
                        Q.push(another->first);
                    }
                }
            }

            len = nQ.size();
            while (len>0) {
                pii now = nQ.front();
                nQ.pop();
                ++tot;
                --len;

                tab[now] = 1;
                int i = now.first;
                int j = now.second + 1;
                mpit another = tab.find(MP(i,j));
                if (another==tab.end()) {
                    if (tab.find(MP(i-1,j))!=tab.end()) {
                        nQ.push(MP(i,j));
                    }
                }

                i = now.first + 1;
                j = now.second;
                another = tab.find(MP(i,j));
                if (another==tab.end()) {
                    if (tab.find(MP(i,j-1))!=tab.end()) {
                        nQ.push(MP(i,j));
                    }
                }
            }
        }

        printf("%d\n", ret);
    }
    return 0;
}
