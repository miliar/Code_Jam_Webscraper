#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

class teamstat {
    public:
    int matches,wins;
    double WP, OWP, OOWP;
};

int main()
{
    int T;
    cin >> T;
    for (int q=1; q<=T; q++) {
        int N;
        cin >> N;
        string table[105];
        for (int i=0; i<N; i++) {
            cin >> table[i];
        }

        printf("Case #%d:\n",q);

        teamstat stats[105];
        for (int i=0; i<N; i++) {
            stats[i].matches=stats[i].wins=stats[i].WP=stats[i].OWP=stats[i].OOWP=0;
            for (int j=0; j<N; j++) {
                if (table[i][j]!='.') {
                    stats[i].matches++;
                }
                if (table[i][j]=='1') {
                    stats[i].wins++;
                }
            }
            stats[i].WP=(double)stats[i].wins/stats[i].matches;
            //cout << stats[i].WP << endl;
        }

        for (int i=0; i<N; i++) {
            double sum=0; int opp=0;
            for (int j=0; j<N; j++) {
                if (table[i][j]!='.') {
                    //Are all opponents?
                    opp++;
                    int dw=0,dm=0;
                    if (table[j][i]=='1') {
                        dm=1;
                        dw=1;
                    }
                    if (table[j][i]=='0') {
                        dm=1;
                    }
                    sum+=(double) (stats[j].wins-dw)/(stats[j].matches-dm);
                }
            }
            stats[i].OWP=sum/opp;
            //cout << stats[i].OWP << endl;
         }

         for (int i=0; i<N; i++) {
             //Are all opponents<
             int opp=0;
             double sum=0;
             for (int j=0; j<N; j++) {
                 if (table[i][j]!='.') {
                     opp++;
                     sum+=stats[j].OWP;
                 }
             }
             stats[i].OOWP=sum/(opp);
             printf("%.9f\n", 0.25 * stats[i].WP + 0.50 * stats[i].OWP + 0.25 * stats[i].OOWP);

         }


    }
    return 0;
}
