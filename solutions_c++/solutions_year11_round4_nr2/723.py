#include <algorithm>
#include <cassert>
#include <cstring>
#include <iostream>
using namespace std;

const int MAX_RC = 500;

int rows, cols, dens;
char matrix[MAX_RC][MAX_RC];
int strip[MAX_RC];
int block[MAX_RC];
bool dead[MAX_RC][MAX_RC];

void vblocks(int r, int k)
{
    const int bs = k / 2;
    block[0] = 0;
    for(int c = 0; c < bs; c++)
        block[0] += strip[c];
    // cout << "r=" << r << ": block[0] = " << block[0] << endl;

    for(int c = 1; c <= cols - bs; c++) {
        block[c] = block[c - 1] - strip[c - 1] + strip[c + bs - 1];
        // cout << "r=" << r << ": block[" << c << "] = " << block[c] << endl;
        int beg = c + bs - k;
        int end = c + bs - 1;
        if(beg >= 0) {
            int b1 = block[beg] - matrix[r][beg] - matrix[r + k - 1][beg];
            int b2 = block[c] - matrix[r][end] - matrix[r + k - 1][end];
            // cout << "b1=" << b1 << " b2=" << b2 << endl;
            if(b1 != b2)
                dead[r][beg] = true;
        }
    }
    // cout << endl;
}

void hblocks(int c, int k)
{
    const int bs = k / 2;
    block[0] = 0;
    for(int r = 0; r < bs; r++)
        block[0] += strip[r];
    // cout << "c=" << c << ": block[0] = " << block[0] << endl;

    for(int r = 1; r <= rows - bs; r++) {
        block[r] = block[r - 1] - strip[r - 1] + strip[r + bs - 1];
        // cout << "c=" << c << ": block[" << r << "] = " << block[r] << endl;
        int beg = r + bs - k;
        int end = r + bs - 1;
        if(beg >= 0) {
            int b1 = block[beg] - matrix[beg][c] - matrix[beg][c + k - 1];
            int b2 = block[r] - matrix[end][c] - matrix[end][c + k - 1];
            // cout << "b1=" << b1 << " b2=" << b2 << endl;
            if(b1 != b2)
                dead[beg][c] = true;
        }
    }
    // cout << endl;
}

bool find(const int k)
{
    memset(dead, 0, sizeof(dead));

    // Vertical strips.
    for(int c = 0; c < cols; c++) {
        strip[c] = 0;
        for(int r = 0; r < k; r++)
            strip[c] += matrix[r][c];
        // cout << "r=0: strip[" << c << "] = " << strip[c] << endl;
    }
    vblocks(0, k);
    for(int r = 1; r <= rows - k; r++) {
        for(int c = 0; c < cols; c++) {
            strip[c] += matrix[r + k - 1][c] - matrix[r - 1][c];
            // cout << "r=" << r << " strip[" << c << "] = " << strip[c] << endl;
        }
        vblocks(r, k);
    }

    // Horizontal strips.
    for(int r = 0; r < rows; r++) {
        strip[r] = 0;
        for(int c = 0; c < k; c++)
            strip[r] += matrix[r][c];
        // cout << "c=0: strip[" << r << "] = " << strip[r] << endl;
    }
    hblocks(0, k);
    for(int c = 1; c <= cols - k; c++) {
        for(int r = 0; r < rows; r++) {
            strip[r] += matrix[r][c + k - 1] - matrix[r][c - 1];
            // cout << "c=" << c << " strip[" << r << "] = " << strip[r] << endl;
        }
        hblocks(c, k);
    }

    for(int r = 0; r <= rows - k; r++) {
        for(int c = 0; c <= cols - k; c++) {
            if(!dead[r][c]) {
                // cout << "Found !dead[" << r << "][" << c << "] !!!" << endl;
                return true;
            }
        }
    }
    return false;
}

int solve()
{
    for(int k = min(rows, cols); k >= 3; k--) {
        if(find(k))
            return k;
    }
    return -1; // impossible
}

int main()
{
    int tests;
    cin >> tests;
    for(int t = 0; t < tests; t++) {
        cin >> rows >> cols >> dens;
        for(int r = 0; r < rows; r++) {
            cin >> matrix[r];
            assert(strlen(matrix[r]) == (uint)cols);
            for(int c = 0; c < cols; c++)
                matrix[r][c] -= '0';
        }
        int ans = solve();
        cout << "Case #" << t + 1 << ": ";
        if(ans == -1)
            cout << "IMPOSSIBLE";
        else
            cout << ans;
        cout << endl;
    }
    return 0;
}
