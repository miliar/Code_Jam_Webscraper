#include <cstdio>
#include <iostream>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <map>
#include <string>
#include <vector>
using namespace std;

int min_3(int a, int b, int c) {
    if( a>b )
        a=b;
    if( a>c )
        a=c;
    return a;
}
char to_num(char c) {
    if( c>='0' && c<='9' )
        return c-'0';
    else
        return c-'A'+10;
}
int max_square[512][512];
char color[513][513];
int get_max_sq(int x, int y) {
    if( x>=0 && x<512 && y>=0 && y<512 )
        return max_square[x][y];
    else
        return 0xFFFF;
}
void reset_max() {
    for(int i=0; i<512; i++) for(int j=0; j<512; j++)
        max_square[i][j] = 0xFFFF;
}
void reset_color() {
    for(int i=0; i<513; i++) for(int j=0; j<513; j++)
        color[i][j] = 2;
}
void cut(int x, int y, int size) {
    for(int i=0; i<size; i++) for(int j=0; j<size; j++)
        color[x+i][y+j] = 2;
}
void render(int x, char * line, int len) {
    for(int i=0; i<len; i++) {
        char c = to_num(line[i]);
        for(int j=0; j<4; j++)
            color[x][i*4+j] = ( ( (c >> (3-j)) + x + j ) & 1 );
    }
}

int count_max_sq(int x, int y) {
    int c00 = color[x][y], c10 = color[x+1][y], c01 = color[x][y+1], c11 = color[x+1][y+1];
    if( c00 == 2 )
        return 0;
    int a = get_max_sq(x+1, y+1), b = get_max_sq(x, y+1), c = get_max_sq(x+1, y);
    if( c00!=c11 ) a = 0; if( c00!=c01 ) b = 0; if( c00!=c10 ) c = 0;
    if( a!=0xFFFF && b!=0xFFFF && c!=0xFFFF ) {
        int d = min_3(a, b, c) + 1;
        max_square[x][y] = d;
        return d;
    } else {
        int ext = 1;
        for( ; ; ext++) {
            int flag = 0;
            for(int i=0; i<ext; i++) {
                if( c00 != color[x + ext][y + i] ) {
                    flag = 1;
                    break;
                }
            }
            for(int i=0; i<ext; i++) {
                if( c00 != color[x + i][y + ext] ) {
                    flag = 1;
                    break;
                }
            }
            if( c00 != color[x + ext][y + ext] )
                flag = 1;
            if( flag )
                break;
        }
        max_square[x][y] = ext;
        return ext;
    }
}

int main()
{
/*    reset_max();
    reset_color();
    color[0][0] = 0;
    color[0][1] = 0;
    color[1][0] = 0;
    color[1][1] = 0;
    count_max_sq(0, 0);
    cout << max_square[0][0] << endl;
    cout << max_square[1][1] << endl;
    count_max_sq(1, 1);
    cout << max_square[0][0] << endl;
    cout << max_square[1][1] << endl;
    return 0;*/
    int T;
    
    cin >> T;

    for(int i=1; i<=T; i++) {
        reset_max();
        reset_color();
        int M, N;
        char line[200];
        cin >> M >> N;
        for(int j=0; j<M; j++) {
            cin >> line;
            render(j, line, N/4);
        }
        map<int, int> m_map;
        for( ; ; ) {
            int max = 0, max_x, max_y;
            for(int x = M-1; x>=0; x--) for(int y = N-1; y>=0; y--) {
                int z = count_max_sq(x, y);
                if( !z )
                    continue;
                if(   z > max || 
                    ( z==max  &&  x<max_x ) ||
                    ( z==max  &&  x==max_x  && y<max_y ) ) {
                    max = z;
                    max_x = x;
                    max_y = y;
                }
            }
            if( max ) {
                cut( max_x, max_y, max );
                m_map[max] ++;
            } else
                break;
        }
        cout << "Case #" << i << ": " << m_map.size() << endl;
        for(map<int, int>::reverse_iterator it = m_map.rbegin(); it!=m_map.rend(); it++)
            cout << (*it).first << " " << (*it).second << endl;
    }
    
   // cin >> T;
    return 0;
}
