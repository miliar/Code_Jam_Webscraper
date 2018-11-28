#include <cstdio>

using namespace std;

int main()
{
    int N, T, NA, NB, countA, countB, listosEnA[10000], listosEnB[10000], salenDeA[10000], salenDeB[10000];
    int hh1, mm1, hh2, mm2;
    FILE *in = fopen("entrada.txt", "r");
        fscanf(in, "%d\n", &N);
        for (int x = 0; x < N; x++)
        {
            countA = 0; countB = 0;
            for (int t = 0; t < 10000; t++){ listosEnA[t] = 0; listosEnB[t] = 0; salenDeA[t] = 0; salenDeB[t] = 0; }
            fscanf(in, "%d\n", &T);
            fscanf(in, "%d %d\n", &NA, &NB);
            for (int t = 0; t < NA; t++)
            {
                fscanf(in, "%d:%d %d:%d\n", &hh1, &mm1, &hh2, &mm2);
                salenDeA[60 * hh1 + mm1]++;
                listosEnB[60 * hh2 + mm2 + T]++;
            }
            for (int t = 0; t < NB; t++)
            {
                fscanf(in, "%d:%d %d:%d\n", &hh1, &mm1, &hh2, &mm2);
                salenDeB[60 * hh1 + mm1]++;
                listosEnA[60 * hh2 + mm2 + T]++;
            }

            int ta = 0;
            for (int t = 0; t < 60 * 24; t++)
            {
                ta += (listosEnA[t] - salenDeA[t]);
                if (ta < 0)
                {
                    countA += (-1 * ta);
                    ta = 0;
                }
            }

            int tb = 0;
            for (int t = 0; t < 60 * 24; t++)
            {
                tb += (listosEnB[t] - salenDeB[t]);
                if (tb < 0)
                {
                    countB += (-1 * tb);
                    tb = 0;
                }
            }
            
            printf("Case #%d: %d %d\n", (x+1), countA, countB);
        }
    fclose(in);
    return 0;
}
