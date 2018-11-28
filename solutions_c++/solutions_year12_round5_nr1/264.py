#include <stdio.h>
#include <cstdio>
#include <algorithm>

using namespace std;

struct S {
    int id;
    int time;
    int percentage;
    bool operator <(const S& rhs) const {
        if (percentage > rhs.percentage) return true;
        if (percentage < rhs.percentage) return false;
        if (time > rhs.time) return true;
        if (time < rhs.time) return false;
        if (id < rhs.id) return true;
        return false;
    }
} s[1024];

int n;

int main(int argc, char const *argv[]) {
    int T;
    scanf("%d", &T);
    for (int ti = 0; ti < T; ++ti) {
        printf("Case #%d:", ti+1);
        scanf("%d", &n);
        for (int i = 0; i < n; ++i) {
            scanf("%d", &s[i].time);
            s[i].id = i;
        }
        for (int i = 0; i < n; ++i) {
            scanf("%d", &s[i].percentage);
        }
        sort(s, s+n);
        for (int i = 0; i < n; ++i) {
            printf(" %d", s[i].id);
        }
        printf("\n");
    }
    return 0;
}
