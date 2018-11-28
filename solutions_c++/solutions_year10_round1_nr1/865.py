#include <iostream>
#include <vector>
using namespace std;

vector< vector<char> > t;
int n, k;
void entrada()
{
    cin >> n >> k;
    t.clear();
    t = vector< vector<char> >(n);
    for (int i = 0; i < n; ++i)
    {
        t[i] = vector<char>(n);
        for ( int j = 0; j < n; ++j )
            cin >> t[i][j];
    }
}

void print()
{
    for (int i = 0; i < n; ++i)
    {
        for ( int j = 0; j < n; ++j )
            cout << t[i][j];
        cout << endl;
    }
    cout << endl;
}

void rotate()
{
    for (int i = n-1; i >= 0; --i)
    {
        for ( int j = n-1; j >= 0; --j )
        {
            if ( t[i][j] != '.' )
            {
                int pos = j;
                for ( int k = j+1; k < n; ++k )
                    if ( t[i][k] == '.' )
                        pos = k;
                    else break;
                //cout << i << " " << j << " " << pos << endl;
                if ( pos != j )
                {
                    t[i][pos] = t[i][j];
                    t[i][j] = '.';
                }
                //print();
            }
        }
    }
}

string verify()
{
    bool r = false, b = false;
    for (int i = 0; i < n; ++i)
    {
        int cont = 1;
        for ( int j = 1; j < n; ++j )
        {
            if ( t[i][j] != '.' and t[i][j] == t[i][j-1] )
                ++cont;
            else cont = 1;
            
            if ( cont == k )
                if ( t[i][j] == 'B' ) b = true;
                else if ( t[i][j] == 'R' ) r = true;
            //cout << i << " " << j << " " << cont << endl;
        }
    }
    //cout << r << " " << b << endl;
    
    for ( int j = 0; j < n; ++j )
    {
        int cont = 1;
        for (int i = 1; i < n; ++i)
        {
            if ( t[i][j] != '.' and t[i][j] == t[i-1][j] )
                ++cont;
            else cont = 1;
            
            if ( cont == k )
                if ( t[i][j] == 'B' ) b = true;
                else if ( t[i][j] == 'R' ) r = true;
        }
    }
    //cout << r << " " << b << endl;
    
    for (int i = -(n-1); i <= n-1; ++i)
    {
        int cont = 1;
        for (int j = 1; j < n; ++j)
        {
            int y = j, x = j+i;
            if ( x < 0 or x >= n ) continue;
            if ( x-1 < 0 or x-1 >= n ) continue;
            
            if ( t[y][x] != '.' and t[y][x] == t[y-1][x-1] )
                ++cont;
            else cont = 1;
            
            if ( cont == k )
                if ( t[y][x] == 'B' ) b = true;
                else if ( t[y][x] == 'R' ) r = true;
            //cout << y << " " << x << " " << cont << endl;
        }
        //cout << endl;
    }
    //cout << r << " " << b << endl;
    
    for (int i = 0; i <= 2*n-1; ++i)
    {
        int cont = 1;
        for (int j = 1; j < n; ++j)
        {
            int y = j, x = i-j;
            if ( x < 0 or x >= n ) continue;
            if ( x+1 < 0 or x+1 >= n ) continue;
            
            if ( t[y][x] != '.' and t[y][x] == t[y-1][x+1] )
                ++cont;
            else cont = 1;
            
            if ( cont == k )
                if ( t[y][x] == 'B' ) b = true;
                else if ( t[y][x] == 'R' ) r = true;
                
            //cout << y << " " << x << " " << cont << endl;
        }
        //cout << endl;
    }
    //cout << r << " " << b << endl;
    
    if ( r and b ) return "Both";
    if ( r ) return "Red";
    if ( b ) return "Blue";
    return "Neither";
}

int main()
{
    int casos; cin >> casos;
    for (int i = 0; i < casos; ++i)
    {
        entrada();
        //print();
        rotate();
        //cout << n << " " << k << endl;
        //print();
        
        cout << "Case #" << i+1 << ": " << verify() << endl;
    }
}
