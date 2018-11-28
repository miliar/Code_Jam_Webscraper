#include <iostream>
#include <fstream>
using namespace std;
    int C, N, M, A, x0, y0, x1, y1, x2, y2;
    int dx2, minx, miny;
bool isok(int dx1, int dy1, int dy2, int A){
    if (dy1 == 0){
        if (dx1 * dy2 == A){
            dx2 = 0;
        minx = min(min(dx1, 0), dx2);
        miny = min(min(dy1, 0), dy2);
        x0 = -minx;
        x1 = dx1 - minx;
        x2 = dx2 - minx;
        y0 = -miny;
        y1 = dy1 - miny;
        y2 = dy2 - miny;
        //cout << x0 << ' ' << y0 << ' ' << x1 << ' ' << y1 << ' ' << x2 << ' ' << y2 << endl;
        if (x0 <= N && x1 <= N && x2 <= N && y0 <= M && y1 <= M && y2 <= M) return true;
        }
        else return false;
    }
    if ((dx1 * dy2 - A) % dy1 == 0){
        dx2 = (dx1 * dy2 - A) / dy1;
        minx = min(min(dx1, 0), dx2);
        miny = min(min(dy1, 0), dy2);
        x0 = -minx;
        x1 = dx1 - minx;
        x2 = dx2 - minx;
        y0 = -miny;
        y1 = dy1 - miny;
        y2 = dy2 - miny;
        //cout << x0 << ' ' << y0 << ' ' << x1 << ' ' << y1 << ' ' << x2 << ' ' << y2 << endl;
        if (x0 <= N && x1 <= N && x2 <= N && y0 <= M && y1 <= M && y2 <= M) return true;
    }
    return false;
}
bool ok(){
    for(int dx1 = 0; dx1 <= N; ++ dx1)
        for(int dy1 = 0; dy1 <= M; ++ dy1)
            for(int dy2 = dy1 - M; dy2 <= M; ++ dy2){
                //cout << "hoho" << endl;
                if (isok(dx1, dy1, dy2, A))
                    return true;
                if (isok(dx1, dy1, dy2, -A)) return true;
                }
    return false;
}
int main(){
    ifstream cin("B-small-attempt0.in");
    ofstream cout("out.txt");
    cin >> C;
    for(int tcase = 1; tcase <= C; ++ tcase){
        cin >> N >> M >> A;
        cout << "Case #" << tcase << ": ";
        if (ok())
            cout << x0 << ' ' << y0 << ' ' << x1 << ' ' << y1 << ' ' << x2 << ' ' << y2 << endl;
        else cout << "IMPOSSIBLE" << endl;
    }
    return 0;
}
