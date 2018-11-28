#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstdlib>
using namespace std;

int main() {
    int n; scanf("%d", &n);
    for (int cas = 1; cas <= n; cas++) {
        int ta, na, nb;
        scanf("%d %d %d", &ta, &na, &nb);
        vector<int> arrivea, arriveb, leavea, leaveb;
        for (int i = 0; i < na; i++) {
            int h, m;
            scanf("%d:%d", &h, &m);
            leavea.push_back(h*60+m);
            scanf("%d:%d", &h, &m);
            arriveb.push_back(h*60+m+ta);
        }
        for (int i = 0; i < nb; i++) {
            int h, m;
            scanf("%d:%d", &h, &m);
            leaveb.push_back(h*60+m);
            scanf("%d:%d", &h, &m);
            arrivea.push_back(h*60+m+ta);
        }
        sort(leavea.begin(), leavea.end());
        sort(leaveb.begin(), leaveb.end());
        sort(arrivea.begin(), arrivea.end());
        sort(arriveb.begin(), arriveb.end());
        vector<int> numata(24*60+1, 0);
        vector<int> numatb(24*60+1, 0);
        for (int i = 0; i < na; i++) {
            for (int j = arriveb[i]; j <= 24*60; j++) numatb[j]++;
        }
        for (int i = 0; i < nb; i++) {
            for (int j = arrivea[i]; j <= 24*60; j++) numata[j]++;
        }
        int numa = 0;
        int numb = 0;
        for (int i = 0; i < na; i++) {
            if (numata[leavea[i]] == 0) {
                numa++;
            } else {
                for (int j = leavea[i]; j <= 24*60; j++) numata[j]--;
            }
        }
        for (int i = 0; i < nb; i++) {
            if (numatb[leaveb[i]] == 0) {
                numb++;
            } else {
                for (int j = leaveb[i]; j <= 24*60; j++) numatb[j]--;
            }
        }
        printf("Case #%d: %d %d\n", cas, numa, numb);
    }
}

