#include<cstdio>
#include<cstring>

int chk(int N, int A, int B)
{
    if( N < 10 ) return 0;
    if( N < 100 ) {
        int tmp = (N % 10) * 10 + N / 10;
        if( tmp > N && tmp <= B ) return 1;
        return 0;
    }
    if( N < 1000 ) {
        int tmp = (N % 10) * 100 + N / 10;
        int ret = 0;
        if( tmp > N && tmp <= B ) ++ret;
        tmp = (N % 100) * 10 + N / 100;
        if( tmp > N && tmp <= B ) ++ret;
        return ret;
    }
    return 0;
}

int main()
{
    //freopen("data.in", "r", stdin);
    //freopen("data.out", "w", stdout);
    int nt, idx = 0;
    scanf("%d", &nt);
    while( (nt --) > 0 ) {
        int A, B; scanf("%d %d", &A, &B);
        int ans = 0;
        for(int i = A; i <= B; i++)
            ans += chk(i, A, B);
        printf("Case #%d: %d\n", ++idx, ans);
    }
    return 0;
}
