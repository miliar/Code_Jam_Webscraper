//
//  main.cpp
//  Square Tiles

#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
using namespace std;
static const double EPS = 1e-5;
typedef long long ll;


static vector<string> dfs( vector<string> picture )
{
    int r = (int)picture.size();
    int c = (int)picture[0].length();

    bool flag = false;
    for( int y = 0; y < r; y++ )
        for( int x = 0; x < c; x++ )
        {
            if( picture[y][x] == '#' )
                flag = true;
        }
    
    if( flag == false )
    {
        return picture;
    }
    
    for( int y = 0; y < r - 1; y++ )
        for( int x = 0; x < c - 1; x++ )
        {
            if( picture[y][x] == '#' && picture[y+1][x] == '#' && picture[y][x+1] == '#' && picture[y+1][x+1] == '#' )
            {
                vector<string> copy = picture;
                
                copy[y][x] = '/';
                copy[y+1][x] = 0x5c;
                copy[y][x+1] = 0x5c;
                copy[y+1][x+1] = '/';
                
                return dfs(copy);
            }
        }
    
    return picture;
}



int main (int argc, const char * argv[])
{
    FILE *in = fopen( "A-large.in", "rt" );
    int T;
    char line[1024];
    
    fgets(line, sizeof(line), in);
    sscanf(line, "%d", &T);

    for( int t = 0; t < T; t++ )
    {
        int R;
        int C;

        fgets(line, sizeof(line), in);
        sscanf(line, "%d %d", &R, &C);

        vector<string> picture;
        
        for( int r = 0; r < R; r++ )
        {
            string s;
            fgets(line, sizeof(line), in);
            s = line;
            s[s.length()-1] = '\0';
            picture.push_back(s);
        }

        vector<string> result = dfs(picture);
        
        bool flag = false;
        for( int y = 0; y < R; y++ )
            for( int x = 0; x < C; x++ )
            {
                if( result[y][x] == '#' )
                    flag = true;
            }
        
        cout << "Case #" << t + 1 << ":" << endl;
        
        if( flag == true )
            cout << "Impossible" << endl;
        else
            for( int y = 0; y < R; y++ )
                cout << result[y] << endl;
    }
    
    return 0;
}

