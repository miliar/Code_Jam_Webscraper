/*
ID: Zupijs
PROG:
LANG: C++
*/

//{ Includes
#include <iostream>
#include <fstream>
//}

//{ Defines
#define in "B-large.in"
#define out "B-large.out"
#define maxH 100
#define maxW 100
//}

using namespace std;

struct cell
{
    int altitude;
    char letter;
    bool N, W, E, S;
};

int h, w;
cell map[maxH][maxW];

void DFS ( int i, int j, char basin)
{
    map[i][j].letter = basin;
    if ( i - 1 >= 0 && map[i][j].N == true && map[i-1][j].letter == '0' )
    {
        DFS ( i - 1, j, basin );
    }
    if ( j - 1 >= 0 && map[i][j].W == true && map[i][j-1].letter == '0' )
    {
        DFS ( i, j - 1, basin );

    }
    if ( j + 1 < w && map[i][j].E == true && map[i][j+1].letter == '0' )
    {
        DFS ( i, j + 1, basin );
    }
    if ( i + 1 < h && map[i][j].S == true && map[i+1][j].letter == '0' )
    {
        DFS ( i + 1, j, basin );
    }
}

int main()
{
	ifstream fin;
	fin.open( in );
	ofstream fout;
	fout.open( out );

	int c, n, i, j, min, flow;
	char cur;
	fin >> n;

	for ( c = 1; c <= n; c++ )
	{
        fin >> h >> w;
        cur = 'a';
        for ( i = 0; i < h; i++ )
        {
            for ( j = 0; j < w; j++ )
            {
                fin >> map[i][j].altitude;
                map[i][j].letter = '0';
                map[i][j].N = false;
                map[i][j].W = false;
                map[i][j].E = false;
                map[i][j].S = false;
            }
        }
        for ( i = 0; i < h; i++ )
        {
            for ( j = 0; j < w; j++ )
            {
                flow = 0;
                min = map[i][j].altitude;
                if ( i - 1 >= 0 && map[i-1][j].altitude < min )
                {
                    min = map[i-1][j].altitude;
                    flow = 1;
                }
                if ( j - 1 >= 0 && map[i][j-1].altitude < min )
                {
                    min = map[i][j-1].altitude;
                    flow = 2;
                }
                if ( j + 1 < w && map[i][j+1].altitude < min )
                {
                    min = map[i][j+1].altitude;
                    flow = 3;
                }
                if ( i + 1 < h && map[i+1][j].altitude < min )
                {
                    min = map[i+1][j].altitude;
                    flow = 4;
                }
                switch ( flow )
                {
                    case 1:
                        map[i][j].N = true;
                        map[i-1][j].S = true;
                        break;
                    case 2:
                        map[i][j].W = true;
                        map[i][j-1].E = true;
                        break;
                    case 3:
                        map[i][j].E = true;
                        map[i][j+1].W = true;
                        break;
                    case 4:
                        map[i][j].S = true;
                        map[i+1][j].N = true;
                        break;
                    default:
                        break;
                }
            }
        }
        for ( i = 0; i < h; i++ )
            {
                for ( j = 0; j < w; j++ )
                {
                    if ( map[i][j].letter == '0' )
                    {
                        DFS ( i, j, cur );
                        cur++;
                    }
                }
            }
        fout << "Case #" << c << ":" << endl;
        for ( i = 0; i < h; i++ )
            {
                for ( j = 0; j < w - 1; j++ )
                {
                    fout << map[i][j].letter << " ";
                }
                j = w - 1;
                fout << map[i][j].letter << endl;
            }

	}

	fin.close();
	fout.close();

	return 0;
}
