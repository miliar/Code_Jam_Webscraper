#include <iostream>
using namespace std;
int box[100][100], H, W, sink;
char drain[100][100];
bool vis[100][100];

char trace(int row, int col)
{
    if(drain[row][col] != '.') return drain[row][col];
    int smallest = box[row][col];
    int dir[4][2] = {-1,0,0,-1,0,1,1,0};
    
    bool anyLower = 0;
    for(int i=0; i<4; i++)
    {
        int r = row + dir[i][0];
        int c = col + dir[i][1];
        if(r >= 0 && r < H && c >= 0 && c < W && box[r][c] < smallest)
        {
            anyLower = 1;
            smallest = box[r][c];
        }
    }
    
    if(anyLower == 0)
    {
        drain[row][col] = 'a' + sink;
        sink ++;
        return drain[row][col];
    }
    
    for(int i=0; i<4; i++)
    {
        int r = row + dir[i][0];
        int c = col + dir[i][1];
        if(r >= 0 && r < H && c >= 0 && c < W && box[r][c] == smallest)
        {
            if(drain[r][c] == '.') drain[r][c] = trace(r,c);
            return drain[r][c];
        }
    }
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    
    int T;
    cin >> T;
    for(int t=1; t<=T; t++)
    {
        cin >> H >> W;
        for(int i=0; i<H; i++) for(int j=0; j<W; j++) cin >> box[i][j];
        
        memset(drain, '.', sizeof(drain));
        sink = 0;
        
        for(int i=0; i<H; i++)
            for(int j=0; j<W; j++)
                if(drain[i][j] == '.') drain[i][j] = trace(i,j);

        cout << "Case #" << t << ":" << endl;
        for(int i=0; i<H; i++, cout << endl) for(int j=0; j<W; j++)
        {
            if(j > 0) putchar(' ');
            cout << drain[i][j];
        }
    }
}
