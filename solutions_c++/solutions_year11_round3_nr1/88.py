#include <iostream>
#include <string>

using namespace std;

string d[100];
int main() {
    int T;
    cin>>T;
    int dx[] = {0, 1, 0, 1};
    int dy[] = {0, 0, 1, 1};
    string rep = "/\\\\/";
    for (int t=1;t<=T;t++) {
        int R, C;
        cin>>R>>C;
        for (int i=0;i<R;i++) {
            cin>>d[i];
        }
        bool good = true;
        for (int r=0;r<R;r++) for (int c=0;c<C;c++) {
            if (d[r][c] == '#') {
                for (int i=0;i<4;i++) {
                    int nc = c + dx[i];
                    int nr = r + dy[i];
                    if (nc >= C || nr >= R) {
                        good = false;
                        break;
                    }
                    if (d[nr][nc] != '#') good = false;
                    d[nr][nc] = rep[i];
                }
            }
        }
        cout << "Case #" << t << ":" << endl;
        if (good) {
            for (int i=0;i<R;i++) cout << d[i] << endl;
        } else {
            cout << "Impossible" << endl;
        }
    }
}
