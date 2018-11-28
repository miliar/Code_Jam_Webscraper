#include <iostream>
#include <cstdio>

using namespace std;


int T, N;
long double WP[100];
long double OWP[100];
long double OOWP[100];

char results[100][100];


struct s_totaux
{
    int nbWin;
    int nbLost;
};


s_totaux fillNbs(int lin)
{
    s_totaux ret = {0, 0};

    for (int col = 0; col < N; col++)
    {
        if (results[lin][col] == '1')
            ret.nbWin++;
        else if (results[lin][col] == '0')
            ret.nbLost++;
    }

    return ret;
}

int main()
{

    freopen("large.in", "r", stdin);
    freopen("large.out", "w", stdout);
    long double OWPTmp;

    scanf("%d", &T);


    s_totaux totaux;

    for (int test = 1; test <= T; test++)
    {
        scanf("%d", &N);

        for (int lin = 0; lin < N; lin++)
        {
            getchar();

            for (int col = 0; col < N; col++)
                scanf("%c", &results[lin][col]);
        }



        for (int team = 0; team < N; team++)
        {
            totaux = fillNbs(team);
            WP[team] = ((long double)totaux.nbWin)/((long double)(totaux.nbWin + totaux.nbLost));
            OWPTmp = 0;
            int cpt = 0;

            for (int opo = 0; opo < N; opo++)
            {
                if (results[team][opo] == '.')
                    continue;

                cpt++;

                totaux = fillNbs(opo);

                if (results[team][opo] == '1')
                    totaux.nbLost--;

                else if (results[team][opo] == '0')
                    totaux.nbWin--;

                OWPTmp += ((long double)totaux.nbWin)/((long double) totaux.nbLost+totaux.nbWin);
            }

            OWP[team] = OWPTmp/((long double) (cpt));
        }


        for (int team = 0; team < N; team++)
        {
            OOWP[team] = 0;
            int cpt = 0;
            for (int opo = 0; opo < N; opo++)
            {
                if (results[team][opo] != '.')
                {
                    OOWP[team] += OWP[opo];
                    cpt++;
                }
            }
            OOWP[team] /= ((long double)(cpt));
        }



        printf("Case #%d:\n", test);
        for (int team = 0; team < N; team++)
            printf("%lf\n", (double)(0.25*(WP[team]+OOWP[team]) + 0.5*OWP[team]));




    }

    return 0;
}
