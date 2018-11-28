#include <cstdio>
#include <cstdlib>

#include <iostream>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <sstream>
#include <vector>

using namespace std;

int N; 
long long A, B, C, D, X0, Y0, M;
long long Count[3][3];

void read_one()
{
    cin >> N >> A >> B >> C >> D >> X0 >> Y0 >> M;
}

void solve_one()
{
    int i, j, k;
    long long sol = 0, cur;
    memset (Count, 0, sizeof(Count));

    long long X = X0, Y = Y0;

    for (; N--;) {
        Count[X % 3][Y % 3] ++;
        // cerr << X << " " << Y << endl;
        X = (A*X + B) % M;
        Y = (C*Y + D) % M;
    }

    for (i = 0 ; i < 9; i++)
    for (j = i ; j < 9; j++)
    for (k = j ; k < 9; k++) {
       if ((i % 3 + j % 3 + k % 3) % 3)
            continue;
       if ((i / 3 + j / 3 + k / 3) % 3)
            continue;

       cur  = Count[i / 3][i % 3] --;
       cur *= Count[j / 3][j % 3] --;
       cur *= Count[k / 3][k % 3] --;
       if (i == j && j == k) {
           cur /= 6;
       } else if (i == j || j == k || k == i) {
           cur /= 2;
       }
       sol += cur;
       Count[i / 3][i % 3] ++;
       Count[j / 3][j % 3] ++;
       Count[k / 3][k % 3] ++;
    }

    cout << sol;
}

int main(void)
{
    int T, i;

    for(scanf("%d\n", &T), i = 1; i <= T; i++) {
        read_one();
        printf ("Case #%d: ", i);
        solve_one();
        printf ("\n");
    }
}

