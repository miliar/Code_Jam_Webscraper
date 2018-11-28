
#include <iostream>
#include <string>

using namespace std;

int N;
string adj[100];
double ans[100];

double wp[100]; // throw out game
double owp[100];

void solve() {
    for(int i = 0; i < N; i++) {
        int won = 0;
        int total = 0;
        for(int j = 0; j < N; j++) {
            if(adj[i][j] == '1') won++;
            if(adj[i][j] != '.') total++;
        }
        ans[i] = 0.25 * won / total; // WP

        double sum = 0;
        int div = 0;
        for(int j = 0; j < N; j++) {
            if(adj[i][j] == '.') continue;
            won = 0;
            total = 0;
            for(int k = 0; k < N; k++) {
                if(k == i) continue;
                if(adj[j][k] == '1') won++;
                if(adj[j][k] != '.') total++;
            }
            sum += 1.0 * won / total;
            div++;
        }
        owp[i] = 1.0 * sum / div;

        ans[i] += 0.50 * owp[i]; // OWP
    }

    for(int i = 0; i < N; i++) {
        double sum = 0;
        int total = 0;
        for(int j = 0; j < N; j++) {
            if(adj[i][j] != '.') sum += owp[j], total++;
        }

        ans[i] += 0.25 * sum / total; // OOWP
    }
}

int main() {
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++) {
        cin >> N;
        for(int i = 0; i < N; i++)
            cin >> adj[i];

        solve();

        printf("Case #%d:\n", t);
        for(int i = 0; i < N; i++)
            printf("%.10lf\n", ans[i]);
    }
}
