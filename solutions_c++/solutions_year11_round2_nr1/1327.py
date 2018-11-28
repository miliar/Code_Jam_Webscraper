#include <stdio.h>
#include <string.h>
#include <map>

int N;

char arr[100][1000];
double WP[100];
double OWP[100];
double OOWP[100];
double RPI[100];

void func()
{
    scanf("%d", &N);
    //printf("N= %d\n", N);

    for (int i=0;i<N;i++) {
        scanf("%s", arr[i]);
    }

    for (int i=0;i<N;i++) {
        int games = 0;
        int wins=0;
        for (int j=0;j<N;j++) {
            char c = arr[i][j];
            if (c == '0')
                games++;
            else if (c == '1') {
                games++;
                wins++;
            }
        }
        WP[i] = (wins * 1.0f) / games;
    }

    for (int i=0;i<N;i++) {
        double WPS=0;
        int count=0;
        for (int j=0;j<N;j++) {
            int games=0;
            int wins=0;
            if (j==i)
                continue;
            if (arr[i][j] == '.')
                continue;
            for (int k=0;k<N;k++) {
                if (k==i)
                    continue;
                char c = arr[j][k];
                if (c == '0')
                    games++;
                else if (c == '1') {
                    games++;
                    wins++;
                }
            }
            WPS += (wins * 1.0f) / games;
            count++;
        }
        OWP[i] = WPS / count;
        //printf("OWP%d %lf\n", i, OWP[i]);
    }

    for (int i=0;i<N;i++) {
        double oowp=0;
        int count=0;
        for (int j=0;j<N;j++) {
            if (arr[i][j] != '.') {
                oowp += OWP[j];
                count++;
            }
        }
        OOWP[i] = oowp / count;
        RPI[i] = 0.25f * WP[i] + 0.50f * OWP[i] + 0.25f * OOWP[i];
        printf("%.9lf\n", RPI[i]);
    }
}

main()
{
    int T;
    scanf("%d", &T);
    for (int i=0;i<T;i++) {
        printf("Case #%d:\n", i+1);
        func();
    }
}
