#include <cstdio>
#include <cstring>

using namespace std;

const int maxN = 128;

int N, L, H;
int fre[maxN];

int main()
{
    //freopen("C.in", "r", stdin);
    //freopen("C.out", "w", stdout);

    int cas;

    scanf("%d", &cas);
    for(int cc = 0; cc < cas; cc++)
    {
        scanf("%d %d %d", &N, &L, &H);
        for(int i = 0; i < N; i++)
            scanf("%d", &fre[i]);

        printf("Case #%d: ", cc + 1);

        bool find = false;
        for(int i = L; i <= H && !find; i++)
        {
            bool ok = true;
            for(int j = 0; j < N && ok; j++)
                if(i % fre[j] != 0 && fre[j] % i != 0)
                    ok = false;

            if(ok)
            {
                printf("%d\n", i);
                find = true;
            }
        }

        if(!find) printf("NO\n");
    }
    return 0;
}
