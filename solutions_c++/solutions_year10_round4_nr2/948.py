#include <iostream>
#define MAX 1050
using namespace std;

int m[MAX],t,p;
int pre[MAX][MAX];

int isany(int left,int right) {
    for (int x=left;x<right;x++)
        if (m[x])
           return 1;
    return 0;
}

void decline(int left,int right) {
    for (int x=left;x<right;x++)
        if (m[x])
           m[x]--;
}


int main() {
    cin >> t;
    for (int i=1;i<=t;i++) {
        cin >> p;
        //cout << "!" << p << endl;
        for (int x=0;x<(1 << p);x++) {
            cin >> m[x];
            m[x] = p - m[x];
        }
            
        for (int x=0;x<p;x++) {
            //cout << "!!" << (1 << (p - x - 1)) << endl;
            for (int y=0;y<(1 << (p - x - 1));y++) {
                cin >> pre[x][y];
                //pre[x][y] = 1;
            }
        }

        int needed = 0;
        for (int x=p-1;x>=0;x--) {
            for (int y=0;y < (1 << (p - x - 1));y++) {
                //int ngames = (1 << (p - x - 1));
                int step = 1 << (x+1);
                //cout << ngames << " " << step << "  --> " << isany(y * step , (y+1) * step) << endl;
                //cout << y * step << "  to  " << (y+1) * step  << endl << endl;
                if (isany(y * step , (y+1) * step))
                   needed++ , decline( y * step , (y+1) * step );
            }
        }

        cout << "Case #" << i << ": " << needed << endl;
    }
    return 0;
}
