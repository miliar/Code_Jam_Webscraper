#include <iostream>
#include <string.h>

using namespace std;

char st[30], zaloga[30], res[30];
int len, T, t, role1, konec;
bool used[30];

void solve(int first, int pos) {
    if (konec)
        return;

    if (pos == len) {
        if (role1)
            role1 = 0;
        else
            {
                res[pos] = 0;
                //if (strcmp(res, st) != 0) {
                    cout << "Case #" << t + 1 << ": " << res << endl;
                    konec = 1;
                //}
            }
        return;
    }

    int lastused = -1;

    for (int i = 0; i < len; i++) {
        if ((!role1 || zaloga[i] >= st[pos]) && !used[i] && (!first || zaloga[i] != '0') && (zaloga[i] != lastused)) {
            used[i] = 1;
            lastused = res[pos] = zaloga[i];
            solve(0, pos + 1);
            used[i] = 0;
        }
    }
}

int main() {
    cin >> T;
    for (t = 0; t < T; t++) {
            scanf("%s", st);
            len = strlen(st);
            memcpy(zaloga, st, len);
            memset(used, 0, sizeof(used));
            sort(zaloga, zaloga + len);
            role1 = 1;
            konec = 0;
            solve(1, 0);
            if (!konec) {
                zaloga[len++] = '0';
                sort(zaloga, zaloga + len);
                role1 = 0;
                memset(used, 0, sizeof(used));
                solve(1, 0);
            }
    }
}
