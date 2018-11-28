#include <cstdio>
#include <iostream>

using namespace std;

#define MAX_DIM     128
#define MAX_DIM_2   16384

int height[MAX_DIM][MAX_DIM];


char basin[MAX_DIM][MAX_DIM];

int stack[MAX_DIM_2][2];
int sp;
int h;
char ch;
//enum direction {BASIN=0, NORTH, WEST, EAST, SOUTH};
const int BASIN=0, NORTH=1, WEST=2, EAST=3, SOUTH=4;
int dir[MAX_DIM][MAX_DIM];

int main()
{
    int T;
    cin >> T;
    int new_h;
                       
    for(int case_num=1; case_num <= T; case_num++)
    {
        int H, W;
        cin >> H >> W;
       
        for(int i=0; i<H; i++)
        {
            for(int j=0; j<W; j++)
            {
                cin >> height[i][j];
            }
        }
       
        sp=0;
       
        for(int i=0; i<H; i++)
        {
            for(int j=0; j<W; j++)
            {
                dir[i][j] = BASIN;
                new_h = height[i][j];
                if( i>0 )
                {
//                    cout << "N\n";
                    if(height[i-1][j] < new_h)
                    {
//                        cout << "n\n";
                        new_h = height[i-1][j];
                        dir[i][j] = NORTH;
                    }
                }
                if( j>0 )
                {
//                    cout << "W\n";
                    if(height[i][j-1] < new_h)
                    {
//                        cout << "w\n";
                        new_h = height[i][j-1];
                        dir[i][j] = WEST;
                    }
                }
                if( j<(W-1) )
                {
//                    cout << "E\n";
                    if(height[i][j+1] < new_h)
                    {
//                        cout << "e\n";
                        new_h = height[i][j+1];
                        dir[i][j] = EAST;
                    }
                }
                if( i<(H-1) )
                {
//                    cout << "S\n";
                    if(height[i+1][j] < new_h)
                    {
//                        cout << "s\n";
                        new_h = height[i+1][j];
                        dir[i][j] = SOUTH;
                    }
                }
            }
        }

/*        for(int i=0; i<H; i++)
        {
            for(int j=0; j<W; j++)
            {
                cout << height[i][j] << " ";
            }
            cout << endl;
        }
        for(int i=0; i<H; i++)
        {
            for(int j=0; j<W; j++)
            {
                cout << dir[i][j] << " ";
            }
            cout << endl;
        }
*/        
        for(int i=0; i<H; i++)
        {
            for(int j=0; j<W; j++)
            {
                basin[i][j] = '0';
            }
        }
        
        ch = 'a';
        for(int i=0; i<H; i++)
        {
            for(int j=0; j<W; j++)
            {
                sp = 0;
                if(basin[i][j] == '0')
                {
                    if( NORTH == dir[i][j] ) if( '0' == basin[i-1][j] )
                    {
                        stack[sp][0] = i-1;
                        stack[sp][1] = j;
                        sp++;
                    }
                    if( WEST == dir[i][j] ) if( '0' == basin[i][j-1] )
                    {
                        stack[sp][0] = i;
                        stack[sp][1] = j-1;
                        sp++;
                    }
                    if( EAST == dir[i][j] ) if( '0' == basin[i][j+1] )
                    {
                        stack[sp][0] = i;
                        stack[sp][1] = j+1;
                        sp++;
                    }
                    if( SOUTH == dir[i][j] ) if( '0' == basin[i+1][j] )
                    {
                        stack[sp][0] = i+1;
                        stack[sp][1] = j;
                        sp++;
                    }
                    if( i>0 ) if( dir[i-1][j] == SOUTH ) if( '0' == basin[i-1][j] )
                    {
                        stack[sp][0] = i-1;
                        stack[sp][1] = j;
                        sp++;
                    }
                    if( j>0 ) if( dir[i][j-1] == EAST ) if( '0' == basin[i][j-1] )
                    {
                        stack[sp][0] = i;
                        stack[sp][1] = j-1;
                        sp++;
                    }
                    if( j<(W-1) ) if( dir[i][j+1] == WEST ) if( '0' == basin[i][j+1] )
                    {
                        stack[sp][0] = i;
                        stack[sp][1] = j+1;
                        sp++;
                    }
                    if( i<(H-1) ) if( dir[i+1][j] == NORTH ) if( '0' == basin[i+1][j] )
                    {
                        stack[sp][0] = i+1;
                        stack[sp][1] = j;
                        sp++;
                    }
                    basin[i][j] = ch;
                    while(sp)
                    {
                        int x, y;
                        sp--;
                        y = stack[sp][0];
                        x = stack[sp][1];
    
                        if( NORTH == dir[y][x] ) if( '0' == basin[y-1][x] )
                        {
                            stack[sp][0] = y-1;
                            stack[sp][1] = x;
                            sp++;
                        }
                        if( WEST == dir[y][x] ) if( '0' == basin[y][x-1] )
                        {
                            stack[sp][0] = y;
                            stack[sp][1] = x-1;
                            sp++;
                        }
                        if( EAST == dir[y][x] ) if( '0' == basin[y][x+1] )
                        {
                            stack[sp][0] = y;
                            stack[sp][1] = x+1;
                            sp++;
                        }
                        if( SOUTH == dir[y][x] ) if( '0' == basin[y+1][x] )
                        {
                            stack[sp][0] = y+1;
                            stack[sp][1] = x;
                            sp++;
                        }
                        if( y>0 ) if( dir[y-1][x] == SOUTH ) if( '0' == basin[y-1][x] )
                        {
                            stack[sp][0] = y-1;
                            stack[sp][1] = x;
                            sp++;
                        }
                        if( x>0 ) if( dir[y][x-1] == EAST ) if( '0' == basin[y][x-1] )
                        {
                            stack[sp][0] = y;
                            stack[sp][1] = x-1;
                            sp++;
                        }
                        if( x<(W-1) ) if( dir[y][x+1] == WEST ) if( '0' == basin[y][x+1] )
                        {
                            stack[sp][0] = y;
                            stack[sp][1] = x+1;
                            sp++;
                        }
                        if( y<(H-1) ) if( dir[y+1][x] == NORTH ) if( '0' == basin[y+1][x] )
                        {
                            stack[sp][0] = y+1;
                            stack[sp][1] = x;
                            sp++;
                        }
                        basin[y][x] = ch;
                    }
                    ch++;
                }
            }
        }
                
        cout << "Case #" << case_num <<":" << endl;
        for(int i=0; i<H; i++)
        {
            for(int j=0; j<W-1; j++)
            {
                cout << basin[i][j] << ' ';
            }
            cout << basin[i][W-1] << endl;
        }
    }
   
    return 0;
}

