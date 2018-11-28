#include <iostream>
#include <cstring>
#include <cstdlib>
using namespace std;

int c[10];

void setup(int N) {
    while (N) {
        c[N % 10]++;
        N /= 10;
    }
}

bool check(int N) {
    int other[10];
    memset(other, 0, sizeof(other));
    while (N) {
        other[N % 10]++;
        N /= 10;
    }
    for (int i = 1; i < 10; i++)
        if (c[i] != other[i])
            return false;
    return true;
}

int main()
{
    int T;
    int N;
    cin >> T;
    for (int i = 0; i < T; i++) {
        cin >> N;
        memset(c, 0, sizeof(c));
        setup(N);
        for (int j = N+1; ; j++)
        {
            if (check(j)) {
                cout << "Case #" << i + 1 << ": " << j << endl;
                break;
            }
        }
    }
}
