#include <iostream>
#include <vector>

using namespace std;


bool a[210][210];
bool b[210][210];
const int MAX=200;


bool done() {
    for(int x=0; x<MAX; x++) for(int y=0; y<MAX; y++) {
        if (a[x][y]) return false;
    }
    return true;
}

int main() {
    int cases;
    cin >> cases;

    for(int c=0; c<cases; c++) {
        memset(a,0,sizeof(a));

        int R;
        cin >> R;
        for(int i=0; i<R; i++) {
            int x1,x2,y1,y2;
            cin >> x1 >> y1>>x2>>y2;
            if (x1>x2) swap(x1,x2);
            if (y1>y2) swap(y1,y2);
            for(int x=x1; x<=x2; x++) for(int y=y1; y<=y2; y++) a[50+x][50+y] = 1;
        }
            //for(int x=0; x<MAX; x++) { for(int y=0; y<MAX; y++) cout<<a[x][y];cout<<endl; }cout<<endl;

        int ans=0;
        while(!done()) {
            ans++;
            memset(b,0,sizeof(b));
            for(int x=0; x<MAX; x++) for(int y=0; y<MAX; y++) {
                int ne = 0;
                if (x>0 && a[x-1][y]) ne++;
                if (y>0 && a[x][y-1]) ne++;
                b[x][y] = (ne == 2 || (ne == 1 && a[x][y]));
            }
            for(int x=0; x<MAX; x++) for(int y=0; y<MAX; y++) a[x][y] = b[x][y];
        }

        cout << "Case #" <<(c+1) << ": " << ans << endl;
    }
}
