#include <iostream>

using namespace std;

int T;
int H,W;
int grid[101][101];
char ans[101][101];
char curL;

const int dx[4]={0,-1,1,0}, dy[4]={-1,0,0,1};

inline bool isValid(int r, int c) {
    return (r>=0&&r<H&&c>=0&&c<W);
}

char dfs(int r, int c) {
    //find the sink connected
    if(ans[r][c]=='S') return ans[r][c]=curL++;
    if(ans[r][c]!='#') return ans[r][c];
    int lowest=(1<<30);
    for( int k=0; k<4; k++ )
        if( isValid(r+dy[k],c+dx[k])  )
            lowest=min(lowest,grid[r+dy[k]][c+dx[k]]);

    for( int k=0; k<4; k++ )
        if( isValid(r+dy[k],c+dx[k]) && grid[r+dy[k]][c+dx[k]]==lowest ) {
            return ans[r][c]=dfs(r+dy[k],c+dx[k]);
        }
    return '!'; //something wrong
}


int main() {
    freopen("B-large.in","r",stdin);
    freopen("largeout.txt","w",stdout);

    cin >> T;
    for( int test=1; test<=T; test++ ) {
        cin >> H >> W;
        curL = 'a';
        for( int i=0; i<H; i++ )
            for( int j=0; j<W; j++ ) {
                cin >> grid[i][j];
                ans[i][j]='#';
            }
        //get sinks
        for( int i=0; i<H; i++ )
            for( int j=0; j<W; j++ ) {
                bool isSink=true;
                for( int k=0; k<4; k++ )
                    if( isValid(i+dy[k],j+dx[k]) && grid[i+dy[k]][j+dx[k]]<grid[i][j] )
                        isSink = false;
                if( isSink ) ans[i][j]='S';
            }
        cout << "Case #" << test << ":" << endl;
        for( int i=0; i<H; i++ ) {
            for( int j=0; j<W; j++ )
                if( j==W-1 ) cout << dfs(i,j);
                else cout << dfs(i,j) << " ";
            cout << endl;
        }

    }
    return 0;
}

