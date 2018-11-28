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

int d[128];
int K, N;

void read_one()
{
    int i;
    cin >> K >> N;
    for (i = 0; i < N; i++)
       cin >> d[i];
}

int deck[5002], newdeck[5002];

void solve_one()
{
    int deck_len = 0, i, j, k;
    // cerr << K << "," << N << " ";
    for (k = K - 1; k >= 0; k--) {
        deck_len ++;
        newdeck[k % deck_len] = k;
        j = 0;
        for (i = (k + 1) % deck_len; i != (k % deck_len); i = (i + 1) % deck_len)
            newdeck[i] = deck[j++];
        memcpy (deck, newdeck, sizeof(deck));
    }

    for (i = 0; i < N; i++)
        cout << " " << deck[d[i] - 1] + 1; 
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

