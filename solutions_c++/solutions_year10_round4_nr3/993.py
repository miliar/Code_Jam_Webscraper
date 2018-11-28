#include <iostream>
#include <vector>
#include <string>
#include <utility>
using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;

void print(VVI cell)
{
    for(int i=0;i<8;i++) {
        for(int j=0;j<8;j++) {
            cout << cell[i][j];
        }
        cout << endl;
    }
    cout << endl;
}

int main()
{
    int t;
    cin >> t;
    for(int cnt=1;cnt<=t;cnt++) {
        int r;
        cin >> r;
        VVI cell(102, VI(102, 0));
        VVI all0(102, VI(102, 0));
        for(int i=0;i<r;i++) {
            int x1, y1, x2, y2;
            cin >> x1 >> y1 >> x2 >>y2;
            for(int j=x1;j<=x2;j++) {
                for(int k=y1;k<=y2;k++) {
                    cell[k][j] = 1;
                }
            }
        }
        int ans = -1;
        for(int tt=1;;tt++) {
//            print(cell);
            VVI tmp = cell;
            for(int i=1;i<=100;i++) {
                for(int j=1;j<=100;j++) {
                    if(cell[i-1][j] == 0 && cell[i][j-1] == 0)
                        tmp[i][j] = 0;
                    if(cell[i-1][j] == 1 && cell[i][j-1] == 1)
                        tmp[i][j] = 1;
                }
            }
            cell = tmp;
            if(cell == all0) {
                ans = tt;
                break;
            }
        }
        cout << "Case #" << cnt << ": " << ans << endl;
    }
    
    return 0;
}
