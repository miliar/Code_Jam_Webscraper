#include <cstdio>

int probCount;
int n, a, b, c, d, x0, y0, m;
long long count [3][3];


int main() {
    scanf("%d", &probCount);
    for(int probIndex = 1; probIndex<=probCount; probIndex++) {
        scanf("%d%d%d%d%d%d%d%d", &n, &a, &b, &c, &d, &x0, &y0, &m);

        long long x = x0;
        long long y = y0;
        long long ans = 0;
        for(int i=0; i<3; i++) {
            for(int j=0; j<3; j++) {
                count [i][j] = 0;
            }
        }
        for(int i=0; i<n; i++) {
            count[x%3][y%3]++;
            x = (a*x+b)%m;
            y = (c*y+d)%m;
        }
        for(int i=0; i<3; i++) {
            for(int j=0; j<3; j++) {
                ans+= count[i][j]*(count[i][j]-1)*(count[i][j]-2)/6;
            }
            ans+= count[i][0]*count[i][1]*count[i][2];
            ans+= count[0][i]*count[1][i]*count[2][i];
        }
        ans+=count[0][0]*count[1][1]*count[2][2];
        ans+=count[0][0]*count[1][2]*count[2][1];
        ans+=count[0][1]*count[1][0]*count[2][2];
        ans+=count[0][1]*count[1][2]*count[2][0];
        ans+=count[0][2]*count[1][1]*count[2][0];
        ans+=count[0][2]*count[1][0]*count[2][1];

        printf("Case #%d: %I64d\n", probIndex, ans);
    }
    return 0;
}
