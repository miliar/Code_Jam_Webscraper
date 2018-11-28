#include <iostream>
#include <vector>

using namespace std;


vector<string> games;
int wins[110];
int played[110];

double wp[110];
double owp[110];
double oowp[110];

int main() {
    int cases;
    cin >> cases;

    for(int c=0; c<cases; c++) {
        int N;
        cin >> N;
        games.resize(N);
        for(int i=0; i<N; i++) cin >> games[i];

        memset(played,0,sizeof(played));
        memset(wins,0,sizeof(wins));
        for(int i=0; i<N; i++) {
            for(int j=0; j<N; j++) {
                if (games[i][j] != '.') {
                    played[i]++;
                    if (games[i][j]=='1') wins[i]++;
                }
            }
            wp[i] = (1.0*wins[i]) / played[i];
        }

        for(int i=0; i<N; i++) {
            double owpsum=0, owpcount=0;
            for(int j=0; j<N; j++) {
                if (games[i][j] != '.') {
                    int corr = games[i][j]=='1' ? 0 : 1;
                    owpsum += (1.0*wins[j]-corr) / (played[j]-1);
                    owpcount++;
                }
            }
            //cout << "   TEAM " << (char)(i+'A') << " owpsum="<<owpsum << "  owpcount="<<owpcount<<endl;
            owp[i] = owpsum/owpcount;
        }

        for(int i=0; i<N; i++) {
            double oowpsum=0, oowpcount=0;
            for(int j=0; j<N; j++) {
                if (games[i][j] != '.') {
                    oowpsum+=owp[j];
                    oowpcount++;
                }
            }
            oowp[i] = oowpsum/oowpcount;
        }


        cout << "Case #" <<(c+1) << ":"<<endl;
        for(int i=0; i<N; i++) {
            double rip = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i];
            printf("%.12f", rip);
            cout<<endl;
            //cout << "  WP="<<wp[i] << "  OWP="<<owp[i]<< "  OOWP="<<oowp[i]<<endl;
        }
    }
}
