#include <cstdio>



int main() {
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    
    int T, t;
    int n;
    int which[100];
    int where[100];
    
    
    scanf("%d", &T);
    for (t = 0; t < T; t++) {
        int place[2] = {1, 1};
        int i, j, k;
        char temp[2];
        
        scanf("%d", &n);
        for (i = 0; i < n; i++) {
            scanf("%s %d ", temp, &where[i]);
            which[i] = temp[0] == 'B';
        }
        
        i = 0;
        k = 0;
        for (j = 0; i < n; j++) {
            for (; which[k] == which[i] && k < n; k++);
            if (k < n) {
                if (place[which[k]] != where[k]) {
                    place[which[k]] += 2*(where[k] > place[which[k]]) - 1;
                }
            }
            if (place[which[i]] != where[i]) {
                place[which[i]] += 2*(where[i] > place[which[i]]) - 1;
            } else {
                i++;
            }
        }
        printf("Case #%d: %d\n", t+1, j);
    }
}
        
    
    
    
