#include <iostream>


using namespace std;

int alt[100][100];
char map[100][100];
char mark;
int path[10000];
int pc;
int dx[] = {-1,0,0,1};
int dy[] = {0, -1, 1, 0};
int h,w;

int getmindir(int x, int y)
{
    int md = -1;
    int min = alt[x][y];
    for(int dir=0;dir<4;dir++)
    {
        int nx = x+dx[dir];
        int ny = y+dy[dir];
        if((nx >=0 && nx < h && ny >=0 && ny < w) && (alt[nx][ny] < min))
        {
            min = alt[nx][ny];
            md = dir;
        }
    }
    return md;
}

int main()
{
    FILE* in = freopen("B-large.in", "r", stdin);
    FILE* out = freopen("B-large.out", "w+", stdout);


    int cases;
    cin>>cases;

    for(int q=1;q<=cases;++q)
    {
        int x,y;
        cin>>h>>w;
        memset(map,0,sizeof(map));
        mark = 'a';
        pc = 0;
        for(int i=0;i<h;++i)
        {
            for(int j=0;j<w;++j)
            {
                cin>>alt[i][j];
            }
        }
        while(true)
        {
            x = 0;y = 0;
            while(0 != map[x][y])
            {
                ++y;
                if(y>=w)
                {
                    ++x;
                    y=0;
                }
                if(x>=h)
                {
                    break;
                }
            }
            if(x>=h)
                break;

            pc = 0;
            while(0 == map[x][y])
            {
                int dir = getmindir(x,y);
                if(-1 == dir)
                    break;
                path[pc++] = dir;
                x+=dx[dir];
                y+=dy[dir];
            }
            char cm = map[x][y];
            if(0==cm)
                cm = mark++;

            for(--pc;pc>=0;--pc)
            {
                map[x][y] = cm;
                x-=dx[path[pc]];
                y-=dy[path[pc]];
            }
            map[x][y] = cm;
        }
        cout<<"Case #"<<q<<":\n";
        for(int i=0;i<h;++i)
        {
            for(int j=0;j<w;++j)
            {
                cout<<map[i][j]<<' ';
            }
            cout<<'\n';
        }
    }
}
