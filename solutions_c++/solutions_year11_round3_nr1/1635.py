#include <iostream>

using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int q=1; q<=T; q++) {
        char a[60][60]={0};
        int R,C;
        cin >> R >> C;
        for (int i=1; i<=R; i++) {
            for (int j=1; j<=C; j++) {
                cin >> a[i][j];
            }
        }

        int imp=0;
        for (int i=1; i<=R; i++) {
            for (int j=1; j<=C; j++) {
                if (a[i][j]=='#') {
                    a[i][j]='/';
                    if (a[i][j+1]!='#' || a[i+1][j]!='#' || a[i+1][j+1]!='#') imp=1;
                    a[i][j+1]='\\';
                    a[i+1][j]='\\';
                    a[i+1][j+1]='/';
                }
            }
        }
        cout << "Case #" << q <<":" << endl;
        if (imp) cout << "Impossible" << endl;
        else {
            for (int i=1; i<=R; i++) {
                for (int j=1; j<=C; j++) {
                    cout << a[i][j];
                }
                cout << endl;
            }
        }
    }
    return 0;
}
