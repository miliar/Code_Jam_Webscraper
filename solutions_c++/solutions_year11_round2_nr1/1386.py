#include <iostream>
#include <vector>
#include <string>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

int getint() { int i; cin >> i; return i; }
string getline() { char line[1024];cin.getline(line,1024);return string(line); }

#define for_from_to(V,FROM,TO) for(int V=FROM;V<(TO);V++)
#define for_i_from0_to(X) for_from_to(i,0,X)

int encode(int i, int j) { return i* 1000 + j; }
#define ZERO(X) memset(X, 0, sizeof(X) )
char results[1000][1000];

bool won[1000][1000];
bool played[1000][1000];
int played_count[1000];
int won_count[1000];
double wp[1000];
double owp[1000];
double oowp[1000];

int main() {
    int T= getint();
    string result ="";

    for_from_to(testcase, 0, T) {
        int N = getint();getline();

        ZERO(results);
        ZERO(won);
        ZERO(played);
        ZERO(played_count);
        ZERO(won_count);
        ZERO(wp);
        ZERO(owp);
        ZERO(oowp);

        for_i_from0_to(N) {
            string line = getline();
            for_from_to(j,0,N) {
                switch(line[j]) {
                    case '.':
                        results[i][j]=0;
                        break;
                    case '1':
                        results[i][j]=1;
                        won[i][j] = true;
                        won_count[i]++;
                        played[i][j] = true;
                        played_count[i]++;
                        break;
                    case '0':
                        results[i][j]=-1;
                        won[i][j] = false;
                        played[i][j] = true;
                        played_count[i]++;
                        break;
                    default:
                        // i = 22 / (j-j);
                        break;
                }
            }
            // cout <<"["<< line <<"]"<< endl;
            wp[i] = won_count[i] *1.0/ played_count[i];
        }

        for_i_from0_to(N) {
            int count = 0;
            double wp = 0.0;

            for_from_to(j,0,N) {
                if (!played[i][j])
                    continue;

                int W = 0, P = 0;
                for_from_to(k,0,N) {
                    if (i==j)
                        continue;
                    if (i==k)
                        continue;
                    if (played[j][k]) {
                        P++;
                        if (won[j][k]) {
                            W++;
                        }
                    }
                }

                double t = W * 1.0 / P;

                wp += t;
                count++;
            }
            owp[i] = wp / count;
        }

        for_i_from0_to(N) {
            double t = 0.0;
            int count = 0;

            for_from_to(j,0,N) {
                if (played[i][j]) {
                    t+= owp[j];
                    count++;
                }
            }
            oowp[i] = t / count;
        }
            
        cout << "Case #" << testcase+1<<":" << result << endl;
        for_i_from0_to(N) {
            double rpi = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
            cout << rpi << endl;
        }

    }

}
