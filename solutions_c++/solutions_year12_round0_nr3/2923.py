#include <iostream>

using namespace std;

const int MAXN = 2000000;

bool vis[MAXN+10];
int sta[11];

int recycle(int n, const int A, const int B, int MOD) {
    int cnt = 0;
    int mod = 10;
    
    while (mod <= n) {
        int m = n / mod + n % mod * MOD / mod;
        if (!vis[m] && m > n && m <= B) {
            vis[m] = true;
            sta[cnt++] = m;
        }
        mod *= 10;
    }
    for (int i = 0; i < cnt; i++) vis[ sta[i] ] = false;
    return cnt;
}

int recycleCnt(const int A, const int B) {
    int result = 0;
    int MOD = 1;
    while (MOD <= A) {
        MOD *= 10;
    }
    for (int a = A; a < B; a++) {
        result += recycle(a, A, B, MOD);
    }
    return result;
}

int main()
{
    FILE *fin, *fout;
    fin = fopen("D:\\TopCoder\\gcj2012\\QR\\C-small-attempt0.in", "r");
    fout = fopen("D:\\TopCoder\\gcj2012\\QR\\C.out", "w");
    
    int T;
    fscanf(fin, "%d", &T);
    for (int ca = 1; ca <= T; ca++) {
        int A, B;
        fscanf(fin, "%d %d", &A, &B);
        fprintf(fout, "Case #%d: %d\n", ca, recycleCnt(A, B));
    }
    
    fclose(fin);
    fclose(fout);
    return 0;
}

