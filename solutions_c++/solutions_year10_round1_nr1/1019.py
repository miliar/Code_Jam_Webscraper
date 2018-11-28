#include <iostream>

using namespace std;

int test;
int n, k;
char c[100][100];
int dx[] = {1, 1, 0, 1};
int dy[] = {0, -1, 1, 1};
 

bool check(char ch)
{
    for ( int i = 0 ; i < n ; i ++ )
        for ( int j = 0 ; j < n ; j ++ ){
            if ( c[i][j] == ch ){
                int dem[4];
                for ( int u = 0 ; u < 4 ; u ++ )
                    dem[u] = 0;
                for ( int u = 0 ; u < 4 ; u ++ ){
                    int x = i;
                    int y = j;
                    while ( 0 <= x && x < n && 0 <= y && y < n && c[x][y] == ch){
                        dem[u]++;
                        x += dx[u];
                        y += dy[u]; 
                    }
                }
                for ( int u = 0 ; u < 4 ; u ++ )
                    if ( dem[u] >= k )
                        return true;
            }
        }
    return false;
}


void rotate()
{
    char kc[100][100];
    for ( int i = 0 ; i < n ; i ++ )
        for ( int j = 0 ; j < n ; j ++ )
            kc[i][j] = c[n-1-j][i];
    
    
    
    for ( int i = n - 1; i >= 0 ; i -- ){
        for ( int j = 0; j < n ; j ++ ){
            if ( kc[i][j] != '.' ){
                int x = i+1;
                while ( x < n && kc[x][j] == '.' )
                    x++;
                x--;
                if ( x == i ) continue;
                kc[x][j] = kc[i][j];
                kc[i][j] = '.';
            }
        }
    }
    
    
    for ( int i = 0 ; i < n ; i ++ )
        for ( int j = 0 ; j < n ; j ++ )
            c[i][j] = kc[i][j];
}

void process()
{
    bool bb = false, br = false;
    rotate();
    if ( check('B')) bb = true;
    if ( check('R')) br = true;
    
    if ( bb && br ) cout << "Both" << endl;
    else if ( bb ) cout << "Blue" << endl;
    else if ( br ) cout << "Red" << endl;
    else cout << "Neither" << endl;
}

void load()
{
    cin >> test;
    for ( int i = 0 ; i < test ; i ++){
        cout << "Case #" << i + 1 << ": ";
        cin >> n >> k;
        for ( int u = 0 ; u < n ; u ++ )
            for ( int v = 0 ; v < n ; v ++ )
                cin >> c[u][v];
        process();
    }
}

int main()
{
    load();
    return 0;
}
