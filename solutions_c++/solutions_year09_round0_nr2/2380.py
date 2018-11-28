#include <iostream>
#include <string>
using namespace std;

// NWES
int dx[] = { 0, -1, +1, 0 };
int dy[] = { -1, 0, 0, +1 };

int M[128][128];
int R[128][128];
int W, H;

bool valid(int x, int y) {
    return x>=0 && x<W && y>=0 && y<H;
}

int where(int x, int y) {
    int best = M[x][y];
    int result = -1;
    for (int d=0; d<4; d++) {
        int xx = x+dx[d], yy = y+dy[d];
        if (!valid(xx, yy)) continue;
        if (M[xx][yy]<best) result=d, best=M[xx][yy];
    }
    return result;
}


void floodfill(int x0, int y0, int basen) {
    R[x0][y0] = basen;
    for (int d=0; d<4; d++) {
        int xx = x0+dx[d], yy = y0+dy[d];
        if (!valid(xx, yy)) continue;
        int dd = where(xx, yy);
        if (dd==-1) continue;
        if (xx+dx[dd]==x0 && yy+dy[dd]==y0)
            floodfill(xx, yy, basen);
    }
}


int main() {

    int T; cin>>T;
    for (int t=0; t<T; t++) {
        cout<<"Case #"<<(t+1)<<":\n";
        cin>>H>>W;
        for (int y=0; y<H; y++)
            for (int x=0; x<W; x++)
                cin>>M[x][y], R[x][y]=0;
        
        int basen=1;
        for (int y=0; y<H; y++)
            for (int x=0; x<W; x++)
                if (where(x, y)==-1)
                    floodfill(x, y, basen++);
                    
        string rename = "..............................";
        char firstFree = 'a';
        for (int y=0; y<H; y++) {
            for (int x=0; x<W; x++) {
                if (rename[R[x][y]]=='.')
                    rename[R[x][y]]=firstFree++;
                cout<<rename[R[x][y]];
                //cout<<R[x][y]<<" ";
                if (x+1<W) cout<<" ";
            }
            cout<<"\n";
        }
    }

    return 0;
}
