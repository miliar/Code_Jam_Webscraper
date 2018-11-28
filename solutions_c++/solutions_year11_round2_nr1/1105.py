/*
NAME: Saketh Are
PROG: RPI
LANG: C++
*/

#include<fstream>
#include<vector>
using namespace std;

ifstream fin("rpi.in");
ofstream fout("rpi.out");

int T, N; char c;
int ngames[105];
int nwins[105];
int grid[105][105];
vector<int> opp[105];
long double WP[105];
long double OWP[105];
long double OOWP[105];

int main()
{
    fin >> T;
    for(int q = 0; q<T; q++){
        fin >> N;
        for(int a=0; a<N; a++){
            ngames[a]=0;
            nwins[a]=0;
            WP[a]=0;
            opp[a].clear();
            for(int b=0; b<N; b++){
                fin >> c;
                grid[a][b]=c;
                if(c=='.') continue;
                opp[a].push_back(b);
                ngames[a]++;
                if(c=='1') nwins[a]++;
                WP[a]=((long double)nwins[a])/ngames[a];
            }
        }
        for(int a=0; a<N; a++){
            OWP[a]=0;
            for(int b=0; b<opp[a].size(); b++){
               OWP[a]+=((long double)(nwins[opp[a][b]]-(grid[a][opp[a][b]]=='0')))
                   /(ngames[opp[a][b]]-1);
            }
            OWP[a]/=opp[a].size();
        }
        for(int a=0; a<N; a++){
            OOWP[a]=0;
            for(int b=0; b<opp[a].size(); b++)
               OOWP[a]+=OWP[opp[a][b]];
            OOWP[a]/=opp[a].size();
        }
        fout << "Case #" << q+1 << ":" << endl;
        fout.precision(20);
        for(int c=0; c<N; c++)
            fout << 0.25*WP[c] + 0.50*OWP[c] + 0.25*OOWP[c] << endl;
    }
    return 0;
}
