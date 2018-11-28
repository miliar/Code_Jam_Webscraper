/* Google Code Jam Qualifying Round - Speaking in Tongues */

#include <iostream>
#include <cstdio>

#define MAXG 200

using namespace std;

char mapping[] = {
        'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b',
        'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q' 
};

int main() {
        int T; cin >> T; scanf("\n");
        for (int cT = 1; cT <= T; cT++) {
                char G[MAXG]; fgets(G, MAXG, stdin);
                char S[MAXG] = {0};
                int i = 0;
                do {
                        S[i] = G[i] == ' ' ? ' ' : mapping[G[i] - 'a'];
                        i++;
                } while (G[i] != '\n' && G[i] != '\0');
                printf("Case #%d: %s\n", cT, S);
        }
}
