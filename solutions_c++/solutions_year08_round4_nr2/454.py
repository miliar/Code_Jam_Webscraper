#include <cstdio>
#include <string>
using namespace std;

int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out.txt", "w", stdout);
    int kase, right, myCheck;
    int N, M, a, t = 1, ks;
    int x1, y1, x2, y2, x3, y3;
    scanf("%d", &kase);
    for(ks = 1; ks <= kase; ks++){
        right = 0;
        scanf("%d%d%d", &N, &M, &a);
        printf("Case #%d: ", ks);
        if(a > N * M)
        {
            printf("IMPOSSIBLE\n");
            continue;
        }
        for(x1 = 0;x1 <= N;x1++)
            for(y1 = 0;y1 <= M;y1++)
                for(x2 = 0;x2 <= N;x2++)
                    for(y2 = 0;y2 <= M;y2++)
                        for(x3 = 0;x3 <= N;x3++)
                            for(y3 = 0;y3 <= M;y3++)
                            {
                                myCheck = (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1);
                                if(myCheck == a || myCheck == -a)
                                {
                                    right = 1;
                                    goto PROCESS;
                                }
                            }
        PROCESS :
        if(right) printf("%d %d %d %d %d %d\n", x1, y1, x2, y2, x3, y3);
        else printf("IMPOSSIBLE\n");
    }
    //system("pause");
    return 0;   
}
