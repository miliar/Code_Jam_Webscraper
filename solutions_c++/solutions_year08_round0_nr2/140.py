#include <cstdio>
#include <algorithm>

using namespace std;

struct TEvent
{
    int Time, Flag;
};

bool operator < (const TEvent &A, const TEvent &B)
{
    return (A.Time < B.Time) || (A.Time == B.Time && A.Flag < B.Flag);
}

int GetTime()
{
    int H, M;
    char Ch;
    scanf("%d%c%d", &H, &Ch, &M);
    return H * 60 + M;
}

int Turn, nA, nB;
TEvent A[1000], B[1000];

int main()
{
    int Cases;
    scanf("%d", &Cases);
    for (int Case = 1; Case <= Cases; Case ++)
    {
        scanf("%d%d%d", &Turn, &nA, &nB);
        for (int i = 0; i < nA; i ++)
        {
            A[i].Time = GetTime();
            A[i].Flag = 1; // Out
            B[i].Time = GetTime() + Turn;
            B[i].Flag = 0; // In
        }
        for (int i = nA; i < nA + nB; i ++)
        {
            B[i].Time = GetTime();
            B[i].Flag = 1; // Out
            A[i].Time = GetTime() + Turn;
            A[i].Flag = 0; // In
        }
        sort(A, A + nA + nB);
        sort(B, B + nA + nB);
        int AnsA = 0, AnsB = 0, Train = 0;
        for (int i = 0; i < nA + nB; i ++)
        {
            if (A[i].Flag == 0)
                Train ++;
            else
                if (Train > 0)
                    Train --;
                else
                    AnsA ++;
        }
        Train = 0;
        for (int i = 0; i < nA + nB; i ++)
        {
            if (B[i].Flag == 0)
                Train ++;
            else
                if (Train > 0)
                    Train --;
                else
                    AnsB ++;
        }
        printf("Case #%d: %d %d\n", Case, AnsA, AnsB);
    }
    return 0;
}
