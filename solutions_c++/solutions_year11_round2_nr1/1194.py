#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
#define For(i,x) for (int i=0; i<(int)(x); i++)
#define mp make_pair

void calc(int n, vector<string>& tab) {
    vector<pair<int, int> > wps;
    vector<double> owps;
    vector<double> oowps;

    // wp
    For(i, n) {
        int win = 0, lose = 0;
        For(j, n) {
            if (tab[i][j] == '1')
                win++;
            else if (tab[i][j] == '0')
                lose++;
        }

        wps.push_back(mp(win, lose));
    }

    // owps
    For(i, n) {
        int cnt = 0;
        double sum = 0;
        For(j, n) {
            if (i == j) continue;
            if (tab[j][i] == '1') {
                int win = wps[j].first-1;
                int lose = wps[j].second;
                sum += 1.0*win/(win+lose);
                cnt++;
            }
            else if (tab[j][i] == '0') {
                int win = wps[j].first;
                int lose = wps[j].second-1;
                sum += 1.0*win/(win+lose);
                cnt++;
            }
        }
        owps.push_back(sum/cnt);
    }

    //For(i, n) { cout << owps[i] << endl; }

    // oowps
    For(i, n) {
        int cnt = 0;
        double sum = 0;
        For(j, n) {
            if (tab[i][j] != '.') {
                sum += owps[j];
                cnt++;
            }
        }
        oowps.push_back(sum/cnt);
    }

    For(i, n) {
        int win = wps[i].first;
        int lose = wps[i].second;
        double wp = 1.0*win/(win+lose);
        double rpi = 0.25 * wp + 0.50 * owps[i] + 0.25 * oowps[i];
        printf("%.10lf\n", rpi);
    }

}

int main() {
    int ncases;
    scanf("%d", &ncases);
    For(cc, ncases) {
        int n;
        scanf("%d", &n);

        vector<string> tab;
        char s[1000];
        For(i, n) {
            scanf("%s", s);
            tab.push_back(s);
        }

        printf("Case #%d:\n", cc+1);
        calc(n, tab);
    }
}



