#include <iostream>
#include <string>
#include <iomanip>

#define REP(i, a, b) for(i = a; i < b; i++)
#define rep(i, n) REP(i, 0, n)
#define REPD(i, a, b) for(i = a; i > b; i--)
#define repd(i, n) REPD(i, n, 0)
#define UTL(i, a, b) for(i = a; i <= b; i++)
#define utl(i, n) UTL(i, 1, n)
#define UTLD(i, a, b) for(i = a; i >= b; i--)
#define utld(i, n) UTLD(i, n, 1)

using namespace std;

int main()
{
    freopen("data.in", "r", stdin);
    freopen("data.out", "w", stdout);

    int n, in, len, i;
    int chi;
    int base;

    long long result;

    int num[40];

    char str[100];

    cin >> n;

    utl(in, n) {
        cin >> str;
        base = 0;
        rep(i, 40) {
            num[i] = -1;
        }
        len = strlen(str);
        rep(i, len) {
            if(str[i] >= '0' && str[i] <= '9') {
                chi = str[i] - '0';
            } else {
                chi = str[i] - 'a' + 10;
            }
            if(num[chi] < 0) {
                if(base == 0) {
                    num[chi] = 1;
                } else if(base == 1) {
                    num[chi] = 0;
                } else {
                    num[chi] = base;
                }
                base++;
            }
            //cout << base << endl;
        }
        if(base == 1) base++;
        result = 0;
        rep(i, len) {
            if(str[i] >= '0' && str[i] <= '9') {
                chi = str[i] - '0';
            } else {
                chi = str[i] - 'a' + 10;
            }
            result = result * base + num[chi];
        }
        cout << "Case #" << in << ": " << result << endl;
    }

    return 0;
}
