#include<iostream>
#include<algorithm>
#include<tuple>
#include<map>
#include<utility>

using namespace std;

int main() {
    int T;
    cin >> T;
    for(int tt=1; tt<=T; tt++) {
        int H, W, a[200][200];
        cin >> H >> W;

        for(int i=0; i<=H+1; i++) 
            a[i][0] = a[i][W+1] = 100000;
        for(int j=0; j<=W+1; j++) 
            a[0][j] = a[H+1][j] = 100000;

        tuple<int, int, int> t[20000];
        for(int i=1, k=0; i<=H; i++) {
            for(int j=1; j<=W; j++) {
                cin >> a[i][j];
                t[k++] = make_tuple(a[i][j], i, j);
            }
        }
        sort(t, t + W*H);

        pair<int, int> flow[200][200];
        for(int i=0; i<H*W; i++) {
            int h = get<0>(t[i]);
            int x = get<1>(t[i]);
            int y = get<2>(t[i]);

            flow[x][y] = make_pair(x, y);

            if(a[x-1][y] < h) {
                h = a[x-1][y];
                flow[x][y] = flow[x-1][y];
            }
            if(a[x][y-1] < h) {
                h = a[x][y-1];
                flow[x][y] = flow[x][y-1];
            }
            if(a[x][y+1] < h) {
                h = a[x][y+1];
                flow[x][y] = flow[x][y+1];
            }
            if(a[x+1][y] < h) {
                h = a[x+1][y];
                flow[x][y] = flow[x+1][y];
            }
        }


        map<pair<int, int>, char> m;
        cout << "Case #" << tt << ":\n";
        for(int i=1; i<=H; i++) {
            for(int j=1; j<=W; j++) {
                if(m[flow[i][j]] == 0) m[flow[i][j]] = 'a' + m.size() - 1;
                cout << m[flow[i][j]];
                if(j == W) cout << endl;
                else cout << ' ';
            }
        }
    }
}

