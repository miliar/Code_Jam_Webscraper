#include <cstdio>
using namespace std;

char mp[55][55];
int r, c;

int main(void) {
    int t;
    scanf("%d", &t);
    for (int ti = 1; ti <= t; ti++) {
        printf("Case #%d:\n", ti);
        scanf("%d %d", &r, &c);
        for (int i = 0; i < r; i++) {
            scanf("%s", mp[i]);
        }
        for (int y = 0; y < r-1; y++) {
            for (int x = 0; x < c-1; x++) {
                if(mp[y][x] == '#' && mp[y][x+1] == '#' && mp[y+1][x] == '#' && mp[y+1][x+1] == '#') {
                    mp[y][x] = '/';
                    mp[y][x+1] = '\\';
                    mp[y+1][x] = '\\';
                    mp[y+1][x+1] = '/';
                } 
            }
        }
        bool f = true;
        for (int y = 0; y < r; y++) {
            for (int x = 0; x < c; x++) {
                if(mp[y][x] == '#') f = false;
            }
        }
        if(f) {
            for (int i = 0; i < r; i++) {
                printf("%s\n", mp[i]);
            }
        } else {
            printf("Impossible\n");
        }
    }
    return 48-48;
}
