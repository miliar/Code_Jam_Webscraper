#include <stdio.h>
#include <iostream>
#include <vector>
using namespace std;

// #include <wara_lib.cc>
// #include <wara_list.cc>
// #include <wara_hash.cc>

typedef unsigned long long u_longlong;
typedef unsigned long u_long;

// #define DEBUG
// #define HASH_LEN 256

int check(char a, char b)
{
    if (b == 'T') {
        return (1);
    }
    if (a == b) {
        return (1);
    }
    return (0);
}

int check2(char data[][4])
{
    long long i;
    long long j;

    for (i = 0; i < 4; i++) {
        for (j = 0; j < 4; j++) {
            if (data[i][j] == '.') {
                return (0);
            }
        }
    }

    return (1);
}

const char *calc(char data[][4])
{
    long long i;
    long long j;
    char a;

    for (i = 0; i < 4; i++) {
        a = data[i][0];
        if (a == '.') {
            continue;
        } else if (a == 'T') {
            a = data[i][1];
            if (a == '.') {
                continue;
            }
        }

        for (j = 0; j < 4; j++) {
            if (!check(a, data[i][j])) {
                break;
            }
        }
        if (j < 4) {
            continue;
        }

        if (a == 'O') {
            goto o_won;
        } else {
            goto x_won;
        }
    }

    for (i = 0; i < 4; i++) {
        a = data[0][i];
        if (a == '.') {
            continue;
        } else if (a == 'T') {
            a = data[1][i];
            if (a == '.') {
                continue;
            }
        }

        for (j = 0; j < 4; j++) {
            if (!check(a, data[j][i])) {
                break;
            }
        }
        if (j < 4) {
            continue;
        }

        if (a == 'O') {
            goto o_won;
        } else {
            goto x_won;
        }
    }

    a = data[0][0];
    if (a == '.') {
        goto next1;
    } else if (a == 'T') {
        a = data[1][1];
        if (a == '.') {
            goto next1;
        }
    }
    for (i = 0; i < 4; i++) {
        if (!check(a, data[i][i])) {
            break;
        }
    }
    if (i >= 4) {
        if (a == 'O') {
            goto o_won;
        } else {
            goto x_won;
        }
    }
next1:

    a = data[0][3];
    if (a == '.') {
        goto next2;
    } else if (a == 'T') {
        a = data[1][2];
        if (a == '.') {
            goto next2;
        }
    }
    for (i = 0, j = 3; i < 4; i++, j--) {
        if (!check(a, data[i][j])) {
            break;
        }
    }
    if (i >= 4) {
        if (a == 'O') {
            goto o_won;
        } else {
            goto x_won;
        }
    }
next2:

    if (check2(data)) {
        return ("Draw");
    }
    return ("Game has not completed");

o_won:
    return ("O won");
x_won:
    return ("X won");
}

void exec(u_longlong num)
{
    const char *ans;
    char data[4][4];
    u_longlong i;

    for (i = 0; i < 4; i++) {
        cin >> data[i][0] >> data[i][1] >> data[i][2] >> data[i][3];
    }

#ifdef DEBUG
    for (i = 0; i < 4; i++) {
        cout << data[i][0] << data[i][1] << data[i][2] << data[i][3] << endl;
    }
#endif /* DEBUG */

    ans = calc(data);

    cout << "Case #" << num << ": ";
    cout << ans;
    cout << endl;

    return;
}

int main(int argc, char **argv)
{
    u_longlong t, i;

    cin >> t;
#ifdef DEBUG
    cout << "a_small start" << endl;
#endif /* DEBUG */
    for (i = 0; i < t; i++) {
        exec(i + 1);
    }

    return (0);
}
