#include <cstdio>

FILE *in, *out;

int main(){
    in = fopen("A.in", "r");
    out = fopen("A.out", "w");
    int T;
    fscanf(in, "%d", &T);
    for(int t=0;t<T;t++){
        int n, A, B, C, D, x0, y0, M;
        fscanf(in, "%d %d %d %d %d %d %d %d", &n, &A, &B, &C, &D, &x0, &y0, &M);

        long long cnt[3][3];
        for(int i=0;i<3;i++)
            for(int j=0;j<3;j++)
                cnt[i][j]=0;

        int x=x0, y=y0;
        cnt[x%3][y%3]++;

        for(int i=0;i<n-1;i++){
            x = (A*x + B) % M;
            y = (C*y + D) % M;
            cnt[x%3][y%3]++;
        }

        long long result=0;

        result += cnt[0][0] * (cnt[0][0]-1) * (cnt[0][0]-2)/6;
        result += cnt[0][1] * (cnt[0][1]-1) * (cnt[0][1]-2)/6;
        result += cnt[0][2] * (cnt[0][2]-1) * (cnt[0][2]-2)/6;
        result += cnt[0][0] * cnt[0][1] * cnt[0][2];

        result += cnt[1][0] * (cnt[1][0]-1) * (cnt[1][0]-2)/6;
        result += cnt[1][1] * (cnt[1][1]-1) * (cnt[1][1]-2)/6;
        result += cnt[1][2] * (cnt[1][2]-1) * (cnt[1][2]-2)/6;
        result += cnt[1][0] * cnt[1][1] * cnt[1][2];

        result += cnt[2][0] * (cnt[2][0]-1) * (cnt[2][0]-2)/6;
        result += cnt[2][1] * (cnt[2][1]-1) * (cnt[2][1]-2)/6;
        result += cnt[2][2] * (cnt[2][2]-1) * (cnt[2][2]-2)/6;
        result += cnt[2][0] * cnt[2][1] * cnt[2][2];

        result += cnt[0][0] * cnt[1][0] * cnt[2][0];
        result += cnt[0][1] * cnt[1][1] * cnt[2][1];
        result += cnt[0][2] * cnt[1][2] * cnt[2][2];

        result += cnt[0][0] * cnt[1][1] * cnt[2][2];
        result += cnt[0][1] * cnt[1][0] * cnt[2][2];
        result += cnt[0][1] * cnt[1][2] * cnt[2][0];

        fprintf(out, "Case #%d: %lld\n", t+1, result);
    }
    fclose(in);
    fclose(out);
    return 0;
}