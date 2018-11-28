#include <stdio.h>
#include <memory.h>

int A=0;
int B=1;

int N;
int T;
int NA,NB;
int minute[1440][2];
int H1,M1,H2,M2;

int main()
{
    int i,j;

    FILE* fp1=freopen("B-small-attempt1.in", "r", stdin);
    FILE* fp2=freopen("out.txt", "w", stdout);

    scanf("%d", &N);
    for(i=1; i<=N; i++)
    {
        memset(minute, 0, sizeof(minute));

        scanf("%d", &T);
        scanf("%d %d", &NA, &NB);

        for(j=0; j<NA; j++)
        {
            scanf("%d:%d %d:%d", &H1, &M1, &H2, &M2);
            minute[H1*60+M1][A] -= 1;
            minute[H2*60+M2+T][B] += 1;
        }
        for(j=0; j<NB; j++)
        {
            scanf("%d:%d %d:%d", &H1, &M1, &H2, &M2);
            minute[H1*60+M1][B] -= 1;
            minute[H2*60+M2+T][A] += 1;
        }

        int TA,TB;
        int CA,CB;
        TA=0; TB=0;
        CA=0; CB=0;
        for(j=0; j<1440; j++)
        {
            TA += minute[j][A];
            TB += minute[j][B];
            if(TA<0) 
            {
                CA-=TA;
                TA=0;
            }
            if(TB<0)
            {
                CB-=TB;
                TB=0;
            }
        }

        printf("Case #%d: %d %d\n", i, CA, CB);
    }

    fclose(fp1);
    fclose(fp2);

    return 0;
}