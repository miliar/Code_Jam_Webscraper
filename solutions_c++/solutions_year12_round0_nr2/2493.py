#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <algorithm>

using namespace std;

#define MAX 105

int table[MAX][MAX];

int isgood(int total, bool surprising, int p) {
    for (int i=0; i <= 10; ++i) {
        for (int j=i; j <= i + 1 + surprising; ++j) {
            for (int k=j; k <= i + 1 + surprising; ++k) {
                if (i + j + k == total && k >= p) {
                    return 1;
                }
            }
        }
    }
    return 0;
}

int main() {
    int t, T = 1;
    
    scanf("%d ", &t);
    while (t--) {
        printf("Case #%d: ", T++);
        
        int n, surprises, p;
        
        scanf("%d %d %d", &n, &surprises, &p);
        
        vector <int> scores(n);
        
        for (int i=0; i < n; ++i) {
            scanf("%d", &scores[i]);
        }
        
        memset(table, 0, sizeof(table)); // index, number of surprises
        
        table[0][0] = isgood(scores[0], false, p);
        if (surprises > 0) table[0][1] = isgood(scores[0], true, p);
        
        for (int i=1; i < n; ++i) {
            for (int k=0; k <= surprises; ++k) {
                int A = table[i-1][k] + isgood(scores[i], false, p);
                int B = (k > 0) ? table[i-1][k-1] + isgood(scores[i], true, p) : 0;
                table[i][k] = max(A, B);
            }
        }
        
        printf("%d\n", table[n-1][surprises]);
    }
    
    return 0;
}
