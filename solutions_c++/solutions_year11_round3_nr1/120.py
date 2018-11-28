#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
    int t;
    cin >> t;
    for(int tc=1;tc<=t;tc++) {
        int r, c;
        cin >> r >> c;
        string tile[50];
        for(int i=0;i<r;i++) {
            cin >> tile[i];
        }

        for(int i=0;i<r-1;i++) {
            for(int j=0;j<c-1;j++) {
                if(tile[i][j] == '#' && tile[i+1][j] == '#' &&
                   tile[i][j+1] == '#' && tile[i+1][j+1] == '#') {
                    tile[i][j] = tile[i+1][j+1] = '/';
                    tile[i+1][j] = tile[i][j+1] = '\\';
                }
            }
        }

        bool ans = true;
        for(int i=0;i<r;i++) {
            for(int j=0;j<c;j++) {
                if(tile[i][j] == '#') {
                    ans = false;
                }
            }
        }

        cout << "Case #" << tc << ":" << endl;
        if(ans) {
            for(int i=0;i<r;i++) {
                cout << tile[i] << endl;
            }
        }
        else {
            cout << "Impossible" << endl;
        }
    }

    return 0;
}
