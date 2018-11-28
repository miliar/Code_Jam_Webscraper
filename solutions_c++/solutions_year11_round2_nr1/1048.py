#include <iostream>
#include <fstream>
#include <cstdlib>

using namespace std;

ifstream in("in.txt");
FILE *out = fopen("out.txt","w");

typedef long long LL;
const int MAXN = 1000;
string grid[MAXN];
double WP[MAXN], OWP[MAXN], OOWP[MAXN];
double numG[MAXN];

int main() {
    int T;
    in >> T;
    for( int test=1; test<=T; test++ ) {
        int N;
        in >> N;
        for( int i=0; i<N; i++ ) in >> grid[i];
        for( int i=0; i<N; i++ ) {
            double G=0;
            WP[i] = 0.0;
            for( int j=0; j<N; j++ ) {
                if( grid[i][j] == '.' ) continue;
                G++;
                WP[i] += grid[i][j]-'0';
            }
            WP[i] /= G;
            numG[i] = G;
            //cout << WP[i] << ": WP" << endl;
        }
        for( int i=0; i<N; i++ ) {
            OWP[i] = 0.0;
            for( int j=0; j<N; j++ ) {
                //see if played against
                if( grid[i][j] == '.' ) continue;
                double p = 1.0 - (grid[i][j]-'0');
                OWP[i] += (WP[j]*numG[j] - p)/(numG[j]-1.0);
            }
            OWP[i] /= numG[i];
            //cout << OWP[i] << ": OWP" << endl;
        }

        for( int i=0; i<N; i++ ) {
            OOWP[i] = 0.0;
            for( int j=0; j<N; j++ ) {
                if( grid[i][j] == '.' ) continue;
                OOWP[i] += OWP[j];
            }
            OOWP[i] /= numG[i];
        }

        //out << "Case #" << test << ":" << endl;
        fprintf(out,"Case #%d:\n",test);
        for( int i=0; i<N; i++ )
            fprintf(out,"%.8lf\n", (0.25*WP[i] +0.5*OWP[i]+0.25*OOWP[i]));

    }

    return 0;
}



