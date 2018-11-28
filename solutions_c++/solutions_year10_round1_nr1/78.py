#include <iostream>
#include <string>
#include <vector>
#include <cstring>
using namespace std;

int N,K;

string ogrid[101];
char grid[101][101];

int dx[]={0,1,1,-1};
int dy[]={1,0,1,1};

bool solve(char c) {
    for(int i=0;i<N;i++) for(int j=0;j<N;j++) if(grid[i][j]==c) for(int k=0;k<4;k++) {
        int y=i, x=j;
        int sofar=0;
        while(sofar<K&&y<N&&x<N&&y>=0&&x>=0&&grid[y][x]==c) {
            sofar++;
            x+=dx[k];
            y+=dy[k];
        }
        if(sofar==K) return true;
    }
    return false;
}

/*void print() {
    for(int i=0;i<N;i++) {
        for(int j=0;j<N;j++)
            cout<<grid[i][j];
        cout<<endl;
    }
    cout<<endl<<endl<<endl;
}*/

void shift_down(int col, int row) {
    for(int i=row;i>0;i--) {
        grid[i][col] = grid[i-1][col];
    }
    grid[0][col]='.';
}

void rotate() {
    /*for(int i=0;i<N;i++) {
        cout<<ogrid[i]<<endl;
    }
    cout<<endl<<endl;*/
    for(int i=0;i<N;i++) for(int j=0;j<N;j++) {
        grid[j][N-1-i]=ogrid[i][j];
    }
    //print();
    for(int row=N-1;row>0;row--) {
        for(int i=0;i<N;i++) {
            bool has=false;
            for(int j=row-1;j>=0;j--) if(grid[j][i]!='.') has=true;
            if(!has) continue;
            while(grid[row][i]=='.') {
                //cout<<row<<"****"<<i<<endl;
                shift_down(i,row);
                //print();
            }
        }
    }
}

string solve() {
    rotate();
    bool red=solve('R'), blue=solve('B');
    if(red&&blue) return "Both";
    if(!red&&!blue) return "Neither";
    if(red) return "Red";
    if(blue) return "Blue";
    return "SHIT";
}

int main() {
    int cases;
    cin>>cases;
    for(int c=1;c<=cases;c++) {
        cin>>N>>K;
        for(int i=0;i<N;i++) cin>>ogrid[i];
        cout<<"Case #"<<c<<": "<<solve()<<endl;
    }
}
