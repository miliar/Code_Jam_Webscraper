#include <iostream>
#include <string>

#define MAXLEN 25

using namespace std;

void theNext(long long n) {
    long long rest;
    int digs[MAXLEN];
    int len;
    int i, j;
    int tmp, num;
    int si;
    int zs;

    digs[0] = n % 10;
    n /= 10;

    len = 1;

    while(n > 0) {
        tmp = n % 10;
        n /=10;
        if(tmp < digs[len-1]) {
            j = len - 1;
            while(j >= 0) {
                if(digs[j] <= tmp) break;
                j--;
            }
            j++;
            //cout << "fd";
            if(n > 0) cout << n;
            cout << digs[j];
            digs[j] = tmp;
            for(num = 0; num <= 9; num++) {
                for(i = len-1; i >= 0; i--) {
                    if(digs[i] == num) cout << digs[i];
                }
            }
            return;

        }
        digs[len] = tmp;
        len++;
    }

    zs = 1;

    i = 0;

    while(digs[i] == 0) {
        zs++;
        i++;
    }

    cout << digs[i];
    for(j = 0; j < zs; j++) {
        cout << 0;
    }

    for(j = i + 1; j < len; j++) {
        cout << digs[j];
    }
}

int main()
{
    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);

    int t, b, tn;
    int i;
    char ch;
    long long n;
    long long k;

    cin >> t;

    for(tn = 1; tn <= t; tn++) {
        cin >> n;
        cout << "Case #" << tn << ": ";
        theNext(n);
        cout << endl;
    }

    return 0;
}
