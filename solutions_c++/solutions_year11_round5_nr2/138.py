#include <iostream> 
#include <cstring>
#include <cstdio>
#include <algorithm>
using namespace std;

int seq[1010];
int seq_len;

void init() {
    cin >> seq_len;
    for (int i = 1; i <= seq_len; i ++)
        cin >> seq[i];
}

pair<int, int> a[1010];
int n;

int list[1010], len;

bool check(int limit) {
    len = 0;
    for (int i = 1; i <= n; i ++) {
        int c = a[i].second;
        if (c < len) {
            sort(list+1, list+len+1);
            while (c < len)
                if (list[len] < limit)
                    return false;
                else
                    len --;
        } else
            while (c > len)
                list[++ len] = 0;
        for (int k = 1; k <= len; k ++)
            list[k] ++;
    }
    for (int i = 1; i <= len; i ++)
        if (list[i] < limit)
            return false;
    return true;
}

int compute() {
    //for (int i = 1; i <= n; i ++) printf("%d ", a[i].second); printf("\n");
    //check(4);return 0;
    
    int le = 1, ri = n;
    while (le < ri) {
        int mid = (le+ri+1) / 2;
        if (check(mid))
            le = mid;
        else
            ri = mid-1;
    }
    return le;
}

void solve(int case_index) {
    printf("Case #%d: ", case_index);
    if (seq_len == 0) {
        printf("0\n");
        return;
    }
    int ans = 1<<30;
    sort(seq+1, seq+seq_len+1);
    for (int i = 1, j; i <= seq_len; i = j+1) {
        for (j = i; j < seq_len && seq[j+1]-seq[j]<=1; j ++);
      //  printf("i=%d j=%d seq[i]=%d\n",i,j,seq[i]);
        n = 0;
        for (int k = i, la = -1; k <= j; k ++) {
            if (seq[k] > la)
                a[++ n] = make_pair(la = seq[k], 0);
            a[n].second ++;
        }
        ans = min(ans, compute());
    }
    printf("%d\n", ans);
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.txt", "w", stdout);
    int case_count;
    scanf("%d", &case_count);
    for (int i = 1; i <= case_count; i ++) {
        cerr<<i<<endl;
        init();
        solve(i);
    }
    return 0;
}
