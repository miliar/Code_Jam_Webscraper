#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int r, c;
int d;
char w[500][500];
int cum[501][501];
int cumcol[501][501];
int cumrow[501][501];

int getCums() {
    int i, j;
    for (i = 1; i <= r; i++)
        for (j = 1; j <= c; j++)
            cum[i][j] = cum[i-1][j] + cum[i][j-1] - cum[i-1][j-1] + w[i-1][j-1];
    for (i = 1; i <= r; i++)
        for (j = 1; j <= c; j++)
            cumcol[i][j] = cumcol[i-1][j] + cumcol[i][j-1] - cumcol[i-1][j-1] + j*w[i-1][j-1];
    for (i = 1; i <= r; i++)
        for (j = 1; j <= c; j++)
            cumrow[i][j] = cumrow[i-1][j] + cumrow[i][j-1] - cumrow[i-1][j-1] + i*w[i-1][j-1];
}

int rowCumBox(int size, int row, int col) {
    int ans = cumrow[row+size][col+size] - cumrow[row][col+size] - cumrow[row+size][col] + cumrow[row][col];
    ans-=w[row][col]*(row+1);
    ans-=w[row+size-1][col]*(row+size);
    ans-=w[row][col+size-1]*(row+1);
    ans-=w[row+size-1][col+size-1]*(row+size);
    return ans;
}

int colCumBox(int size, int row, int col) {
    int ans = cumcol[row+size][col+size] - cumcol[row][col+size] - cumcol[row+size][col] + cumcol[row][col];
    ans-=w[row][col]*(col+1);
    ans-=w[row+size-1][col]*(col+1);
    ans-=w[row][col+size-1]*(col+size);
    ans-=w[row+size-1][col+size-1]*(col+size);
    return ans;
}

int cumBox(int size, int row, int col) {
    int ans = cum[row+size][col+size] - cum[row][col+size] - cum[row+size][col] + cum[row][col];
    ans-=w[row][col];
    ans-=w[row+size-1][col];
    ans-=w[row][col+size-1];
    ans-=w[row+size-1][col+size-1];
    return ans;

}

bool rowCentred(int size, int row, int col) {
    int totalweighted = rowCumBox(size, row, col);
    int totalunweighted = cumBox(size, row, col);
    return totalweighted*2 - totalunweighted*(2*row+(size+1)) == 0;
}

bool colCentred(int size, int row, int col) {
    int totalweighted = colCumBox(size, row, col);
    int totalunweighted = cumBox(size, row, col);
    return totalweighted*2 - totalunweighted*(2*col+(size+1)) == 0;
}

bool isCentred(int size, int row, int col) {
    return rowCentred(size, row, col) && colCentred(size, row, col);    
}

bool canBeDone(int k) {
    int i, j;
    for (i = 0; i <= r-k; i++)
        for (j = 0; j <= c-k; j++)
            if (isCentred(k, i, j))
                return true;
    return false;
}
    

int main() {
    int T, TT;
    scanf("%d", &TT);
    for (T = 1; T <= TT; T++) {
        scanf("%d %d %d\n", &r, &c, &d);
        int best = 0;
        int i, j;
        char temp[600];
        for (i = 0; i < r; i++) {
            scanf("%s", temp);
            for (j = 0; j < c; j++) {
                w[i][j] = temp[j] - '0';
            }
        }
        
        getCums();
        
        for (i = 3; i <= min(r, c); i++)
            if (canBeDone(i))
                best = i;
        
        
        printf("Case #%d: ", T);
        if (!best)
            printf("IMPOSSIBLE\n");
        else
            printf("%d\n", best);
    }
}
