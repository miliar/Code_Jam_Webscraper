#include <cstdio>
#include <string>
#include <map>

using namespace std;

int N, Q;
string Tmp;
char Buf[200];
map <string, int> ID;
int Query;
int DP[200][2000];

int main()
{
    int Cases;
    scanf("%d", &Cases);
    for (int Case = 1; Case <= Cases; Case ++)
    {
        scanf("%d", &N);
        fgets(Buf, 200, stdin);
        ID.clear();

        for (int i = 0; i < N; i ++)
        {
            fgets(Buf, 200, stdin);
            Tmp = Buf;
            ID[Tmp] = i;
        }
        
        memset(DP, 1, sizeof(DP));
        for (int i = 0; i < N; i ++)
            DP[i][0] = 0;
            
        scanf("%d", &Q);
        fgets(Buf, 200, stdin);
        for (int i = 0; i < Q; i ++)
        {
            fgets(Buf, 200, stdin);
            Tmp = Buf;
            Query = ID[Tmp];
            for (int j = 0; j < N; j ++)
                if (Query != j)
                {
                    DP[j][i + 1] <?= DP[Query][i] + 1;
                    DP[j][i + 1] <?= DP[j][i];
                }
        }
        
        int Ans = 1000000;
        for (int i = 0; i < N; i ++)
            Ans <?= DP[i][Q];
        printf("Case #%d: %d\n", Case, Ans);
    }
    return 0;
}
