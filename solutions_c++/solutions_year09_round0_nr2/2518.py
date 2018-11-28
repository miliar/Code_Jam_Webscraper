#include<iostream>
#include<string>

#define MAXSIZE 100 // small: 10; large: 100
#define MAXALTS 10000 // small: 10; large: 10000
#define MAXBASINS 26 // small: 2; large: 26

using namespace std;

enum dir { THIS, NORTH, WEST, EAST, SOUTH };
char dirSymbols[5] = { '.', '^', '<', '>', 'v' };

int T, H, W;
int map[MAXSIZE][MAXSIZE];
dir minmap[MAXSIZE][MAXSIZE];
char cmap[MAXSIZE][MAXSIZE];
char curBasin, curRealBasin;
char basinMap[MAXBASINS];

void dfs(int row, int col)
{
    cmap[row][col] = curBasin;

    if(row > 0 && cmap[row-1][col] == ' ' && minmap[row-1][col] == SOUTH)
        dfs(row-1, col);

    if(col > 0 && cmap[row][col-1] == ' ' && minmap[row][col-1] == EAST)
        dfs(row, col-1);

    if(col < (W-1) && cmap[row][col+1] == ' ' && minmap[row][col+1] == WEST)
        dfs(row, col+1);

    if(row < (H-1) && cmap[row+1][col] == ' ' && minmap[row+1][col] == NORTH)
        dfs(row+1, col);
}

int main(int argc, char *argv[])
{
    int row, col;
    int minval;
    dir mindir;

    cin>>T;
    for(int mycase=1; mycase<=T; mycase++)
    {
        cin>>H>>W;
        for(row=0; row<H; row++)
        {
            for(col=0; col<W; col++)
            {
                cin>>map[row][col];
                minmap[row][col] = THIS;
                cmap[row][col] = ' ';
            }
        }

        for(row=0; row<H; row++)
        {
            for(col=0; col<W; col++)
            {
                minval = map[row][col];
                mindir = THIS;

                if(row > 0 && map[row-1][col] < minval)
                {
                    minval = map[row-1][col];
                    mindir = NORTH;
                }

                if(col > 0 && map[row][col-1] < minval)
                {
                    minval = map[row][col-1];
                    mindir = WEST;
                }

                if(col < (W-1) && map[row][col+1] < minval)
                {
                    minval = map[row][col+1];
                    mindir = EAST;
                }

                if(row < (H-1) && map[row+1][col] < minval)
                {
                    minval = map[row+1][col];
                    mindir = SOUTH;
                }

                minmap[row][col] = mindir;
                
                //cout<<dirSymbols[minmap[row][col]]<<" ";
            }
            //cout<<endl;
        }

        curBasin='A';
        // For each min-point, color it, then run a search (dfs/bfs) from there...
        for(row=0; row<H; row++)
        {
            for(col=0; col<W; col++)
            {
                if(minmap[row][col]==THIS)
                {
                    dfs(row, col);
                    curBasin++;
                }
            }
        }

        // Now re-map to bring in the correct lexicographic order...
        for(curBasin='A'; curBasin<=('A'+MAXBASINS); curBasin++)
            basinMap[curBasin - 'A'] = ' ';

        curRealBasin = 'a';
        for(row=0; row<H; row++)
        {
            for(col=0; col<W; col++)
            {
                if(basinMap[cmap[row][col] - 'A'] == ' ')
                {
                    basinMap[cmap[row][col] - 'A'] = curRealBasin;
                    cmap[row][col] = curRealBasin;
                    curRealBasin++;
                }
                else
                    cmap[row][col] = basinMap[cmap[row][col] - 'A'];
            }
        }

        cout<<"Case #"<<mycase<<": "<<endl;
        for(row=0; row<H; row++)
        {
            for(col=0; col<W; col++)
                cout<<cmap[row][col]<<' ';

            cout<<endl;
        }
    }

    //system("pause");
    return 0;
}