#include <cstdio>

#include <vector>
using namespace std;

typedef vector<int> TIntVector;
typedef vector<TIntVector> TIntVectorVector;

int Move(int x, int y, const TIntVectorVector& att, TIntVectorVector* letters, int* max) {
    if ((*letters)[x][y] == -1) {
        const int dirs[] = {-1, 0, 0, -1, 0, 1, 1, 0};
        int min = att[x][y];
        int minIndex = -1;
        for (size_t i = 0; i < 4; ++i) {
            int xx = x + dirs[2*i];
            if (xx >= 0 && xx < att.size()) {
                int yy = y + dirs[2*i + 1];
                if (yy >= 0 && yy < att[xx].size())
                    if (att[xx][yy] < min) {
                        min = att[xx][yy];
                        minIndex = i;
                    }
            }
        }
        if (min < att[x][y]) {
            int xx = x + dirs[2*minIndex];
            int yy = y + dirs[2*minIndex + 1];
            (*letters)[x][y] = Move(xx, yy, att, letters, max);
        } else {
            (*letters)[x][y] = *max;
            ++(*max);
        }
    }
    return (*letters)[x][y];
}

int main() {
    // freopen("input.txt", "r", stdin);
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    int n;
    scanf("%d", &n);
    for (int nT = 0; nT < n; ++nT) {
        int h, w;
        scanf("%d%d", &h, &w);
        TIntVectorVector att;
        for (int i = 0; i < h; ++i) {
            TIntVector row;
            for (int j = 0; j < w; ++j) {
                int dummy;
                scanf("%d", &dummy);
                row.push_back(dummy);
            }
            att.push_back(row);
        }
        TIntVector letterRow(w, -1);
        TIntVectorVector letters(h, letterRow);
        
        int max = 0;
        printf("Case #%d:\n", nT + 1);
        for (size_t i = 0; i < h; ++i) {
            for (size_t j = 0; j < w; ++j) {
                printf("%c ", 'a' + Move(i, j, att, &letters, &max));
            }
            printf("\n");
        }
    }
    
    return 0;
}
